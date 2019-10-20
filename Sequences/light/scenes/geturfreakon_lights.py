#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from scene_functions import *

def slowmotium_main(seq,timer):
    crepitement(seq, timer, [['TuttiLointain','Red', '{4,5}', 230, 255], ['TuttiLointain', 'Blue', '{4,5}', 190, 210], ['TuttiProche', 'Red', '{1,2,3}', 230, 255], ['TuttiProche', 'Blue', '{1,2,3}', 150, 175],['TuttiProche', 'Green', '{1,2,3}', 100, 107]])

