import os
import random

def semiRandomize():

# ----------------------------#
# Settings
#----------------------------#

    videoList = os.listdir("C:/Users/ramme/Dev/Manip-Maitrise/Amusement_Comportementale/video/") # Get a list of every video in folder
    
    videoDict={} # This dict will contain a key (the name of the video) and a value for the type of video  
    for name in videoList:
        videoDict[name]= name[0]
            
    bloc1=[]
    bloc2=[]
    bloc3=[]
    
    #Video Settings
    TOTAL= len(videoList) # Number of total video in the
    Max= TOTAL/9

#-------------------------- --#
# First Bloc
# ----------------------------#

    count1=0
    count2=0
    count3=0
    typeList = []


    while True:

        #Get random video
        video = random.choice(list(videoDict.keys()))
        videoType = int(videoDict[video])
        
        # Add the first 3 video without type restriction
        if len(bloc1) < 3:
            
            bloc1.append(video)
            typeList.append(videoType)
            del videoDict[video]
            
            if videoType == 1:
                count1+=1
                continue
            elif videoType == 2:
                count2+=1
                continue
            elif videoType == 3:
                count3+=1
                continue
            else:
                print('Error')

        #Check if the video type have reach the maximum, if so, restart
        elif (videoType == 1 and count1 == Max) or (videoType == 2 and count2 == Max) or (videoType == 3 and count3 == Max):
            continue

        # Check if the videoType is the same as the last 3 AND if it is not the last 3 videos to add
        elif videoType == typeList[-1] and videoType == typeList[-2] and videoType == typeList[-3] and len(bloc1) < ((TOTAL/3) - 3):
            continue

        else:
            bloc1.append(video)
            typeList.append(videoType)
            del videoDict[video]

            if len(bloc1) == (TOTAL/3):
                break

            if videoType == 1:
                count1+=1
                continue

            elif videoType == 2:
                count2+=1
                continue

            elif videoType == 3:
                count3+=1
                continue


# -----------------------------#
# Second Bloc
# -----------------------------#

    count1 = 0
    count2 = 0
    count3 = 0
    typeList = []

    while True:

        # Get random video
        video = random.choice(list(videoDict.keys()))
        videoType = int(videoDict[video])

        # Add the first 3 video without type restriction
        if len(bloc2) < 3:

            bloc2.append(video)
            typeList.append(videoType)
            del videoDict[video]

            if videoType == 1:
                count1 += 1
                continue
            elif videoType == 2:
                count2 += 1
                continue
            elif videoType == 3:
                count3 += 1
                continue

        # Check if the video type have reach the maximum, if so, restart
        elif (videoType == 1 and count1 == Max) or (videoType == 2 and count2 == Max) or (
                videoType == 3 and count3 == Max):
            continue

        # Check if the videoType is the same as the last 3 AND if it is not the last 3 videos to add
        elif videoType == typeList[-1] and videoType == typeList[-2] and videoType == typeList[-3] and len(
                bloc2) < ((TOTAL/3) - 3):
            continue

        else:
            bloc2.append(video)
            typeList.append(videoType)
            del videoDict[video]

            if len(bloc2) == (TOTAL/3):
                break

            if videoType == 1:
                count1 += 1
                continue

            elif videoType == 2:
                count2 += 1
                continue

            elif videoType == 3:
                count3 += 1
                continue

# -----------------------------#
# Third Bloc
# -----------------------------#

    count1 = 0
    count2 = 0
    count3 = 0
    typeList = []

    while True:

        # Get random video
        video = random.choice(list(videoDict.keys()))
        videoType = int(videoDict[video])

        # Add the first 3 video without type restriction
        if len(bloc3) < 3:

            bloc3.append(video)
            typeList.append(videoType)
            del videoDict[video]

            if videoType == 1:
                count1 += 1
                continue
            elif videoType == 2:
                count2 += 1
                continue
            elif videoType == 3:
                count3 += 1
                continue

        # Check if the video type have reach the maximum, if so, restart
        elif (videoType == 1 and count1 == Max) or (videoType == 2 and count2 == Max) or (
                        videoType == 3 and count3 == Max):
            continue

        # Check if the videoType is the same as the last 3 AND if it is not the last 3 videos to add
        elif videoType == typeList[-1] and videoType == typeList[-2] and videoType == typeList[-3] and len(
                bloc3) < ((TOTAL/3) - 3):
            continue

        else:
            bloc3.append(video)
            typeList.append(videoType)
            del videoDict[video]

            if len(bloc3) == (TOTAL/3): # Check if done (reach 1/3 of the video)
                break

            if videoType == 1:
                count1 += 1
                continue

            elif videoType == 2:
                count2 += 1
                continue

            elif videoType == 3:
                count3 += 1
                continue

    return bloc1, bloc2, bloc3