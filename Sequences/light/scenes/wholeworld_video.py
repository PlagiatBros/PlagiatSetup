#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

from random import normalvariate

def wholeworld_intro_respect(seq, timer):
    seq.send('/pyta/scene_recall', 'wholeworld_intro_respect')
    seq.send(':/Lightseq/Scene/Play', 'wholeworld_intro')

def wholeworld_couplet_synth_fade(seq, timer):
    seq.send('/pyta/slide/eyes_2/animate', 'alpha', 0.1, 0.5, 20)

def wholeworld_boomboclaat_glitch(seq, timer):
    while True:
        deviation = normalvariate(0, 0.5)
        seq.send('/pyta/slide/pearlharbor/set', 'rgbwave', 0.6 if deviation > 0.8 else 0)
        timer.wait(0.01, 's')
