#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from video_functions import *

def no_budget(seq, timer):
    write(seq, timer, 1, text='Faute de budget', glitch=360, dur=0)
    write(seq, timer, 0, text='Panne de budgé', glitch=360, dur=0)
