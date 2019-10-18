#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from scene_functions import *


def horrorcore_intro(seq, timer):
    seq.send(qlcport, '/TuttiProche/Green/Segment/[1-2]', 60)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[1-2]', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[7-8]', 255)

def horrorcore_couplet_stable(seq, timer):
    seq.send(qlcport, '/TuttiProche/Green/Segment/[1-2]', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[1-3]', 255)
    seq.send(qlcport, '/TuttiProche/Red/Segment/8', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/7', 0)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/1', 15)

def horrorcore_couplet_crepitement(seq, timer):
    crepitement(seq, timer, [["Tutti", "White", "{3,5}", 15, 30]])

def horrorcore_couplet_crepitement_stop(seq, timer):
    seq.scene_stop('horrorcore_couplet_crepitement')
    seq.send(qlcport, '/Tutti/White/Segment/{3,5}', 0)

def horrorcore_couplet_donkey(seq, timer):
    seq.send(qlcport, '/TuttiProche/*/Segment/All', 0)
    seq.send(qlcport, '/ProcheJardin/White/Segment/1', 70)
    seq.send(qlcport, '/ProcheCour/White/Segment/2', 70)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/{1,8}', 30)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{1,8}', 20)

def horrorcore_refrain_stable(seq, timer):
    seq.send(qlcport, '/TuttiProche/White/Segment/{1,2}', 200)
    seq.send(qlcport, '/TuttiProche/Green/Segment/{5,6,7,8}', 140)
    seq.send(qlcport, '/TuttiProche/Red/Segment/{5,6,7,8}', 160)
    seq.scene_run_subscene(crepitement, [seq, timer, [['TuttiProche', 'Red', '{3,4}', 15,80],['TuttiLointain', 'Red', '{1,3,5,7}', 30, 80], ['TuttiLointain', 'Green', '{1,3,5,7}', 50, 70], ['TuttiLointain', 'Red', '{2,4,6,8}', 50, 70], ['TuttiLointain', 'Green', '{2,4,6,8}', 30, 80]]])

def horrorcore_couplet2_intro(seq, timer):
    seq.send(qlcport, '/TuttiProche/White/Segment/1', 140)
    crepitement(seq, timer, [['ProcheJardin', 'Red', '2', 30, 80], ['ProcheCour', 'Red', '2', 30, 40]])

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

def horrorcore_couplet2_blinder_surcouche(seq, timer):
    seq.send(qlcport, '/TuttiLointain/{Red,Green}/Segment/8', 120)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/7', 70)


def horrorcore_messe(seq, timer):
    seq.send(qlcport, '/TuttiProche/{Red,Blue}/Segment/{7,8}', 100)
    seq.send(qlcport, '/TuttiLointain/{Red,Blue}/Segment/{2,7,8}', 190)
    seq.send(qlcport, '/TuttiProche/White/Segment/1', 75)

def horrorcore_ac4_intro1(seq,timer):
    crepitement(seq, timer, [['TuttiJardin', 'Red', '{4,5}', 30, 100], ['TuttiJardin', 'Blue', '{4,5}', 30, 100], ['TuttiCour', 'Red', '{4,5}', 30, 100], ['TuttiCour', 'Blue', '{4,5}', 30, 100]])
#    crepitement(seq, timer, [['LointainJardin', 'Red', '{1,3,5,7}', 30, 100], ['LointainJardin', 'Red', '{2,4,6,8}', 30, 100], ['LointainJardin', 'Blue', '{1,3,5,7}', 30, 100], ['LointainJardin', 'Blue', '{2,4,6,8}', 30, 100], ['LointainCour', 'Red', '{1,3,5,7}', 30, 100], ['LointainCour', 'Red', '{2,4,6,8}', 30, 100], ['LointainCour', 'Blue', '{1,3,5,7}', 30, 100], ['LointainCour', 'Blue', '{2,4,6,8}', 30, 100]])

def horrorcore_ac4_intro2(seq,timer):
    strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainJardin', 'LointainCour'], ['White'], [1, 2, 3, 6, 7, 8], 'aleatoire', step= 0.01, ramped = [0, 255, 60], alea_type = ['tutti', 1, 1, 1])


def horrorcore_dropTheBass(seq,timer):
    seq.send(qlcport, '/Tutti/Green/Segment/1', 118)
    seq.send(qlcport, '/Tutti/Blue/Segment/1', 25)
    seq.send(qlcport, '/Tutti/Red/Segment/8', 50)

def horrorcore_mooncup_maison(seq,timer):
    crepitement(seq, timer, [['Tutti', 'Red', 'All', 120, 255]])
