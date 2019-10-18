#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint
from scene_functions import *


def sw_intro(seq, timer):
    seq.send(qlcport, '/Tutti/Blue/Segment/{1,4,8}', 170)
    seq.send(qlcport, '/TuttiProche/White/Segment/{2,3}', 50)


def sw_couplet_auto_lights(seq, timer):
    timer.wait(7, 'b')
    seq.send(qlcport, '/TuttiLointain/White/Segment/{4,5}', 180)
    seq.send(qlcport, '/TuttiProche/White/Segment/{2,3,5,6}', 180)
    timer.wait(0.25, 'b')
    seq.send(qlcport, '/*/*/Segment/*', 0)

def sw_couplet1(seq, timer):
    eased_fade(seq, timer, ['/Tutti/Blue/Segment/{1,6,7,8}', '/TuttiProche/White/Segment/2'], 0, 150, 1, 0.01)

def sw_moroness(seq, timer):
    seq.send(':/Lightseq/Sequence/Enable', 'sw_moroness_segments')
    timer.wait(10, 'b')
    seq.send(':/Lightseq/Sequence/Disable', 'sw_moroness_segments')
    seq.send(':/Lightseq/Scene/Stop', 'sw_randomized_segments')

def sw_randomized_segment(seq, timer, dimmer):
    bar = ['ProcheJardin', 'ProcheCour', 'LointainJardin', 'LointainCour']
    segment = [2, 3, 4, 5]
    strobelights(seq, timer, bar[randint(0,3)], 'White', segment[randint(0,3)], 'aleatoire', ramped = [dimmer, 0, 0.05] ,alea_type = ['tutti', 1, 1, 1])

def sw_refrain(seq, timer):
    seq.send(qlcport, '/Tutti/White/Segment/{4,5}', 200)

def sw_refrain_strobe(seq, timer):
    strobelights(seq, timer, ['ProcheJardin','ProcheCour','LointainJardin','LointainCour'], ['Red','White'], [2,4,5,7], 'aleatoire', alea_type = ['tutti', 1, 1, 1])
