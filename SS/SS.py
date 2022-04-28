#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue Mar 29 18:55:05 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
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
    originPath='/Users/rhythmjain/Desktop/GTStuff/2-1/GRA/PsychoPy/SS/SS.py',
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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Consent_Form"
Consent_FormClock = core.Clock()
consent_form_text = visual.TextStim(win=win, name='consent_form_text',
    text='***Salient structures Consent Form***\n\nPurpose:\n\nEthics: This study has been reviewed by the Georgia Tech Institutional Review Board, and has been identified as “Minimal risk research qualified for exemption status under 45 CFR 46 104d.2(iii). (Ethics ID # H19240).\n\nDuration: The survey should take approximately 30 minutes or less to complete. Your answers are extremely valuable to us and we thank you for participating in this survey.\n\nConfidentiality: The study data will be collected anonymously. Data obtained though this survey will only be connected to an anonymous identification number and will be securely stored on a password-protected and encrypted computer for a minimum of 5 years as per Georgia Tech policy. In any final published version of this research, the identity of survey participants will not be disclosed. Study records will be kept confidential to the extent required by law. To make sure that this research is being carried out in the proper way, the Georgia Institute of Technology IRB may review study records. The Office of Human Research Protections may also look at study records.\n\nCompensation & Rights: Your participation in this study is voluntary. There is no compensation for participating in this study. You may refuse or discontinue your voluntary participation in this research study at any time. However, only completed surveys will be included in our analysis. You do not waive any of your legal rights by agreeing to be in the study.\nContacts and Questions: For questions, concerns, or complaints about the study, you may contact the P.I., Dr. Claire Arthur at: claire.arthur[at]gatech.edu or by telephone 404-894-9110. If you have any questions about your rights as a research subject, you may contact Ms. Melanie Clark, Georgia Institute of Technology at (404) 894-6942.\n\nBy pressing the space bar you are agreeing to participate. To leave the experiment at any point you can hit the escape button.\n\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
consent_resp = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='***Instructions (please read carefully!)***\n\nIn this experiment, you will listen to a series of short musical excerpts each less than one minute. You will click the button marked “start excerpt” to begin playing each excerpt. Once the music starts playing, you should listen attentively, paying careful attention to the changing chords (or harmony) in the song. There are lots of parts in music: the melody (the part you would sing along to), the rhythm or beat (the part you might tap your foot to), and the chords (I.e., the accompaniment/harmony, or, the remaining parts and instruments that sound together simultaneously in a harmonious way). This experiment will focus on chords.\nPress any key to continue.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "Participant_Info"
Participant_InfoClock = core.Clock()
win.allowStencil = True
information_form = visual.Form(win=win, name='information_form',
    items='csv_participant_information.xlsx',
    textHeight=0.03,
    font='Arial',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1, 1),
    pos=(0, 0),
    itemPadding=0.05
)
submit_button = visual.ButtonStim(win, 
    text='Submit', font='Arvo',
    pos=(0,-0.5),
    letterHeight=0.03,
    size=None, borderWidth=0.0,
    fillColor='black', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-center',
    name='submit_button'
)
submit_button.buttonClock = core.Clock()

# Initialize components for Routine "blank"
blankClock = core.Clock()
fixation_message = visual.TextStim(win=win, name='fixation_message',
    text='Get ready for the next clip! ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Annotations"
AnnotationsClock = core.Clock()
track = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='track')
track.setVolume(1.0)

