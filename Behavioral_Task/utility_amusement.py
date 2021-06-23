import os, sys
from psychopy import visual, sound
from psychopy import core, event, gui
import random
from VideoOrder import semiRandomize
import csv
import time


#-----------------------------------#
#                                   #
#       Fonctions used in the       #
#             experiment            #
#                                   #
#-----------------------------------#


# ---------------------------------------------------------------------- #
#
# SET THE PARTICIPANT
# Fonction to create a new Participant

# ---------------------------------------------------------------------- #

def setParticipantSetting():
    
    # Create and open a GUI where we can set the ParticipantID
    
    myDlg = gui.Dlg(title="Humor - Experience")
    myDlg.addField('ParticipantID:')
    data = myDlg.show()

    ParticipantID = str(data[0])
    name="data/participant"+ParticipantID+".csv"

    #Check if csv already exist for this participantID
    if os.path.isfile(name) is True:
        print("\n\nError : The participantID already exist\nparticipant"+ParticipantID+".csv // already exist")
        sys.exit()

    return ParticipantID



# -------------------------------------------------------------------#
#
# DEFINE VIDEO ORDER
# Fonction to define in wich order the participant will be watching the video
#
# ---------------------------------------------------------------------- #

def defineVideoList(globalData, bug=False, testing=False):

    # Normal experience (from the beginning)
    if bug is False:
        
        # In testing mode, there's only 6 video to watch
        if testing is True:
            ListBloc={'1':['1Neutral_baseball_GA.mp4', '2EDIT2_funny_monkeyz_sans_logo.mp4'], '2':['1Neutral_excavator.mp4', '3Humour_cat_fall_GA.mp4'], '3':['3edited2_H_sport_LG 8.mp4', '3Humour_otter_GA.mp4']} 
        
        # Normal experience with pseudo-randomize video order 
        else:
            ListBloc={}
            ListBloc['1'], ListBloc['2'], ListBloc['3'] = semiRandomize()
        
        videoOrder= 1
        
        # Save in the ListVideo.csv the participant ID and the video order in case there's a bug and we need to get the video order to restart
        saveCSV('ListVideo.csv', ['ParticipantID', 'Bloc1', 'Bloc2', 'Bloc3'], {'ParticipantID':globalData['ParticipantID'], 'Bloc1':ListBloc['1'], 'Bloc2':ListBloc['2'], 'Bloc3':ListBloc['3']} )
        
    # Manually edit if there's a bug and we need to restart the experiment
    elif bug is True:
        ListBloc={} # Add Manually the video from Listvideo.csv
        total=0
        
    if testing is True:
        emotionList1=['Intéressé(e)!Interested', 'Angoissé(e)!Distressed']
        emotionList2=['Intéressé(e)!Interested', 'Angoissé(e)!Distressed']
        
    if testing is False:
        emotionList1=['Intéressé(e)!Interested', 'Angoissé(e)!Distressed','Excité(e)!Excited', 'Fâché(e)!Upset', 'Fort(e)!Strong',\
        'Coupable!Guilty', 'Effrayé(e)!Scared', 'Hostile!Hostile', 'Enthousiaste!Enthusiastic', 'Fier(e)!Proud', 'Irrité(e)!Irritable',\
        'Alerte!Alert',  'Honteux(se)!Ashamed', 'Inspiré(e)!Inspired', 'Nerveux(se)!Nervous', 'Déterminé(e)!Determined', 'Attentif(ve)!Attentive',\
        'Agité(e)!Jittery', 'Actif(ve)!Active', 'Craintif(ve)!Afraid']
        emotionList2=['Intéressé(e)!Interested', 'Angoissé(e)!Distressed','Excité(e)!Excited', 'Fâché(e)!Upset', 'Fort(e)!Strong',\
        'Coupable!Guilty', 'Effrayé(e)!Scared', 'Hostile!Hostile', 'Enthousiaste!Enthusiastic', 'Fier(e)!Proud', 'Irrité(e)!Irritable',\
        'Alerte!Alert',  'Honteux(se)!Ashamed', 'Inspiré(e)!Inspired', 'Nerveux(se)!Nervous', 'Déterminé(e)!Determined', 'Attentif(ve)!Attentive',\
        'Agité(e)!Jittery', 'Actif(ve)!Active', 'Craintif(ve)!Afraid']
        
        
    ListEmotion = {'pre':emotionList1, 'post':emotionList2}
        
    return ListBloc, videoOrder, ListEmotion
    
    
    
