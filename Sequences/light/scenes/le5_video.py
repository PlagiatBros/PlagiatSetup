#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from video_functions import *
from random import random, shuffle


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



_niglou = ['Niglou', 'Niggah', 'Nigrid', 'iNgrid', 'Nigroo', 'Nicole'] * 5
_niglou_text = '\ndon\'t you know it ain\'t\n\
no heavy duty too heavy\n\
for Mi$$y $chneck One-Two?'
shuffle(_niglou)

def le5_niglou(seq, timer):
    for n in _niglou:
        write(seq, timer, text=n + _niglou_text, dur=random(), align=['c', 'b'], pos=[0, 0.1])
    write(seq, timer, text='Niggah' + _niglou_text, dur=0, align=['c', 'b'], pos=[0, 0.1])


_words = ['DO YOU', 'USE', 'KREWZ', 'KNTRL?']
_i = 0
def le5_trapcup(seq, timer):
    global _i
    seq.send('/pyta/slide/white/reset')
    seq.send('/pyta/slide/white/set', 'visible', 1)
    seq.send('/pyta/slide/white/strobe', 'color', 1,1,1, 0,0,0, 0.08, 0.5)
    seq.send('/pyta/slide/white/set', 'position_z', -10)
    seq.send('/pyta/text/0/reset')
    seq.send('/pyta/text/0/set', 'visible', 1)
    seq.send('/pyta/text/0/strobe', 'color', 0,0,0, 1,1,1, 0.08, 0.5)
    seq.send('/pyta/text/0/set', 'text', _words[_i%len(_words)])
    _i += 1
    timer.wait(0.75, 'b')
    seq.send('/pyta/slide/white/set', 'visible', 0)
    seq.send('/pyta/text/0/set', 'visible', 0)
