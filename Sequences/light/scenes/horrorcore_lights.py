#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint

### ALIASES GENERAUX

def crepitement(seq, timer, bars, colors, segments, cmin, cmax):
    # bars, colors et segments suivant syntaxe OSC
    while True:
        seq.send(qlcport, '/'+bars+'/'+colors+'/Segment/'+segments, randint(cmin, cmax))
        timer.wait(0.01, 's')
        
###


def horrorcore_intro(seq, timer):
    seq.send(qlcport, '/TuttiProche/Green/Segment/[1-2]', 60)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[1-2]', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[7-8]', 255)

def horrorcore_couplet_stable(seq, timer):
    seq.send(qlcport, '/TuttiProche/Green/Segment/[1-2]', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[1-2]', 255)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[7-8]', 255)

def horrorcore_couplet_crepitement(seq, timer):
    crepitement(seq, timer, "Tutti", "White", "{3,5}", 15, 30)

def horrorcore_couplet_crepitement_stop(seq, timer):
    seq.scene_stop('horrorcore_couplet_crepitement')
    seq.send(qlcport, '/Tutti/White/Segment/{3,5}', 0)
