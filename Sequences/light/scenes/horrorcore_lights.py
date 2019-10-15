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
    seq.send(qlcport, '/TuttiProche/Red/Segment/[1-3]', 255)
    seq.send(qlcport, '/TuttiProche/Red/Segment/8', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/7', 0)

def horrorcore_couplet_crepitement(seq, timer):
    crepitement(seq, timer, "Tutti", "White", "{3,5}", 15, 30)

def horrorcore_couplet_crepitement_stop(seq, timer):
    seq.scene_stop('horrorcore_couplet_crepitement')
    seq.send(qlcport, '/Tutti/White/Segment/{3,5}', 0)

def horrorcore_couplet_donkey(seq, timer):
    seq.send(qlcport, '/TuttiProche/*/Segment/All', 0)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/{1,8}', 30)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{1,8}', 20)

def horrorcore_sun_zoom(seq, timer):
    seq.send(rpijardinport, '/pyta/slide/Sun_1/animate', 'tiles', 1, 1, 0.1, 0.1, 1, 'sine')    
    seq.send(rpicourport, '/pyta/slide/Sun_2/animate', 'tiles', 1, 1, 0.1, 0.1, 1, 'sine')    

def horrorcore_white_flash(seq, timer):
    seq.send(rpijardinport, '/pyta/slide/white/set', 'visible', 1)
    seq.send(qlcport, '/*/White/Segment/*', 255)
    timer.wait(0.001, 's')
    seq.send(qlcport, '/*/White/Segment/*', 0)
    timer.wait(0.03, 's')
    seq.send(rpijardinport, '/pyta/slide/white/set', 'visible', 0)


def horrorcore_couplet2_dubstep_extinction(seq, timer):
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'rgbwave', 0.3)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'position_z', -1)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'rgbwave', 0.3)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'position_z', -1)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'zoom', 1.5)    
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'zoom', 1.5)    
    horrorcore_sun_zoom(seq, timer)

    seq.send(':/Lightseq/Sequence/Disable', 'horrorcore_couplet_blinkBass')
    seq.send(qlcport, '/*/*/Segment/*', 0)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 1)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 1)
    horrorcore_sun_zoom(seq, timer)

    timer.wait(20, 'b')
    seq.send(':/Lightseq/Scene/Play', 'horrorcore_white_flash')
    seq.send(':/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass')
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 0)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 0)

    timer.wait(140, 'b')
    seq.send(':/Lightseq/Sequence/Disable', 'horrorcore_couplet_blinkBass')
    seq.send(qlcport, '/*/*/Segment/*', 0)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 1)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 1)
    horrorcore_sun_zoom(seq, timer)

    timer.wait(20, 'b')
    seq.send(':/Lightseq/Scene/Play', 'horrorcore_white_flash')
    seq.send(':/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass')
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 0)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 0)

    timer.wait(150, 'b')
    seq.send(':/Lightseq/Sequence/Disable', 'horrorcore_couplet_blinkBass')
    seq.send(qlcport, '/*/*/Segment/*', 0)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 1)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 1)
    horrorcore_sun_zoom(seq, timer)

    timer.wait(20, 'b')
    seq.send(':/Lightseq/Scene/Play', 'horrorcore_white_flash')
    seq.send(':/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass')
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 0)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 0)
