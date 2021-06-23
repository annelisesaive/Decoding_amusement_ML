
from psychopy import visual
from flow_amusement import *
from utility_amusement import *
import cv2

# ----------------------------#
# Variables
#----------------------------#

#Data
globalData={} # list that contain value of the participant *will be added to every dict of newData at the end
trialData={} # Dict that contain the data for the specific trial
CSVdata = []
frameID = 0

# Experience

## Experience : progress setting
state = '' # text / emotion / fixation / video / rating
expProgress = '' # intro / blocP / emotion1 / bloc1 / bloc2 / bloc3 / emotion2 / ending / resume
blocProgress = '' # intro / initialFix / video / endFix / rating / ending

## Experience : Setting for the fixation
fixationStart = ''
fixationDuration = '' 

# Videos
ListBloc = {} # Dict that contains videos name for each bloc
videoOrder = 0 # Index number

# UI
win = None  # Main windows
activeStims = []

#Configs
testing = True
bug = False # set BUG to False to run the full manip // set BUG to True to set manually the videos to watch


# ----------------------------#
# Program
#----------------------------#

#Setting participant
globalData['ParticipantID'] = setParticipantSetting()

#Setting Videos
ListBloc, videoOrder, ListEmotion = defineVideoList(globalData, bug, testing)
ListBloc['blocTest']=['1Neutral_biking_amsterdam.mp4']
index=0
trialID=0

# Configure webcam
vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'MP4V')
output = cv2.VideoWriter("data/Participant"+globalData['ParticipantID']+".mp4", vid_cod, 20.0, (640,480))

# Initialize experience
win = createScreen()
globalData['StartTime']=time.time()

# Configure starting state
state = 'text'
expProgress = 'intro'
activeStims.append(textScreen(win, "Lors de cette expérience, vous aurez à indiquer, après chaque vidéo, si elle était drôle ou pas."\
        "Vous aurez également à évaluer votre humeur au début et à la fin de l’étude.\n\n"\
        "L'expérience se déroule en trois blocs où chaque bloc dure au plus 15 minutes. Vous pourrez prendre une pause entre chaque bloc."\
        "En plus des trois blocs, nous ferons un bloc de pratique.\n\n"\
        "Appuyez sur une touche lorsque vous êtes prêt à commencer"))


print(ListBloc)

while True:
    
    # update WebCam
    ret,frame = vid_capture.read()
    output.write(frame)
    frameID+=1

    # Update Stimuli
    for stim in activeStims:
        stim.draw()
        
    win.flip()

    # Check if the condition to change have been done 
    if checkStateChange(state, activeStims, fixationStart, fixationDuration) is True:

        ret,frame = vid_capture.read()
        output.write(frame)
        frameID+=1
        
        #Update the data if we are at the end of the rating phase
        if state == 'rating':
            updateRating(expProgress, trialData,globalData, activeStims, frameID, ListEmotion, ListBloc, blocProgress)
            
            #Update Webcam
            ret,frame = vid_capture.read()
            output.write(frame)
            frameID+=1

            if expProgress == 'blocP' or expProgress == 'bloc1' or expProgress == 'bloc2' or expProgress == 'bloc3':

                #Update Webcam
                ret,frame = vid_capture.read()
                output.write(frame)
                frameID+=1
                
                # Save CSV
                if blocProgress == 'ratingFunny':
                    CSVdata.append(Merge(trialData, globalData))
                    trialData={}
                    with open('data/participant'+globalData['ParticipantID']+'.csv', 'w', newline='') as output_file:
                        keys=CSVdata[-1].keys()
                        dict_writer = csv.DictWriter(output_file, keys)
                        dict_writer.writeheader()
                        dict_writer.writerows(CSVdata)
                
                
                ret,frame = vid_capture.read()
                output.write(frame)
                frameID+=1
        
        #update the expProgress
        expProgress, blocProgress, state = updateExpProgress(expProgress, blocProgress, ListBloc, ListEmotion)
        
        ret,frame = vid_capture.read()
        output.write(frame)
        frameID+=1
        
                
        ret,frame = vid_capture.read()
        output.write(frame)
        frameID+=1
        
        #change stimuli
        
        activeStims, fixationStart, fixationDuration, index, trialID = updateStimuli(win, expProgress, blocProgress, ListBloc, ListEmotion, trialData, trialID, index, frameID)
                
        #check if we are done
        if activeStims == None:
            break
            
        ret,frame = vid_capture.read()
        output.write(frame)
        frameID+=1
        
            
        

#Update and save data to CSV

globalData['EndTime']=time.time()
globalData['EndFrame']= frameID

for dict in CSVdata:
    dict = dict.update(globalData)

keys = CSVdata[-1].keys()
with open('data/participant'+globalData['ParticipantID']+'_FINAL.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(CSVdata)

# End webacam
vid_capture.release() # close the already opened camera
output.release() # close the already opened file
cv2.destroyAllWindows() # close the window and de-allocate any associated memory usage

print('terminate without error')

