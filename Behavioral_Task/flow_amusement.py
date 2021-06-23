import os, sys
from psychopy import visual, sound
from psychopy import core, event, gui
import random
from VideoOrder import semiRandomize
import csv
import time
from utility_amusement import *
import cv2



#-----------------------------------#
#                                   #
#             Flow of the           #
#             experiment            #
#                                   #
#-----------------------------------#


# Check if we are done with this screen
def checkStateChange(state, activeStims, fixationStart, fixationDuration):
# state : text / emotion / fixation / video / rating

    # STATE = TEXTE SCREEN
    if state == 'text':
        if len(event.getKeys())>0:
            return True
    
    # STATE = FIXATION CROSS
    if state == 'fixation':
        if time.time() - fixationStart >= fixationDuration:
            return True
    
    # STATE = WATCHING THE VIDEO
    if state == 'video':
        if activeStims[0].status == visual.FINISHED: ## change movie if the new variable is not name movie
            return True

    # STATE = RATING THE VIDEO
    if state == 'rating':
        
        if activeStims[2].noResponse: ## change ratingScale if the new variable is not name ratingScale
            return False
        else:
            return True


# Move foward in the experiment
def updateExpProgress(expProgress, blocProgress, ListBloc, ListEmotion): # return new 1- expProgress, 2- blocProgress, 3- state
    if expProgress == 'intro':
        return 'blocP', 'introText', 'text'
        
    if expProgress == 'blocP':
        if blocProgress == 'introText':
            return 'blocP', 'initialFix', 'fixation'
        if blocProgress == 'initialFix':
            return 'blocP', 'video', 'video'
        if blocProgress == 'video':
            return 'blocP', 'endFix', 'fixation'
            
        if blocProgress == 'endFix':
            return 'blocP', 'ratingArousal', 'rating'
        
        #Rating
        if blocProgress == 'ratingArousal':
            return 'blocP', 'ratingPleasant', 'rating'
            
        if blocProgress == 'ratingPleasant':
            return 'blocP', 'ratingFunny', 'rating'
            
        if blocProgress == 'ratingFunny':
            if not ListBloc['blocTest']:
                    return 'blocP', 'endText', 'text'
            else:
                return 'blocP', 'initialFix', 'fixation'
        
        #End text
        if blocProgress == 'endText':
            return 'emotionPre', 'introText', 'text'

    if expProgress == 'emotionPre':
        
        if blocProgress == 'introText':
            return 'emotionPre', 'rating', 'rating'
        if blocProgress == 'rating':
            if not ListEmotion['pre']:
                return 'bloc1', 'introText', 'text'
            else:
                return 'emotionPre', 'rating', 'rating'

    if expProgress == 'bloc1':
        if blocProgress == 'introText':
            return 'bloc1', 'initialFix', 'fixation'

        if blocProgress == 'initialFix':
            return 'bloc1', 'video', 'video'

        if blocProgress == 'video':
            return 'bloc1', 'endFix', 'fixation'
            
        if blocProgress == 'endFix':
            return 'bloc1', 'ratingArousal', 'rating'
        
        #Rating
        if blocProgress == 'ratingArousal':
            return 'bloc1', 'ratingPleasant', 'rating'
            
        if blocProgress == 'ratingPleasant':
            return 'bloc1', 'ratingFunny', 'rating'
            
        if blocProgress == 'ratingFunny':
            if not ListBloc['1']:
                    return 'bloc1', 'endText', 'text'
            else:
                return 'bloc1', 'initialFix', 'fixation'
        
        if blocProgress == 'endText':
            return 'bloc2', 'introText', 'text'
        
    if expProgress == 'bloc2':
        
        if blocProgress == 'introText':
            return 'bloc2', 'initialFix', 'fixation'
            
        if blocProgress == 'initialFix':
            return 'bloc2', 'video', 'video'
            
        if blocProgress == 'video':
            return 'bloc2', 'endFix', 'fixation'
            
        if blocProgress == 'endFix':
            return 'bloc2', 'ratingArousal', 'rating'
            
        #Rating
        if blocProgress == 'ratingArousal':
            return 'bloc2', 'ratingPleasant', 'rating'
            
        if blocProgress == 'ratingPleasant':
            return 'bloc2', 'ratingFunny', 'rating'
            
        if blocProgress == 'ratingFunny':
            if not ListBloc['2']:
                    return 'bloc2', 'endText', 'text'
            else:
                return 'bloc2', 'initialFix', 'fixation'
        
        if blocProgress == 'endText':
            return 'bloc3', 'introText', 'text'
        
    if expProgress == 'bloc3':
        
        if blocProgress == 'introText':
            return 'bloc3', 'initialFix', 'fixation'
            
        if blocProgress == 'initialFix':
            return 'bloc3', 'video', 'video'
            
        if blocProgress == 'video':
            return 'bloc3', 'endFix', 'fixation'
            
        if blocProgress == 'endFix':
            return 'bloc3', 'ratingArousal', 'rating'
            
        #Rating
        if blocProgress == 'ratingArousal':
            return 'bloc3', 'ratingPleasant', 'rating'
            
        if blocProgress == 'ratingPleasant':
            return 'bloc3', 'ratingFunny', 'rating'
            
        if blocProgress == 'ratingFunny':
            if not ListBloc['3']:
                    return 'bloc3', 'endText', 'text'
            else:
                return 'bloc3', 'initialFix', 'fixation'
        
        if blocProgress == 'endText':
            return 'emotionPost', 'introText', 'text'
        
    if expProgress == 'emotionPost':
        
        if blocProgress == 'introText':
            return 'emotionPost', 'rating', 'rating'
        
        if blocProgress == 'rating':
            if not ListEmotion['post']:
                return 'ending', 'introText', 'text'
            else:
                return 'emotionPost', 'rating', 'rating'

    if expProgress == 'ending':
        return 'ending', 'endText', 'text'

