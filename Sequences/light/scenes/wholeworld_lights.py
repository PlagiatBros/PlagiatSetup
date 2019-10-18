#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from scene_functions import *


def wholeworld_intro(seq, timer):
    seq.send(qlcport, '/TuttiProche/White/Segment/{1,2,8}', 200)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/{4,5}', 255)
    seq.send(qlcport, '/TuttiLointain/{Blue,Green}/Segment/{4,5}', 200)

def wholeworld_pont(seq,timer):
    seq.send(qlcport, '/TuttiProche/White/Segment/{1,2,8}', 200)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/{4,5}', 255)
    seq.send(qlcport, '/TuttiLointain/{Blue,Green}/Segment/{4,5}', 200)

    strobelights(seq, timer, ['ProcheJardin','ProcheCour','LointainJardin','LointainCour'], ['Red','White','{Blue,Green}'], 'All', 'aleatoire', step = 60/seq.bpm/4, alea_type = ['tutti', 1, 1, 1])

def wholeworld_faded_redflash(seq,timer):
    eased_fade(seq, timer, '/TuttiProche/Red/Segment/{3,4,5,6,7}', 255, 0, 0.25*60/seq.bpm, 0.01)

def wholeworld_faded_gbflash(seq,timer):
    eased_fade(seq, timer, '/TuttiProche/{Blue,Green}/Segment/{3,4,5,6,7}', 100, 0, 0.12*60/seq.bpm, 0.01)

def wholeworld_faded_redpump(seq,timer):
    eased_fade(seq, timer, '/TuttiProche/Red/Segment/{3,4,5,6,7}', 0, 255, 0.5*60/seq.bpm, 0.01)
    eased_fade(seq, timer, '/TuttiProche/Red/Segment/{3,4,5,6,7}', 255, 0, 0.25*60/seq.bpm, 0.01)

def wholeworld_couplet(seq,timer):
    crepitement(seq, timer, [['TuttiProche', 'White', '1', 200, 205], ['TuttiProche', 'White', '{2,8}', 200, 205], ['TuttiLointain', '{Green,Blue}', '{4,5}', 150, 160], ['TuttiLointain', 'Red', '{4,5}', 200, 205]])

def wholeworld_synthflash(seq,timer):
    eased_fade(seq, timer, '/TuttiLointain/Red/Segment/{1,2,3,6,7,8}', 180, 0, 0.25*60/seq.bpm, 0.01)
    eased_fade(seq, timer, '/TuttiLointain/{Green,Blue}/Segment/{1,2,3,6,7,8}', 100, 0, 0.25*60/seq.bpm, 0.01)

def wholeworld_refrain_fixe(seq,timer):
    crepitement(seq, timer, [['TuttiLointain', '{Red,Green}', '{4,5,8}', 70, 150]])

def wholeworld_refrain_strobe(seq,timer):
    strobelights(seq, timer, ['ProcheJardin','ProcheCour'], ['Red','Green','White'], [1, 2, 3, 6, 7, 8], 'aleatoire', step = 0.25*60/seq.bpm/4, alea_type = ['tutti', 1, 1, 3])

def wholeworld_boomboclaat(seq,timer):
    strobelights(seq, timer, ['ProcheJardin','ProcheCour'], ['Red'], [1, 2, 3, 6, 7, 8], 'aleatoire', ramped = [20, 180, 9], step = 0.25*60/seq.bpm/4, alea_type = ['tutti', 1, 1, 3])