# Initialize components for Routine "Thank_You_Regular"
Thank_You_RegularClock = core.Clock()
debrief = visual.TextStim(win=win, name='debrief',
    text='***Thank you for your participating*** \n  \nA little bit about this expeirment: The purpose of this study is to better understand the structural features that contribute to the violation of musical expectations, and the impact they have on our emotional experience while listening.\n\nTo know more click here!',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Thank_You_Consent_No"
Thank_You_Consent_NoClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for your time. \n\n',
    font='Arial',
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
key = str(consent_resp.keys)
print(key)

if key.lower() == 'y':
    consent_yes_reps = 1
    consent_no_reps = 0
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
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_resp.keys = []
    instructions_resp.rt = []
    _instructions_resp_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [instructions_text, instructions_resp]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.tStart = t  # local t and not account for scr refresh
            instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            instructions_text.setAutoDraw(True)
        
        # *instructions_resp* updates
        waitOnFlip = False
        if instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_resp.frameNStart = frameN  # exact frame index
            instructions_resp.tStart = t  # local t and not account for scr refresh
            instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_resp, 'tStartRefresh')  # time at next scr refresh
            instructions_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructions_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructions_resp.status == STARTED and not waitOnFlip:
            theseKeys = instructions_resp.getKeys(keyList=None, waitRelease=False)
            _instructions_resp_allKeys.extend(theseKeys)
            if len(_instructions_resp_allKeys):
                instructions_resp.keys = _instructions_resp_allKeys[-1].name  # just the last key pressed
                instructions_resp.rt = _instructions_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    consent_yes.addData('instructions_text.started', instructions_text.tStartRefresh)
    consent_yes.addData('instructions_text.stopped', instructions_text.tStopRefresh)
    # check responses
    if instructions_resp.keys in ['', [], None]:  # No response was made
        instructions_resp.keys = None
    consent_yes.addData('instructions_resp.keys',instructions_resp.keys)
    if instructions_resp.keys != None:  # we had a response
        consent_yes.addData('instructions_resp.rt', instructions_resp.rt)
    consent_yes.addData('instructions_resp.started', instructions_resp.tStartRefresh)
    consent_yes.addData('instructions_resp.stopped', instructions_resp.tStopRefresh)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Participant_Info"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    Participant_InfoComponents = [information_form, submit_button]
    for thisComponent in Participant_InfoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Participant_InfoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Participant_Info"-------
    while continueRoutine:
        # get current time
        t = Participant_InfoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Participant_InfoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *information_form* updates
        if information_form.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            information_form.frameNStart = frameN  # exact frame index
            information_form.tStart = t  # local t and not account for scr refresh
            information_form.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(information_form, 'tStartRefresh')  # time at next scr refresh
            information_form.setAutoDraw(True)
        
        # *submit_button* updates
        if submit_button.status == NOT_STARTED and information_form.complete==True:
            # keep track of start time/frame for later
            submit_button.frameNStart = frameN  # exact frame index
            submit_button.tStart = t  # local t and not account for scr refresh
            submit_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submit_button, 'tStartRefresh')  # time at next scr refresh
            submit_button.setAutoDraw(True)
        if submit_button.status == STARTED:
            # check whether submit_button has been pressed
            if submit_button.isClicked:
                if not submit_button.wasClicked:
                    submit_button.timesOn.append(submit_button.buttonClock.getTime()) # store time of first click
                    submit_button.timesOff.append(submit_button.buttonClock.getTime()) # store time clicked until
                else:
                    submit_button.timesOff[-1] = submit_button.buttonClock.getTime() # update time clicked until
                if not submit_button.wasClicked:
                    continueRoutine = False  # end routine when submit_button is clicked
                    None
                submit_button.wasClicked = True  # if submit_button is still clicked next frame, it is not a new click
            else:
                submit_button.wasClicked = False  # if submit_button is clicked next frame, it is a new click
        else:
            submit_button.wasClicked = False  # if submit_button is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Participant_InfoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Participant_Info"-------
    for thisComponent in Participant_InfoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    information_form.addDataToExp(thisExp, 'columns')
    information_form.autodraw = False
    consent_yes.addData('submit_button.started', submit_button.tStartRefresh)
    consent_yes.addData('submit_button.stopped', submit_button.tStopRefresh)
    consent_yes.addData('submit_button.numClicks', submit_button.numClicks)
    if submit_button.numClicks:
       consent_yes.addData('submit_button.timesOn', submit_button.timesOn)
       consent_yes.addData('submit_button.timesOff', submit_button.timesOff)
    else:
       consent_yes.addData('submit_button.timesOn', "")
       consent_yes.addData('submit_button.timesOff', "")
    # the Routine "Participant_Info" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    annotationLoops = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tracks.xlsx'),
        seed=None, name='annotationLoops')
    thisExp.addLoop(annotationLoops)  # add the loop to the experiment
    thisAnnotationLoop = annotationLoops.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAnnotationLoop.rgb)
    if thisAnnotationLoop != None:
        for paramName in thisAnnotationLoop:
            exec('{} = thisAnnotationLoop[paramName]'.format(paramName))
    
    for thisAnnotationLoop in annotationLoops:
        currentLoop = annotationLoops
        # abbreviate parameter names if possible (e.g. rgb = thisAnnotationLoop.rgb)
        if thisAnnotationLoop != None:
            for paramName in thisAnnotationLoop:
                exec('{} = thisAnnotationLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "blank"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blankComponents = [fixation_message]
        for thisComponent in blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_message* updates
            if fixation_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_message.frameNStart = frameN  # exact frame index
                fixation_message.tStart = t  # local t and not account for scr refresh
                fixation_message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_message, 'tStartRefresh')  # time at next scr refresh
                fixation_message.setAutoDraw(True)
            if fixation_message.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_message.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_message.tStop = t  # not accounting for scr refresh
                    fixation_message.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_message, 'tStopRefresh')  # time at next scr refresh
                    fixation_message.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blank"-------
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        annotationLoops.addData('fixation_message.started', fixation_message.tStartRefresh)
        annotationLoops.addData('fixation_message.stopped', fixation_message.tStopRefresh)
        
        # ------Prepare to start Routine "Annotations"-------
        continueRoutine = True
        # update component parameters for each repeat
        track.setSound(stimuli, hamming=True)
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
        annotationLoops.addData('track.started', track.tStartRefresh)
        annotationLoops.addData('track.stopped', track.tStopRefresh)
        # the Routine "Annotations" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'annotationLoops'
    
    
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
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()