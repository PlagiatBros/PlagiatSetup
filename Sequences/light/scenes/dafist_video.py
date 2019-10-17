#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint, choice


_look_txt= ("Look", "LOOK", "L00K", "lOoK", "LoOk", "LooK", "l00k", "k00l")
def dafist_look(seq, timer):
    for port in [rpicourport, rpijardinport]:
        x = str(choice([0,2]))
        seq.send(port, '/pyta/text/'+x+'/reset')
        seq.send(port, '/pyta/text/'+x+'/set', 'visible', 1)
        seq.send(port, '/pyta/text/'+x+'/set', 'text', _look_txt[randint(0, len(_look_txt)-1)])
    timer.wait(0.8, 'beat')
    seq.send('/pyta/text/{0,2}/set', 'visible', 0)
