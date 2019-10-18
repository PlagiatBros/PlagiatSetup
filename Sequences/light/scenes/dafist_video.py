#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint


_look_txt= ["Look", "LOOK", "L00K", "lOoK", "LoOk", "LooK", "l00k", "k00l"]
def dafist_look(seq, timer):
    seq.send('/pyta/text/*/reset')
    ti = str(randint(0,3))
    seq.send('/pyta/slide/white/set', 'noise', 0)
    seq.send('/pyta/text/'+ti+'/set', 'visible', 1)
    seq.send('/pyta/text/'+ti+'/set', 'text', _look_txt[randint(0, len(_look_txt) -1)], 0.2)
    timer.wait(0.04, 's')
    seq.send('/pyta/slide/white/set', 'noise', -50)
    timer.wait(1, 'beat')
    seq.send('/pyta/text/'+ti+'/set', 'visible', 0)