# -------------------------------------------------------------------#    
#
# CREATE THE MAIN WINDOWS
# Functions to create the screen (ex: size, color, etc.)
#
# ---------------------------------------------------------------------- #

def createScreen():
    # Create the screen
    win = visual.Window(monitor="testMonitor", fullscr=False) #, size= [1920, 1080]) # size=[1920, 1080])
    win.mouseVisible = False
    
    return win



# -------------------------------------------------------------------#    
#
# CREATE A TEXT SCREEN
# Fonction that create a text stimuli to display (setting good for text only screen)
#
# ---------------------------------------------------------------------- #

def textScreen(win, text, height=None): # Require a string with the text to display        
    textStimuli = visual.TextStim(win, text,wrapWidth=1.5, height=height)

    return textStimuli



# ---------------------------------------------------------------------- #
#
# SAVE INTO CSV
# Function that save a dictionnaire into a csv file (requier more than one row to work)
#
# ---------------------------------------------------------------------- #

def saveCSV(CSVname, COLUMNname, data ):
    with open(CSVname, "a", newline='') as f:
        writer = csv.DictWriter(f, COLUMNname)
        if os.stat(CSVname).st_size == 0:
            writer.writeheader()
        writer.writerow(data)
        



# ---------------------------------------------------------------------- #
# 
# SEND TRIGGER
# Fonction that send a trigger via parallel port with a number between 1 and 255
# 
# ---------------------------------------------------------------------- #

def sendTrigger(name):
    return
#   print(name)


# Trigger 100 for begining and end of the experiment. Trigger 200 for beginning and end of the emotions rating
# Trigger the type of the video (1, 2 or 3) and the code of what is happening 
# (1= start of the 1st fixation cross; 2= Start of video; 3=Start of 2nd fixation cross; 4= Start of rating; 5=End of rating) 


def fixation(win): # Return a stimuli (fixation cross & the time it appear)
    fix = visual.TextStim(win, '+')
    return fix
    
def movieStimuli(win, videoName):
    film = 'video/'+videoName # Name of the movie to play
    movie = visual.MovieStim3(win, film, size=(500,400))
    
    return movie
    
def ratingStimuli(win, question, image, label):
        
    title = visual.TextStim(win, question, height=0.1, alignHoriz='center', wrapWidth=1.3, pos=(0.0, 0.4))
    image = visual.ImageStim(win, image,units='pix', size=(2000,600), pos=(0.0, -70.0))
    ratingScale = visual.RatingScale(win, labels=label,scale=None,markerColor='black',\
        high=100, size=1.22, stretch=1.855, showValue=False, showAccept=False,\
        tickHeight=0.0, lineColor='black', singleClick=True)
        
    return title, image, ratingScale
    
def ratingStimuli2(win, question, image, label):
        
    title = visual.TextStim(win, question, height=0.1, alignHoriz='center', wrapWidth=1.3, pos=(0.0, 0.4))
    image = visual.ImageStim(win, image,units='pix', size=(1300,300), pos=(0.0, -65.0))
    ratingScale = visual.RatingScale(win, labels=label,scale=None,markerColor='black',\
        high=100, size=1.22, stretch=1.855, showValue=False, showAccept=False,\
        tickHeight=0.0, lineColor='black', singleClick=True)
        
    return title, image, ratingScale
    
def ratingEmotion(win, emotion):
    choice=['       Très peu\n  ou pas du tout', 'Peu', 'Modérément', 'Beaucoup', "Énormément"]
    EmoFrench, EmoEnglish = emotion.split('!')

    title = visual.TextStim(win, "À quel point ressentez vous l'émotion suivante présentement: ", pos=(0.0,0.3), height=0.09)
    emotionShow = visual.TextStim(win, EmoFrench)
    ratingScale = visual.RatingScale(win, scale=None,markerColor='blue', textSize=0.8, \
        choices=choice,\
        size=1.2, stretch=1.9, showValue=False, acceptPreText='Valider', acceptText='Valider')
        
    return ratingScale, title, emotionShow, EmoEnglish
    
def changeRating(rating):
    choice=['       Très peu\n  ou pas du tout', 'Peu', 'Modérément', 'Beaucoup', "Énormément"]
    if rating == choice[0]:
        return 1
    elif rating == choice[1]:
        return 2
    elif rating == choice[2]:
        return 3
    elif rating == choice[3]:
        return 4
    elif rating == choice[4]:
        return 5
        
        
def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res
    
