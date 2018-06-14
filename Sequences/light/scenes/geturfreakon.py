#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

import random

from ports import *

def sm_blinkinterns(seq, timer):
    i = randomint(0,1)
    rpis=[rpijardinport,rpicourport] 
    seq.send(rpis[i], '/pyta/text', 2, '[plaʒia] is still looking for interns')
    timer.wait(0.8, 's')
    seq.send(rpis[i], '/pyta/text', 2, '[plaʒia]                             ')
