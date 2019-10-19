#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from video_functions import *


def le5_intro(seq, timer):
    write(seq, timer, 0, 'RESPECTE\nPOUISSANCE', 0, 0)
    write(seq, timer, 1, 'LAAA\nPAPAAL', 0, 0)
    seq.send('/pyta/text/0/set', 'size', 0.3)
    seq.send('/pyta/text/0/animate', 'alpha', 0, 0.6, 10)

def le5_couplet1(seq, timer, level=1):
    if level == 1:
        seq.send('/pyta/slide/illuminati2/set', 'alpha', 0.2)
    elif level == 2:
        seq.send('/pyta/slide/illuminati2/set', 'alpha', 0.25)
    elif level == 3:
        seq.send('/pyta/post_process/reset')
        seq.send('/pyta/post_process/set', 'visible', 1)
        t = 60./seq.bpm*15*5
        seq.send('/pyta/slide/illuminati2/animate', 'alpha', 0.25, 0.9, t, 'exponentialin')
        seq.send('/pyta/slide/christcross_1/animate', 'alpha', 0.25, 0.75)
        seq.send('/pyta/slide/christcross_1/animate', 'noise', 0, -20, 'exponentialin')
        timer.wait(t, 's')
        seq.send('/pyta/slide/illuminati/set', 'gif_speed', 3)
        seq.send('/pyta/post_process/set', 'invert', 1)