# Update the stimuli shown 

def updateStimuli(win, expProgress, blocProgress, ListBloc, ListEmotion, trialData, trialID, index, frameID):
    
    if expProgress == 'blocP' or expProgress == 'bloc1' or expProgress == 'bloc2' or expProgress == 'bloc3':
        
        # Setting
        if expProgress == 'blocP':
            introText = ("Nous allons maintenant débuter le bloc de pratique afin de vous familiariser avec le processus d’évaluation."
                    "\n\nVous verrez une croix de fixation suivi d’une vidéo et puis une croix de fixation de nouveau."
                    "Vous aurez ensuite à évaluer à quel point la vidéo est drôle sur une échelle allant de pas drôle’ à ‘très drôle’.\n\n"
                    "Appuyez sur une touche lorsque vous êtes prêt à commencer le bloc de pratique")
                    
            endText = "Le bloc de pratique est maintenant terminé. Nous allons débuter l'expérience.\n\nAppuyez sur une touche lorsque vous êtes prêt à commencer"
                    
            bloc = 'blocTest'
            blocID = 0
            
        elif expProgress == 'bloc1':
            introText= ("BLOC 1\n\nNous allons début le visionnement des vidéos. Vous aurez à regarder plusieurs extraits vidéos puis évaluer"
            "à quel point chaque vidéo était drôle.\n\nAppuyez sur une touche lorsque vous êtes prêt à commencer")
            endText = ("Fin du BLOC 1\n\nVous venez de compléter le premier bloc. Vous pouvez prendre une courte pause\n\n"
            "Appuyer sur une touche lorsque vous êtes prêt à recommencer")
            bloc = '1'
            blocID = '1'
            
        elif expProgress == 'bloc2':
            introText = ("BLOC 2\n\nNous allons débuter le visionnement des vidéos du deuxième bloc. Vous aurez à regarder de nouveau plusieurs extraits vidéos "
            "puis évaluer à quel point chaque vidéo était drôle. \n\nAppuyez sur une touche lorsque vous êtes prêt à commencer")
            endText = ("Fin du BLOC 2\n\nVous venez de compléter le deuxième bloc. Vous pouvez prendre une courte pause"
            "\n\nAppuyer sur une touche lorsque vous êtes prêt à recommencer")
            bloc = '2'
            blocID = '2'
            
        elif expProgress == 'bloc3':
            introText = ("BLOC 3\n\nNous allons débuter le visionnement des vidéos du troisème bloc. Vous aurez à regarder de nouveau plusieurs "
            "extraits vidéos puis évaluer à quel point chaque vidéo était drôle. \n\nAppuyez sur une touche lorsque vous êtes prêt à commencer")
            endText = ("Fin du BLOC 3\n\nAppuyez sur une touche lorsque vous êtes prêt à répondre au dernier questionnaire")
            bloc = '3'
            blocID = '3'


        #Start
        if blocProgress == 'introText':
            trialID=1
            return [textScreen(win,introText, 0.1)], None, None, index, trialID

        if blocProgress == 'initialFix':
            # Create New Stimuli
            stimuli = []
            stimuli.append(fixation(win))
            
            duration = random.choice([1, 1.5])
            
            # Save Data
            trialData['DURATION_PreFix']=duration
            trialData['TIME_StartPreFix'] = time.time()
            trialData['FRAME_StartPreFix'] = frameID
            
            return stimuli, time.time(), duration, index, trialID
            
        if blocProgress == 'video':
            stimuli = []
            stimuli.append(movieStimuli(win, ListBloc[bloc][0]))
            
            #Save Data 
            trialData['index']=index
            index+=1
            trialData['TrialID']=trialID
            trialID=+1
            trialData['BlocID']=blocID
            trialData['VideoName']=ListBloc[bloc][0]
            trialData['VideoType']=ListBloc[bloc][0][0]
            trialData['TIME_StartVideo']=time.time()
            trialData['FRAME_Startvideo']=frameID
            
           
            return stimuli, None, None, index, trialID
            
        if blocProgress == 'endFix':
            # Create New Stimuli
            stimuli = []
            stimuli.append(fixation(win))
            duration = random.choice([1, 1.5])
            
            #Save Data
            trialData['TIME_EndFix'] = time.time()
            trialData['FRAME_StartEndFix'] = frameID
            trialData['DURATION_StartEndFix']=duration
            
            
            return stimuli, time.time(), duration, index, trialID
        
        if blocProgress == 'ratingArousal':
            
            # Create new stimuli
            title, image, ratingScale = ratingStimuli2(win, "Quel est votre niveau d'éveil, c.a.d l'état d'excitation qu'à provoqué cette vidéo chez vous\n", "scale_arousal.png", ['Très calme,\ndétendu', "Très excité,\nstimulé"] )
            stimuli = [title, image, ratingScale]
            
            # Save Data
            trialData['TIME_startRatingArousal']=time.time()
            trialData['FRAME_startRatingArousal']=frameID

            return stimuli, None, None, index, trialID
        
        if blocProgress == 'ratingPleasant':
            # Create new stimuli
            title, image, ratingScale = ratingStimuli2(win, "Quel est votre niveau de plaisir, c.a.d. l'état émotionnel évoqué par la vidéo\n", "scale_pleasantness.png", ["Très\ndésagréable", "Très\n agréable"])
            stimuli = [title, image, ratingScale]
            
            # Save Data
            trialData['TIME_startRatingPleasant']=time.time()
            trialData['FRAME_startRatingPleasant']=frameID

            return stimuli, None, None, index, trialID
        
        if blocProgress== 'ratingFunny':
            # Create new stimuli
            title, image, ratingScale = ratingStimuli(win, "À quel point la vidéo était-elle drôle?", "greenRedScale.png", ['Pas drôle', "Très drôle"] )
            stimuli = [title, image, ratingScale]
            
            # Save Data
            trialData['TIME_startRatingFunny']=time.time()
            trialData['FRAME_startRatingFunny']=frameID

            return stimuli, None, None, index, trialID
            
            

        if blocProgress == 'endText':
            return [textScreen(win,endText)], None, None, index, trialID
            
    
    if expProgress == 'emotionPre':
        if blocProgress == 'introText':
            text=("Les questions suivantes contiennent des adjectifs qui décrivent des sentiments et des émotions."
                    "Lisez chacun de ces adjectifs. Pour chacun de ces adjectifs, vous devez indiquer à quel point il décrit comment vous vous sentez présentement."
                    "Pour ce faire, vous devez utiliser les choix de réponses suivant:\n\n1) Très peu ou pas du tout \n2) Peu \n3) Modérément \n4) Beaucoup \n5) Énormément"
                    "\n\nN’oubliez pas, il n’y a pas de bonnes ou de mauvaises réponses.Nous voulons savoir comment VOUS vous sentez présentement."
                    "\n\nAppuyez sur une touche lorsque vous êtes prêt à commencer")
            return [textScreen(win,text, 0.09)], None, None, index, trialID
        
        if blocProgress == 'rating':
            ratingScale, title, emotionShow, EmoEnglish = ratingEmotion(win, ListEmotion['pre'][0])
            stimuli = [title, emotionShow, ratingScale]
            stim = ListEmotion['pre'][0]
            
            return stimuli, None, None, index, trialID
        
    
    if expProgress == 'emotionPost':
        if blocProgress == 'introText':
            text=("Les questions suivantes contiennent des adjectifs qui décrivent des sentiments et des émotions."
                    "Lisez chacun de ces adjectifs. Pour chacun de ces adjectifs, vous devez indiquer à quel point il décrit comment vous vous sentez présentement."
                    "Pour ce faire, vous devez utiliser les choix de réponses suivant:\n\n1) Très peu ou pas du tout \n2) Peu \n3) Modérément \n4) Beaucoup \n5) Énormément"
                    "\n\nN’oubliez pas, il n’y a pas de bonnes ou de mauvaises réponses.Nous voulons savoir comment VOUS vous sentez présentement."
                    "\n\nAppuyez sur une touche lorsque vous êtes prêt à commencer")
            return [textScreen(win,text, 0.09)], None, None, index, trialID
        
        if blocProgress == 'rating':
            ratingScale, title, emotionShow, EmoEnglish = ratingEmotion(win, ListEmotion['post'][0])
            stimuli = [title, emotionShow, ratingScale]
            stim = ListEmotion['post'][0]
            
            return stimuli, None, None, index, trialID
        
    
    if expProgress == 'ending':
        if blocProgress == 'introText':
            text=("L'expérience est maintenant terminé. Merci de votre participation")
            return [textScreen(win,text, 0.09)], None, None , index, trialID
        else:
            return None, None, None, index, trialID
    

