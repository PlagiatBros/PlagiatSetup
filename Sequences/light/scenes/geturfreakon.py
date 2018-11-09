#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

import random

from ports import *

def sm_blinkinterns(seq, timer):
    i = random.randint(0,1)
    rpis=[rpijardinport,rpicourport]
    seq.send(rpis[i], '/pyta/text', 3, '(still looking for interns)')
    seq.send(rpis[i], '/pyta/text/strobe', 3, 1)
    seq.send(rpis[i], '/pyta/text/position_y', 3, -100)
    seq.send(rpis[i], '/pyta/text/visible', 3, 1)
    timer.wait(0.6, 's')
    seq.send(rpis[i], '/pyta/text/visible', 3, 0)
