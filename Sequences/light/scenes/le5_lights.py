#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from scene_functions import *

def le5_shotgun(seq,timer):
    eased_fade(seq, timer, '/Tutti/White/Segment/All', 255, 0, 0.5, 0.01)
    timer.wait(1, 's')
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{2,4,6,8}', 0, 180, 1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{2,4,6,8}', 0, 18, 1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{2,4,6,8}', 0, 70, 1, 0.01])
    
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{1,3,5,7}', 0, 180, 1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{1,3,5,7}', 0, 18, 1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{1,3,5,7}', 0, 70, 1, 0.01])

    timer.wait(2, 's')
    seq.send(':/Lightseq/Sequence/Enable', 'le5_intro_anim')

def le5_intro_fixe(seq,timer,state):
    if state == 'a':
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{1,3,5,7}', 0, 180, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{1,3,5,7}', 0, 18, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{1,3,5,7}', 0, 70, 0.5, 0.01])

        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{2,4,6,8}', 0, 180, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{2,4,6,8}', 0, 18, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{2,4,6,8}', 0, 70, 0.5, 0.01])


        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{2,4,6,8}', 180, 0, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{2,4,6,8}', 18, 0, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{2,4,6,8}', 70, 0, 0.5, 0.01])

        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{1,3,5,7}', 180, 0, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{1,3,5,7}', 18, 0, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{1,3,5,7}', 70, 0, 0.5, 0.01])

    elif state == 'b':
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{2,4,6,8}', 0, 180, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{2,4,6,8}', 0, 18, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{2,4,6,8}', 0, 70, 0.5, 0.01])

        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{1,3,5,7}', 0, 180, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{1,3,5,7}', 0, 18, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{1,3,5,7}', 0, 70, 0.5, 0.01])
       
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{1,3,5,7}', 180, 0, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{1,3,5,7}', 18, 0, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{1,3,5,7}', 70, 0, 0.5, 0.01])

        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{2,4,6,8}', 180, 0, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{2,4,6,8}', 18, 0, 0.5, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{2,4,6,8}', 70, 0, 0.5, 0.01])

    if state == 'c':
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{1,3,5,7}', 0, 180, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{1,3,5,7}', 0, 18, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{1,3,5,7}', 0, 70, 1, 0.01])

        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{2,4,6,8}', 0, 180, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{2,4,6,8}', 0, 18, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{2,4,6,8}', 0, 70, 1, 0.01])


        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{2,4,6,8}', 180, 0, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{2,4,6,8}', 18, 0, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{2,4,6,8}', 70, 0, 1, 0.01])

        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{1,3,5,7}', 180, 0, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{1,3,5,7}', 18, 0, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{1,3,5,7}', 70, 0, 1, 0.01])

    elif state == 'd':
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{2,4,6,8}', 0, 180, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{2,4,6,8}', 0, 18, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{2,4,6,8}', 0, 70, 1, 0.01])

        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{1,3,5,7}', 0, 180, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{1,3,5,7}', 0, 18, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{1,3,5,7}', 0, 70, 1, 0.01])
       
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{1,3,5,7}', 180, 0, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{1,3,5,7}', 18, 0, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{1,3,5,7}', 70, 0, 1, 0.01])

        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{2,4,6,8}', 180, 0, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{2,4,6,8}', 18, 0, 1, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{2,4,6,8}', 70, 0, 1, 0.01])




def le5_couplet1_part1_fixe(seq,timer):
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{1,3,5,7}', 0, 180, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{1,3,5,7}', 0, 18, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{1,3,5,7}', 0, 70, 0.1, 0.01])
    
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{1,3,5,7}', 0, 180, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{1,3,5,7}', 0, 18, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{1,3,5,7}', 0, 70, 0.1, 0.01])

    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Red/Segment/1', 0, 70, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Green/Segment/1', 0, 18, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Blue/Segment/1', 0, 180, 0.1, 0.01])

    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Red/Segment/3', 0, 70, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Green/Segment/3', 0, 18, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Blue/Segment/3', 0, 180, 0.1, 0.01])

def le5_couplet1_white_flash_step1(seq,timer):
    strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainCour', 'LointainJardin'], ['White', 'Red,Blue', 'Green,Blue'], [2,4,6,8], 'aleatoire', alea_type = ['tutti', 1, 1, 1], step = 60./seq.bpm/10, ramped = [30,30,0.1])

def le5_couplet1_before_me(seq,timer):
    eased_fade(seq, timer, '/TuttiLointain/White/Segment/All', 255, 0, 0.5, 0.01)
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Red/Segment/1', 0, 70, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Green/Segment/1', 0, 8, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Blue/Segment/1', 0, 70, 0.1, 0.01])

    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Red/Segment/3', 0, 70, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Green/Segment/3', 0, 8, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Blue/Segment/3', 0, 70, 0.1, 0.01])
   

