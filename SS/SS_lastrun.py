#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on Mon May 16 09:47:30 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'SS'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/johnmcnamara/Documents/GitHub/SalientStructures/SS/SS_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Consent_Form"
Consent_FormClock = core.Clock()
consent_form_text = visual.TextStim(win=win, name='consent_form_text',
    text='***Salient Structures***\n\nConsent Form\n\nPurpose: You are being asked to be a volunteer in a research study. The purpose of this study is to better understand the structural features that contribute to the violation of musical expectations, and the impact they have on our emotional experience while listening.\n\n\nEthics: This study has been reviewed by the Georgia Tech Institutional Review Board, and has been identified as “Minimal risk research qualified for exemption status under 45 CFR 46 104d.2(iii). (Ethics ID # H19240).\n\nDuration: The survey should take approximately 30 minutes or less to complete. Your answers are extremely valuable to us and we thank you for participating in this survey.\n\nConfidentiality: The study data will be collected anonymously. Data obtained though this survey will only be connected to an anonymous identification number and will be securely stored on a password-protected and encrypted computer for a minimum of 5 years as per Georgia Tech policy. In any final published version of this research, the identity of survey participants will not be disclosed. Study records will be kept confidential to the extent required by law. To make sure that this research is being carried out in the proper way, the Georgia Institute of Technology IRB may review study records. The Office of Human Research Protections may also look at study records.\n\nCompensation & Rights: Your participation in this study is voluntary. There is no compensation for participating in this study. You may refuse or discontinue your voluntary participation in this research study at any time. However, only completed surveys will be included in our analysis. You do not waive any of your legal rights by agreeing to be in the study.\nContacts and Questions: For questions, concerns, or complaints about the study, you may contact the P.I., Dr. Claire Arthur at: claire.arthur[at]gatech.edu or by telephone 404-894-9110. If you have any questions about your rights as a research subject, you may contact Ms. Melanie Clark, Georgia Institute of Technology at (404) 894-6942.\n\nPress ‘y’ if you wish to participate.\nPress ’n’ if you do not wish to participate.\n\nNote: To leave the experiment at any point you can hit the escape button twice.\n\n',
    font='Arial',
    pos=(0, 0.05), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
consent_resp = keyboard.Keyboard()

# Initialize components for Routine "get_songs"
get_songsClock = core.Clock()
with open("number.txt", "r") as f:
    old_num = f.readlines()
    f.close()

pg = int(old_num[0])
new_num = pg + 1

with open("number.txt", "w") as f:
    f.write(str(new_num))
    f.close()

pg = int(old_num[0])

def getVG(num):
    return (2*(num//10) + (num % 2))

def getAG(num):
    return num+1 if num%2==0 else num-1

vg = getVG(pg)
ag = getAG(vg)

def get_row_start(gnum):
    return gnum*5
def get_row_end(gnum, length):
    return gnum*5+length
    
vg_start = get_row_start(vg)
vg_end = get_row_end(vg, 5)
vg_slice = slice(vg_start, vg_end)
ag_start = get_row_start(ag)
ag_end = get_row_end(ag, 5)
ag_slice = slice(ag_start, ag_end)

# Initialize components for Routine "Valence_Instructions"
Valence_InstructionsClock = core.Clock()
valence_instructions_text = visual.TextStim(win=win, name='valence_instructions_text',
    text='***Instructions (please read carefully!)***\n\nIn this experiment, you will listen to a series of short musical excerpts each less than one minute. You will click the button marked “start excerpt” to begin playing each excerpt. Once the music starts playing, you should listen attentively, paying careful attention to the changing chords (or harmony) in the song. There are lots of parts in music: the melody (the part you would sing along to), the rhythm or beat (the part you might tap your foot to), and the chords (I.e., the accompaniment/harmony, or, the remaining parts and instruments that sound together simultaneously in a harmonious way). This experiment will focus on chords.\n\nPress any key to continue.',
    font='Arial',
    pos=(0, 0.05), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
valence_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "Valence_Prompt"
Valence_PromptClock = core.Clock()
Valence_Fixation_Message = visual.TextStim(win=win, name='Valence_Fixation_Message',
    text='Get ready for the clip!\n\nYou will be rating the music based on how happy/pleasant you believe it sounds.\n\nUse the slider to indicate how happy/pleasant you think the music is throughout the course of the song.\n\nPress any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
valence_next = keyboard.Keyboard()

# Initialize components for Routine "Annotations"
AnnotationsClock = core.Clock()
track = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='track')
track.setVolume(1.0)

# Initialize components for Routine "Annotation_Instructions"
Annotation_InstructionsClock = core.Clock()
annotations_instructions_text = visual.TextStim(win=win, name='annotations_instructions_text',
    text='***Instructions (please read carefully!)***\n\nIn this experiment, you will listen to a series of short musical excerpts each less than one minute. You will click the button marked “start excerpt” to begin playing each excerpt. Once the music starts playing, you should listen attentively, paying careful attention to the changing chords (or harmony) in the song. There are lots of parts in music: the melody (the part you would sing along to), the rhythm or beat (the part you might tap your foot to), and the chords (I.e., the accompaniment/harmony, or, the remaining parts and instruments that sound together simultaneously in a harmonious way). This experiment will focus on chords.\n\nPress any key to continue.',
    font='Arial',
    pos=(0, 0.05), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
annotations_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "Arousal_Prompt"
Arousal_PromptClock = core.Clock()
Arousal_Fixation_Message = visual.TextStim(win=win, name='Arousal_Fixation_Message',
    text='Get ready for the clip!\n\nYou will be rating the music based on how much energy you believe it has.\n\nUse the slider to indicate how energetic you think the music is throughout the course of the song.\n\nPress any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
arousal_next = keyboard.Keyboard()

# Initialize components for Routine "Annotations"
AnnotationsClock = core.Clock()
track = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='track')
track.setVolume(1.0)

# Initialize components for Routine "Valence_Instructions"
Valence_InstructionsClock = core.Clock()
valence_instructions_text = visual.TextStim(win=win, name='valence_instructions_text',
    text='***Instructions (please read carefully!)***\n\nIn this experiment, you will listen to a series of short musical excerpts each less than one minute. You will click the button marked “start excerpt” to begin playing each excerpt. Once the music starts playing, you should listen attentively, paying careful attention to the changing chords (or harmony) in the song. There are lots of parts in music: the melody (the part you would sing along to), the rhythm or beat (the part you might tap your foot to), and the chords (I.e., the accompaniment/harmony, or, the remaining parts and instruments that sound together simultaneously in a harmonious way). This experiment will focus on chords.\n\nPress any key to continue.',
    font='Arial',
    pos=(0, 0.05), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
valence_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "Valence_Prompt"
Valence_PromptClock = core.Clock()
Valence_Fixation_Message = visual.TextStim(win=win, name='Valence_Fixation_Message',
    text='Get ready for the clip!\n\nYou will be rating the music based on how happy/pleasant you believe it sounds.\n\nUse the slider to indicate how happy/pleasant you think the music is throughout the course of the song.\n\nPress any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
valence_next = keyboard.Keyboard()

# Initialize components for Routine "Annotations"
AnnotationsClock = core.Clock()
track = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='track')
track.setVolume(1.0)

# Initialize components for Routine "Thank_You_Regular"
Thank_You_RegularClock = core.Clock()
debrief = visual.TextStim(win=win, name='debrief',
    text='***Thank you for your participating*** \n  \nA little bit about this expeirment: The purpose of this study is to better understand the structural features that contribute to the violation of musical expectations, and the impact they have on our emotional experience while listening.\n\nTo know more click here!',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Thank_You_Consent_No"
Thank_You_Consent_NoClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for your time. \n\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Consent_Form"-------
continueRoutine = True
# update component parameters for each repeat
consent_resp.keys = []
consent_resp.rt = []
_consent_resp_allKeys = []
# keep track of which components have finished
Consent_FormComponents = [consent_form_text, consent_resp]
for thisComponent in Consent_FormComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Consent_FormClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Consent_Form"-------
while continueRoutine:
    # get current time
    t = Consent_FormClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Consent_FormClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consent_form_text* updates
    if consent_form_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_form_text.frameNStart = frameN  # exact frame index
        consent_form_text.tStart = t  # local t and not account for scr refresh
        consent_form_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_form_text, 'tStartRefresh')  # time at next scr refresh
        consent_form_text.setAutoDraw(True)
    
    # *consent_resp* updates
    waitOnFlip = False
    if consent_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_resp.frameNStart = frameN  # exact frame index
        consent_resp.tStart = t  # local t and not account for scr refresh
        consent_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_resp, 'tStartRefresh')  # time at next scr refresh
        consent_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(consent_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(consent_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if consent_resp.status == STARTED and not waitOnFlip:
        theseKeys = consent_resp.getKeys(keyList=['y', 'Y', 'n', 'N'], waitRelease=False)
        _consent_resp_allKeys.extend(theseKeys)
        if len(_consent_resp_allKeys):
            consent_resp.keys = _consent_resp_allKeys[-1].name  # just the last key pressed
            consent_resp.rt = _consent_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Consent_FormComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Consent_Form"-------
for thisComponent in Consent_FormComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('consent_form_text.started', consent_form_text.tStartRefresh)
thisExp.addData('consent_form_text.stopped', consent_form_text.tStopRefresh)
# check responses
if consent_resp.keys in ['', [], None]:  # No response was made
    consent_resp.keys = None
thisExp.addData('consent_resp.keys',consent_resp.keys)
if consent_resp.keys != None:  # we had a response
    thisExp.addData('consent_resp.rt', consent_resp.rt)
thisExp.addData('consent_resp.started', consent_resp.tStartRefresh)
thisExp.addData('consent_resp.stopped', consent_resp.tStopRefresh)
thisExp.nextEntry()
import random

key = str(consent_resp.keys)
print(key)

if key.lower() == 'y':
    consent_yes_reps = 1
    consent_no_reps = 0
    valence_first = random.randint(0,1)
    valence_second = -1*valence_first + 1
elif key.lower() == 'n':
    consent_yes_reps = 0
    consent_no_reps = 1
# the Routine "Consent_Form" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
consent_yes = data.TrialHandler(nReps=consent_yes_reps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='consent_yes')
thisExp.addLoop(consent_yes)  # add the loop to the experiment
thisConsent_ye = consent_yes.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConsent_ye.rgb)
if thisConsent_ye != None:
    for paramName in thisConsent_ye:
        exec('{} = thisConsent_ye[paramName]'.format(paramName))

for thisConsent_ye in consent_yes:
    currentLoop = consent_yes
    # abbreviate parameter names if possible (e.g. rgb = thisConsent_ye.rgb)
    if thisConsent_ye != None:
        for paramName in thisConsent_ye:
            exec('{} = thisConsent_ye[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "get_songs"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    get_songsComponents = []
    for thisComponent in get_songsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    get_songsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "get_songs"-------
    while continueRoutine:
        # get current time
        t = get_songsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=get_songsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in get_songsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "get_songs"-------
    for thisComponent in get_songsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "get_songs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    is_valence_first = data.TrialHandler(nReps=valence_first, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='is_valence_first')
    thisExp.addLoop(is_valence_first)  # add the loop to the experiment
    thisIs_valence_first = is_valence_first.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIs_valence_first.rgb)
    if thisIs_valence_first != None:
        for paramName in thisIs_valence_first:
            exec('{} = thisIs_valence_first[paramName]'.format(paramName))
    
    for thisIs_valence_first in is_valence_first:
        currentLoop = is_valence_first
        # abbreviate parameter names if possible (e.g. rgb = thisIs_valence_first.rgb)
        if thisIs_valence_first != None:
            for paramName in thisIs_valence_first:
                exec('{} = thisIs_valence_first[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Valence_Instructions"-------
        continueRoutine = True
        # update component parameters for each repeat
        valence_instructions_resp.keys = []
        valence_instructions_resp.rt = []
        _valence_instructions_resp_allKeys = []
        # keep track of which components have finished
        Valence_InstructionsComponents = [valence_instructions_text, valence_instructions_resp]
        for thisComponent in Valence_InstructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Valence_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Valence_Instructions"-------
        while continueRoutine:
            # get current time
            t = Valence_InstructionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Valence_InstructionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *valence_instructions_text* updates
            if valence_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                valence_instructions_text.frameNStart = frameN  # exact frame index
                valence_instructions_text.tStart = t  # local t and not account for scr refresh
                valence_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(valence_instructions_text, 'tStartRefresh')  # time at next scr refresh
                valence_instructions_text.setAutoDraw(True)
            
            # *valence_instructions_resp* updates
            waitOnFlip = False
            if valence_instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                valence_instructions_resp.frameNStart = frameN  # exact frame index
                valence_instructions_resp.tStart = t  # local t and not account for scr refresh
                valence_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(valence_instructions_resp, 'tStartRefresh')  # time at next scr refresh
                valence_instructions_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(valence_instructions_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(valence_instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if valence_instructions_resp.status == STARTED and not waitOnFlip:
                theseKeys = valence_instructions_resp.getKeys(keyList=None, waitRelease=False)
                _valence_instructions_resp_allKeys.extend(theseKeys)
                if len(_valence_instructions_resp_allKeys):
                    valence_instructions_resp.keys = _valence_instructions_resp_allKeys[-1].name  # just the last key pressed
                    valence_instructions_resp.rt = _valence_instructions_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Valence_InstructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Valence_Instructions"-------
        for thisComponent in Valence_InstructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        is_valence_first.addData('valence_instructions_text.started', valence_instructions_text.tStartRefresh)
        is_valence_first.addData('valence_instructions_text.stopped', valence_instructions_text.tStopRefresh)
        # check responses
        if valence_instructions_resp.keys in ['', [], None]:  # No response was made
            valence_instructions_resp.keys = None
        is_valence_first.addData('valence_instructions_resp.keys',valence_instructions_resp.keys)
        if valence_instructions_resp.keys != None:  # we had a response
            is_valence_first.addData('valence_instructions_resp.rt', valence_instructions_resp.rt)
        is_valence_first.addData('valence_instructions_resp.started', valence_instructions_resp.tStartRefresh)
        is_valence_first.addData('valence_instructions_resp.stopped', valence_instructions_resp.tStopRefresh)
        # the Routine "Valence_Instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        valenceAnnotationLoops = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('fixed_sample.xlsx', selection=vg_slice),
            seed=None, name='valenceAnnotationLoops')
        thisExp.addLoop(valenceAnnotationLoops)  # add the loop to the experiment
        thisValenceAnnotationLoop = valenceAnnotationLoops.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisValenceAnnotationLoop.rgb)
        if thisValenceAnnotationLoop != None:
            for paramName in thisValenceAnnotationLoop:
                exec('{} = thisValenceAnnotationLoop[paramName]'.format(paramName))
        
        for thisValenceAnnotationLoop in valenceAnnotationLoops:
            currentLoop = valenceAnnotationLoops
            # abbreviate parameter names if possible (e.g. rgb = thisValenceAnnotationLoop.rgb)
            if thisValenceAnnotationLoop != None:
                for paramName in thisValenceAnnotationLoop:
                    exec('{} = thisValenceAnnotationLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Valence_Prompt"-------
            continueRoutine = True
            # update component parameters for each repeat
            valence_next.keys = []
            valence_next.rt = []
            _valence_next_allKeys = []
            # keep track of which components have finished
            Valence_PromptComponents = [Valence_Fixation_Message, valence_next]
            for thisComponent in Valence_PromptComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Valence_PromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Valence_Prompt"-------
            while continueRoutine:
                # get current time
                t = Valence_PromptClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Valence_PromptClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Valence_Fixation_Message* updates
                if Valence_Fixation_Message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Valence_Fixation_Message.frameNStart = frameN  # exact frame index
                    Valence_Fixation_Message.tStart = t  # local t and not account for scr refresh
                    Valence_Fixation_Message.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Valence_Fixation_Message, 'tStartRefresh')  # time at next scr refresh
                    Valence_Fixation_Message.setAutoDraw(True)
                
                # *valence_next* updates
                waitOnFlip = False
                if valence_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    valence_next.frameNStart = frameN  # exact frame index
                    valence_next.tStart = t  # local t and not account for scr refresh
                    valence_next.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(valence_next, 'tStartRefresh')  # time at next scr refresh
                    valence_next.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(valence_next.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(valence_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if valence_next.status == STARTED and not waitOnFlip:
                    theseKeys = valence_next.getKeys(keyList=None, waitRelease=False)
                    _valence_next_allKeys.extend(theseKeys)
                    if len(_valence_next_allKeys):
                        valence_next.keys = _valence_next_allKeys[-1].name  # just the last key pressed
                        valence_next.rt = _valence_next_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Valence_PromptComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Valence_Prompt"-------
            for thisComponent in Valence_PromptComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            valenceAnnotationLoops.addData('Valence_Fixation_Message.started', Valence_Fixation_Message.tStartRefresh)
            valenceAnnotationLoops.addData('Valence_Fixation_Message.stopped', Valence_Fixation_Message.tStopRefresh)
            # check responses
            if valence_next.keys in ['', [], None]:  # No response was made
                valence_next.keys = None
            valenceAnnotationLoops.addData('valence_next.keys',valence_next.keys)
            if valence_next.keys != None:  # we had a response
                valenceAnnotationLoops.addData('valence_next.rt', valence_next.rt)
            valenceAnnotationLoops.addData('valence_next.started', valence_next.tStartRefresh)
            valenceAnnotationLoops.addData('valence_next.stopped', valence_next.tStopRefresh)
            # the Routine "Valence_Prompt" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Annotations"-------
            continueRoutine = True
            # update component parameters for each repeat
            track.setSound(WavFileName, hamming=True)
            track.setVolume(1.0, log=False)
            # keep track of which components have finished
            AnnotationsComponents = [track]
            for thisComponent in AnnotationsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AnnotationsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Annotations"-------
            while continueRoutine:
                # get current time
                t = AnnotationsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AnnotationsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop track
                if track.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    track.frameNStart = frameN  # exact frame index
                    track.tStart = t  # local t and not account for scr refresh
                    track.tStartRefresh = tThisFlipGlobal  # on global time
                    track.play(when=win)  # sync with win flip
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AnnotationsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Annotations"-------
            for thisComponent in AnnotationsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            track.stop()  # ensure sound has stopped at end of routine
            valenceAnnotationLoops.addData('track.started', track.tStartRefresh)
            valenceAnnotationLoops.addData('track.stopped', track.tStopRefresh)
            # the Routine "Annotations" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'valenceAnnotationLoops'
        
        thisExp.nextEntry()
        
    # completed valence_first repeats of 'is_valence_first'
    
    
    # ------Prepare to start Routine "Annotation_Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    annotations_instructions_resp.keys = []
    annotations_instructions_resp.rt = []
    _annotations_instructions_resp_allKeys = []
    # keep track of which components have finished
    Annotation_InstructionsComponents = [annotations_instructions_text, annotations_instructions_resp]
    for thisComponent in Annotation_InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Annotation_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Annotation_Instructions"-------
    while continueRoutine:
        # get current time
        t = Annotation_InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Annotation_InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *annotations_instructions_text* updates
        if annotations_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annotations_instructions_text.frameNStart = frameN  # exact frame index
            annotations_instructions_text.tStart = t  # local t and not account for scr refresh
            annotations_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annotations_instructions_text, 'tStartRefresh')  # time at next scr refresh
            annotations_instructions_text.setAutoDraw(True)
        
        # *annotations_instructions_resp* updates
        waitOnFlip = False
        if annotations_instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            annotations_instructions_resp.frameNStart = frameN  # exact frame index
            annotations_instructions_resp.tStart = t  # local t and not account for scr refresh
            annotations_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(annotations_instructions_resp, 'tStartRefresh')  # time at next scr refresh
            annotations_instructions_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(annotations_instructions_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(annotations_instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if annotations_instructions_resp.status == STARTED and not waitOnFlip:
            theseKeys = annotations_instructions_resp.getKeys(keyList=None, waitRelease=False)
            _annotations_instructions_resp_allKeys.extend(theseKeys)
            if len(_annotations_instructions_resp_allKeys):
                annotations_instructions_resp.keys = _annotations_instructions_resp_allKeys[-1].name  # just the last key pressed
                annotations_instructions_resp.rt = _annotations_instructions_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Annotation_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Annotation_Instructions"-------
    for thisComponent in Annotation_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_yes.addData('annotations_instructions_text.started', annotations_instructions_text.tStartRefresh)
    consent_yes.addData('annotations_instructions_text.stopped', annotations_instructions_text.tStopRefresh)
    # check responses
    if annotations_instructions_resp.keys in ['', [], None]:  # No response was made
        annotations_instructions_resp.keys = None
    consent_yes.addData('annotations_instructions_resp.keys',annotations_instructions_resp.keys)
    if annotations_instructions_resp.keys != None:  # we had a response
        consent_yes.addData('annotations_instructions_resp.rt', annotations_instructions_resp.rt)
    consent_yes.addData('annotations_instructions_resp.started', annotations_instructions_resp.tStartRefresh)
    consent_yes.addData('annotations_instructions_resp.stopped', annotations_instructions_resp.tStopRefresh)
    # the Routine "Annotation_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    arousalAnnotationLoops = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('fixed_sample.xlsx', selection=ag_slice),
        seed=None, name='arousalAnnotationLoops')
    thisExp.addLoop(arousalAnnotationLoops)  # add the loop to the experiment
    thisArousalAnnotationLoop = arousalAnnotationLoops.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisArousalAnnotationLoop.rgb)
    if thisArousalAnnotationLoop != None:
        for paramName in thisArousalAnnotationLoop:
            exec('{} = thisArousalAnnotationLoop[paramName]'.format(paramName))
    
    for thisArousalAnnotationLoop in arousalAnnotationLoops:
        currentLoop = arousalAnnotationLoops
        # abbreviate parameter names if possible (e.g. rgb = thisArousalAnnotationLoop.rgb)
        if thisArousalAnnotationLoop != None:
            for paramName in thisArousalAnnotationLoop:
                exec('{} = thisArousalAnnotationLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Arousal_Prompt"-------
        continueRoutine = True
        # update component parameters for each repeat
        arousal_next.keys = []
        arousal_next.rt = []
        _arousal_next_allKeys = []
        # keep track of which components have finished
        Arousal_PromptComponents = [Arousal_Fixation_Message, arousal_next]
        for thisComponent in Arousal_PromptComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Arousal_PromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Arousal_Prompt"-------
        while continueRoutine:
            # get current time
            t = Arousal_PromptClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Arousal_PromptClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Arousal_Fixation_Message* updates
            if Arousal_Fixation_Message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Arousal_Fixation_Message.frameNStart = frameN  # exact frame index
                Arousal_Fixation_Message.tStart = t  # local t and not account for scr refresh
                Arousal_Fixation_Message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Arousal_Fixation_Message, 'tStartRefresh')  # time at next scr refresh
                Arousal_Fixation_Message.setAutoDraw(True)
            
            # *arousal_next* updates
            waitOnFlip = False
            if arousal_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arousal_next.frameNStart = frameN  # exact frame index
                arousal_next.tStart = t  # local t and not account for scr refresh
                arousal_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousal_next, 'tStartRefresh')  # time at next scr refresh
                arousal_next.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(arousal_next.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(arousal_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if arousal_next.status == STARTED and not waitOnFlip:
                theseKeys = arousal_next.getKeys(keyList=None, waitRelease=False)
                _arousal_next_allKeys.extend(theseKeys)
                if len(_arousal_next_allKeys):
                    arousal_next.keys = _arousal_next_allKeys[-1].name  # just the last key pressed
                    arousal_next.rt = _arousal_next_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Arousal_PromptComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Arousal_Prompt"-------
        for thisComponent in Arousal_PromptComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        arousalAnnotationLoops.addData('Arousal_Fixation_Message.started', Arousal_Fixation_Message.tStartRefresh)
        arousalAnnotationLoops.addData('Arousal_Fixation_Message.stopped', Arousal_Fixation_Message.tStopRefresh)
        # check responses
        if arousal_next.keys in ['', [], None]:  # No response was made
            arousal_next.keys = None
        arousalAnnotationLoops.addData('arousal_next.keys',arousal_next.keys)
        if arousal_next.keys != None:  # we had a response
            arousalAnnotationLoops.addData('arousal_next.rt', arousal_next.rt)
        arousalAnnotationLoops.addData('arousal_next.started', arousal_next.tStartRefresh)
        arousalAnnotationLoops.addData('arousal_next.stopped', arousal_next.tStopRefresh)
        # the Routine "Arousal_Prompt" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Annotations"-------
        continueRoutine = True
        # update component parameters for each repeat
        track.setSound(WavFileName, hamming=True)
        track.setVolume(1.0, log=False)
        # keep track of which components have finished
        AnnotationsComponents = [track]
        for thisComponent in AnnotationsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AnnotationsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Annotations"-------
        while continueRoutine:
            # get current time
            t = AnnotationsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AnnotationsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop track
            if track.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                track.frameNStart = frameN  # exact frame index
                track.tStart = t  # local t and not account for scr refresh
                track.tStartRefresh = tThisFlipGlobal  # on global time
                track.play(when=win)  # sync with win flip
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AnnotationsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Annotations"-------
        for thisComponent in AnnotationsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        track.stop()  # ensure sound has stopped at end of routine
        arousalAnnotationLoops.addData('track.started', track.tStartRefresh)
        arousalAnnotationLoops.addData('track.stopped', track.tStopRefresh)
        # the Routine "Annotations" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'arousalAnnotationLoops'
    
    
    # set up handler to look after randomisation of conditions etc
    is_valence_second = data.TrialHandler(nReps=valence_second, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='is_valence_second')
    thisExp.addLoop(is_valence_second)  # add the loop to the experiment
    thisIs_valence_second = is_valence_second.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIs_valence_second.rgb)
    if thisIs_valence_second != None:
        for paramName in thisIs_valence_second:
            exec('{} = thisIs_valence_second[paramName]'.format(paramName))
    
    for thisIs_valence_second in is_valence_second:
        currentLoop = is_valence_second
        # abbreviate parameter names if possible (e.g. rgb = thisIs_valence_second.rgb)
        if thisIs_valence_second != None:
            for paramName in thisIs_valence_second:
                exec('{} = thisIs_valence_second[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Valence_Instructions"-------
        continueRoutine = True
        # update component parameters for each repeat
        valence_instructions_resp.keys = []
        valence_instructions_resp.rt = []
        _valence_instructions_resp_allKeys = []
        # keep track of which components have finished
        Valence_InstructionsComponents = [valence_instructions_text, valence_instructions_resp]
        for thisComponent in Valence_InstructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Valence_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Valence_Instructions"-------
        while continueRoutine:
            # get current time
            t = Valence_InstructionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Valence_InstructionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *valence_instructions_text* updates
            if valence_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                valence_instructions_text.frameNStart = frameN  # exact frame index
                valence_instructions_text.tStart = t  # local t and not account for scr refresh
                valence_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(valence_instructions_text, 'tStartRefresh')  # time at next scr refresh
                valence_instructions_text.setAutoDraw(True)
            
            # *valence_instructions_resp* updates
            waitOnFlip = False
            if valence_instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                valence_instructions_resp.frameNStart = frameN  # exact frame index
                valence_instructions_resp.tStart = t  # local t and not account for scr refresh
                valence_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(valence_instructions_resp, 'tStartRefresh')  # time at next scr refresh
                valence_instructions_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(valence_instructions_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(valence_instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if valence_instructions_resp.status == STARTED and not waitOnFlip:
                theseKeys = valence_instructions_resp.getKeys(keyList=None, waitRelease=False)
                _valence_instructions_resp_allKeys.extend(theseKeys)
                if len(_valence_instructions_resp_allKeys):
                    valence_instructions_resp.keys = _valence_instructions_resp_allKeys[-1].name  # just the last key pressed
                    valence_instructions_resp.rt = _valence_instructions_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Valence_InstructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Valence_Instructions"-------
        for thisComponent in Valence_InstructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        is_valence_second.addData('valence_instructions_text.started', valence_instructions_text.tStartRefresh)
        is_valence_second.addData('valence_instructions_text.stopped', valence_instructions_text.tStopRefresh)
        # check responses
        if valence_instructions_resp.keys in ['', [], None]:  # No response was made
            valence_instructions_resp.keys = None
        is_valence_second.addData('valence_instructions_resp.keys',valence_instructions_resp.keys)
        if valence_instructions_resp.keys != None:  # we had a response
            is_valence_second.addData('valence_instructions_resp.rt', valence_instructions_resp.rt)
        is_valence_second.addData('valence_instructions_resp.started', valence_instructions_resp.tStartRefresh)
        is_valence_second.addData('valence_instructions_resp.stopped', valence_instructions_resp.tStopRefresh)
        # the Routine "Valence_Instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        valenceAnnotationLoops2 = data.TrialHandler(nReps=5.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='valenceAnnotationLoops2')
        thisExp.addLoop(valenceAnnotationLoops2)  # add the loop to the experiment
        thisValenceAnnotationLoops2 = valenceAnnotationLoops2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisValenceAnnotationLoops2.rgb)
        if thisValenceAnnotationLoops2 != None:
            for paramName in thisValenceAnnotationLoops2:
                exec('{} = thisValenceAnnotationLoops2[paramName]'.format(paramName))
        
        for thisValenceAnnotationLoops2 in valenceAnnotationLoops2:
            currentLoop = valenceAnnotationLoops2
            # abbreviate parameter names if possible (e.g. rgb = thisValenceAnnotationLoops2.rgb)
            if thisValenceAnnotationLoops2 != None:
                for paramName in thisValenceAnnotationLoops2:
                    exec('{} = thisValenceAnnotationLoops2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Valence_Prompt"-------
            continueRoutine = True
            # update component parameters for each repeat
            valence_next.keys = []
            valence_next.rt = []
            _valence_next_allKeys = []
            # keep track of which components have finished
            Valence_PromptComponents = [Valence_Fixation_Message, valence_next]
            for thisComponent in Valence_PromptComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Valence_PromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Valence_Prompt"-------
            while continueRoutine:
                # get current time
                t = Valence_PromptClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Valence_PromptClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Valence_Fixation_Message* updates
                if Valence_Fixation_Message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Valence_Fixation_Message.frameNStart = frameN  # exact frame index
                    Valence_Fixation_Message.tStart = t  # local t and not account for scr refresh
                    Valence_Fixation_Message.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Valence_Fixation_Message, 'tStartRefresh')  # time at next scr refresh
                    Valence_Fixation_Message.setAutoDraw(True)
                
                # *valence_next* updates
                waitOnFlip = False
                if valence_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    valence_next.frameNStart = frameN  # exact frame index
                    valence_next.tStart = t  # local t and not account for scr refresh
                    valence_next.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(valence_next, 'tStartRefresh')  # time at next scr refresh
                    valence_next.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(valence_next.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(valence_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if valence_next.status == STARTED and not waitOnFlip:
                    theseKeys = valence_next.getKeys(keyList=None, waitRelease=False)
                    _valence_next_allKeys.extend(theseKeys)
                    if len(_valence_next_allKeys):
                        valence_next.keys = _valence_next_allKeys[-1].name  # just the last key pressed
                        valence_next.rt = _valence_next_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Valence_PromptComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Valence_Prompt"-------
            for thisComponent in Valence_PromptComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            valenceAnnotationLoops2.addData('Valence_Fixation_Message.started', Valence_Fixation_Message.tStartRefresh)
            valenceAnnotationLoops2.addData('Valence_Fixation_Message.stopped', Valence_Fixation_Message.tStopRefresh)
            # check responses
            if valence_next.keys in ['', [], None]:  # No response was made
                valence_next.keys = None
            valenceAnnotationLoops2.addData('valence_next.keys',valence_next.keys)
            if valence_next.keys != None:  # we had a response
                valenceAnnotationLoops2.addData('valence_next.rt', valence_next.rt)
            valenceAnnotationLoops2.addData('valence_next.started', valence_next.tStartRefresh)
            valenceAnnotationLoops2.addData('valence_next.stopped', valence_next.tStopRefresh)
            # the Routine "Valence_Prompt" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Annotations"-------
            continueRoutine = True
            # update component parameters for each repeat
            track.setSound(WavFileName, hamming=True)
            track.setVolume(1.0, log=False)
            # keep track of which components have finished
            AnnotationsComponents = [track]
            for thisComponent in AnnotationsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AnnotationsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Annotations"-------
            while continueRoutine:
                # get current time
                t = AnnotationsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AnnotationsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop track
                if track.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    track.frameNStart = frameN  # exact frame index
                    track.tStart = t  # local t and not account for scr refresh
                    track.tStartRefresh = tThisFlipGlobal  # on global time
                    track.play(when=win)  # sync with win flip
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AnnotationsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Annotations"-------
            for thisComponent in AnnotationsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            track.stop()  # ensure sound has stopped at end of routine
            valenceAnnotationLoops2.addData('track.started', track.tStartRefresh)
            valenceAnnotationLoops2.addData('track.stopped', track.tStopRefresh)
            # the Routine "Annotations" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 5.0 repeats of 'valenceAnnotationLoops2'
        
        thisExp.nextEntry()
        
    # completed valence_second repeats of 'is_valence_second'
    
    
    # ------Prepare to start Routine "Thank_You_Regular"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Thank_You_RegularComponents = [debrief]
    for thisComponent in Thank_You_RegularComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Thank_You_RegularClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Thank_You_Regular"-------
    while continueRoutine:
        # get current time
        t = Thank_You_RegularClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Thank_You_RegularClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *debrief* updates
        if debrief.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debrief.frameNStart = frameN  # exact frame index
            debrief.tStart = t  # local t and not account for scr refresh
            debrief.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debrief, 'tStartRefresh')  # time at next scr refresh
            debrief.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Thank_You_RegularComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Thank_You_Regular"-------
    for thisComponent in Thank_You_RegularComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_yes.addData('debrief.started', debrief.tStartRefresh)
    consent_yes.addData('debrief.stopped', debrief.tStopRefresh)
    # the Routine "Thank_You_Regular" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed consent_yes_reps repeats of 'consent_yes'


# set up handler to look after randomisation of conditions etc
consent_no = data.TrialHandler(nReps=consent_no_reps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='consent_no')
thisExp.addLoop(consent_no)  # add the loop to the experiment
thisConsent_no = consent_no.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConsent_no.rgb)
if thisConsent_no != None:
    for paramName in thisConsent_no:
        exec('{} = thisConsent_no[paramName]'.format(paramName))

for thisConsent_no in consent_no:
    currentLoop = consent_no
    # abbreviate parameter names if possible (e.g. rgb = thisConsent_no.rgb)
    if thisConsent_no != None:
        for paramName in thisConsent_no:
            exec('{} = thisConsent_no[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Thank_You_Consent_No"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Thank_You_Consent_NoComponents = [text]
    for thisComponent in Thank_You_Consent_NoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Thank_You_Consent_NoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Thank_You_Consent_No"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Thank_You_Consent_NoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Thank_You_Consent_NoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Thank_You_Consent_NoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Thank_You_Consent_No"-------
    for thisComponent in Thank_You_Consent_NoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_no.addData('text.started', text.tStartRefresh)
    consent_no.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed consent_no_reps repeats of 'consent_no'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