def updateRating(expProgress, trialData,globalData, activeStims, frameID, ListEmotion, ListBloc, blocProgress):
    if expProgress == 'blocP' or expProgress == 'bloc1' or expProgress == 'bloc2' or expProgress == 'bloc3':
        
        if blocProgress == 'ratingArousal': 
            trialData['TIME_EndRatingArousal']=time.time()
            trialData['FRAME_EndRatingArousal']=frameID
            trialData['ratingArousal'] = activeStims[2].getRating()
        
        elif blocProgress == 'ratingPleasant':
            trialData['TIME_EndRatingPleasant']=time.time()
            trialData['FRAME_EndRatingPleasant']=frameID
            trialData['ratingPleasant'] = activeStims[2].getRating()
            
        elif blocProgress == 'ratingFunny':
            trialData['TIME_EndRatingFunny']=time.time()
            trialData['FRAME_EndRatingFunny']=frameID
            trialData['ratingFunny'] = activeStims[2].getRating()
        
            if expProgress == 'blocP':
                ListBloc['blocTest'].pop(0)
            
            elif expProgress == 'bloc1':
                ListBloc['1'].pop(0)
                
            elif expProgress == 'bloc2':
                ListBloc['2'].pop(0)
                
            elif expProgress == 'bloc3':
                ListBloc['3'].pop(0)
       
        
    if expProgress == 'emotionPre':
        emotion=ListEmotion['pre'][0]
        EmoFrench, EmoEnglish = emotion.split('!')
        
        globalData['pre'+EmoEnglish] = changeRating(activeStims[2].getRating())
        ListEmotion['pre'].pop(0)
        
    if expProgress == 'emotionPost':
        emotion=ListEmotion['post'][0]
        EmoFrench, EmoEnglish = emotion.split('!')
        
        globalData['post'+EmoEnglish] = changeRating(activeStims[2].getRating())
        ListEmotion['post'].pop(0)
        

    
    
    
    
    
    