def le5_couplet1_white_flash_step2(seq,timer):
    strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainCour', 'LointainJardin'], ['White', 'Red,Blue', 'Green,Blue'], [2,4,6,8], 'aleatoire', alea_type = ['tutti', 1, 1, 1], step = 60./seq.bpm/10, ramped = [50,50,0.1])

def le5_couplet1_white_flash_step3(seq,timer):
    strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainCour', 'LointainJardin'], ['White', 'Red,Blue', 'Green,Blue'], [2,4,6,8], 'aleatoire', alea_type = ['tutti', 1, 1, 1], step = 60./seq.bpm/10, ramped = [70,70,0.1])

def le5_couplet2_white_flash_step4(seq,timer):
    strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainCour', 'LointainJardin'], ['White', 'Red,Blue', 'Green,Blue'], [2,4,6,8], 'aleatoire', alea_type = ['tutti', 1, 1, 1], step = 60./seq.bpm/10, ramped = [100,100,0.1])


def le5_refrain_fixe(seq,timer, state = 1):
    if state:
        seq.send(qlcport, '/LointainJardin/Red/Segment/{1,4,5,8}', 255)
        seq.send(qlcport, '/LointainCour/Red/Segment/{1,4,5,8}', 255)
    else:
        seq.send(qlcport, '/*/*/Segment/{1,4,5,8}', 0)

def le5_refrain_strobe(seq,timer,state = 1):
    if state :
        strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainCour', 'LointainJardin'], '{Green,Blue}', [2,3,6,7], 'aleatoire', alea_type = ['bar', 1])
    else:
        seq.send(qlcport, '/*/*/Segment/{2,3,6,7}', 0)


def le5_couplet2_nigro(seq,timer):
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Red/Segment/1', 0, 200, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Green/Segment/1', 0, 24, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Blue/Segment/1', 0, 200, 0.1, 0.01])

    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Red/Segment/3', 0, 70, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Green/Segment/3', 0, 8, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Blue/Segment/3', 0, 70, 0.1, 0.01])

    timer.wait(0.2, 's')
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Red/Segment/3', 70, 200, 8 * 60. / seq.bpm, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Green/Segment/3', 8, 24, 8 * 60. / seq.bpm, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Blue/Segment/3', 70, 200, 8 * 60./ seq.bpm, 0.01])

    timer.wait(7.3, 'b')
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Red/Segment/3', 200, 255, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Green/Segment/3', 24, 100, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Blue/Segment/3', 200, 255, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Red/Segment/1',  200, 70,  0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Green/Segment/1', 24, 8, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Blue/Segment/1', 200, 70, 0.1, 0.01])

def le5_couplet2_trap(seq,timer):
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Red/Segment/1', 0, 70, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Green/Segment/1', 0, 8, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheJardin/Blue/Segment/1', 0, 70, 0.1, 0.01])

    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Red/Segment/3', 0, 70, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Green/Segment/3', 0, 8, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Blue/Segment/3', 0, 70, 0.1, 0.01])

    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Red/Segment/{1,3,5,7}', 0, 180, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Green/Segment/{1,3,5,7}', 0, 18, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainJardin/Blue/Segment/{1,3,5,7}', 0, 70, 0.1, 0.01])
    
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Red/Segment/{1,3,5,7}', 0, 180, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Green/Segment/{1,3,5,7}', 0, 18, 0.1, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/LointainCour/Blue/Segment/{1,3,5,7}', 0, 70, 0.1, 0.01])

    
##########################################

def le5_slow_intro(seq, timer):
    eased_fade(seq, timer, '/Tutti/White/Segment/All', 255, 0, 0.35, 0.01)


    eased_fade(seq, timer, '/ProcheCour/Red/Segment/3', 0, 255, 10, 0.01)
    eased_fade(seq, timer, '/ProcheCour/Green/Segment/3', 0, 190, 10, 0.01)
    eased_fade(seq, timer, '/ProcheCour/Blue/Segment/3', 0, 207, 10, 0.01)

stepo = 0
def le5_slow_bouclage(seq,timer):
    global stepo

    if stepo:
        eased_fade(seq, timer, '/ProcheJardin/Red/Segment/1', 0, 255, 5, 0.01)
        eased_fade(seq, timer, '/ProcheJardin/Green/Segment/1', 0, 190, 5, 0.01)
        eased_fade(seq, timer, '/ProcheJardin/Blue/Segment/1', 0, 207, 5, 0.01)
    else:
        eased_fade(seq, timer, '/LointainCour/Red/Segment/{4,5}', 0, 255, 10, 0.01)
        eased_fade(seq, timer, '/LointainJardin/Green/Segment/{4,5}', 0, 190, 10, 0.01)
        eased_fade(seq, timer, '/LointainJardin/Blue/Segment/{4,5}', 0, 207, 10, 0.01)
        stepo = 1

###########################################

def le5_rabza_fixe(seq,timer):
    seq.send(qlcport, '/TuttiLointain/Red/Segment/{4,5}', 247)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 128)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/{4,5}', 49)
