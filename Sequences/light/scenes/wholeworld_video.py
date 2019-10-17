#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

from random import shuffle


# Intro

def intro_respect(sequencer, timer):

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/scene_recall', 'wholeworld_intro_respect')

def wholeworld_couplet_synth_fade(sequencer, timer):

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/slide/eyes_2/animate', 'alpha', 0.1, 0.5, 20)
