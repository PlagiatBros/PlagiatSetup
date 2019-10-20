#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from scene_functions import *
from random import normalvariate

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
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Red/Segment/3', 0, 255, 10, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Green/Segment/3', 0, 190, 10, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/ProcheCour/Blue/Segment/3', 0, 207, 10, 0.01])

stepo = 0
def le5_slow_bouclage(seq,timer,reset = 0):
    global stepo
    if reset:
        stepo = 0
        return

    if stepo:
        eased_fade(seq, timer, '/ProcheJardin/Red/Segment/1', 0, 255, 5, 0.01)
        eased_fade(seq, timer, '/ProcheJardin/Green/Segment/1', 0, 190, 5, 0.01)
        eased_fade(seq, timer, '/ProcheJardin/Blue/Segment/1', 0, 207, 5, 0.01)
    else:
        stepo = 1
        seq.scene_run_subscene(eased_fade,[seq, timer, '/LointainCour/Red/Segment/{4,5}', 0, 255, 10, 0.01])
        seq.scene_run_subscene(eased_fade,[seq, timer, '/LointainJardin/Green/Segment/{4,5}', 0, 190, 10, 0.01])
        seq.scene_run_subscene(eased_fade,[seq, timer, '/LointainJardin/Blue/Segment/{4,5}', 0, 207, 10, 0.01])

        

###########################################

def le5_rabza_fixe(seq,timer):
    seq.send(qlcport, '/TuttiLointain/Red/Segment/{4,5}', 247)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 128)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/{4,5}', 49)


def le5_rabza_red_flash(seq,timer):
    seq.scene_run_subscene(eased_fade,[seq, timer, '/Tutti/Red/Segment/8', 247, 0, 0.2, 0.01])
    seq.scene_run_subscene(eased_fade,[seq, timer, '/Tutti/Green/Segment/8', 128, 0, 0.2, 0.01])
    seq.scene_run_subscene(eased_fade,[seq, timer, '/Tutti/Blue/Segment/8', 49, 0, 0.2, 0.01])

def le5_rabza_ct_flash(seq,timer,state=1):
    if state:
        seq.send(qlcport, '/ProcheJardin/Red/Segment/3', 20)
        seq.send(qlcport, '/ProcheJardin/Green/Segment/3', 128)
        seq.send(qlcport, '/ProcheJardin/Blue/Segment/3', 247)

        seq.send(qlcport, '/ProcheCour/Red/Segment/5', 20)
        seq.send(qlcport, '/ProcheCour/Green/Segment/5', 128)
        seq.send(qlcport, '/ProcheCour/Blue/Segment/5', 247)
    else:
        seq.send(qlcport, '/ProcheJardin/Red/Segment/3', 0)
        seq.send(qlcport, '/ProcheJardin/Green/Segment/3', 0)
        seq.send(qlcport, '/ProcheJardin/Blue/Segment/3', 0)

        seq.send(qlcport, '/ProcheCour/Red/Segment/5', 0)
        seq.send(qlcport, '/ProcheCour/Green/Segment/5', 0)
        seq.send(qlcport, '/ProcheCour/Blue/Segment/5', 0)

def le5_rabza_refrain_strobe(seq,timer):
    strobelights(seq, timer, 'TuttiLointain', 'White', [1,2,3,4,5,6,7], 'aleatoire', alea_type = ['segment', 1] )
    

def le5_rabza_theme_chase(seq,timer):
    bar_chase(seq, timer, 'LointainJardin', [[247,128,20],[20,128,247]], ['tb'], [0.125, 'b'])
    bar_chase(seq, timer, 'LointainCour', [[247,128,20],[20,128,247]], ['tb'], [0.125, 'b'])
    seq.scene_run_subscene(bar_chase,[seq, timer, 'LointainJardin', [[247,128,20],[20,128,247]], ['tb'], [0.0625, 'b']])
    seq.scene_run_subscene(bar_chase,[seq, timer, 'LointainCour', [[247,128,20],[20,128,247]], ['tb'], [0.0625, 'b']])
    timer.wait(0.25, 'b')
    eased_fade(seq, timer, '/TuttiLointain/White/Segment/All', 255, 0, 0.3, 0.01)
    seq.scene_run_subscene(bar_chase,[seq, timer, 'LointainJardin', [[247,128,20],[20,128,247]], ['bt'], [0.0625, 'b']])
    seq.scene_run_subscene(bar_chase,[seq, timer, 'LointainCour', [[247,128,20],[20,128,247]], ['bt'], [0.0625, 'b']])
    timer.wait(0.25, 'b')
    eased_fade(seq, timer, '/TuttiLointain/White/Segment/All', 255, 0, 0.3, 0.01)

def le5_rabza_couplet_fixe(seq,timer):
        seq.send(qlcport, '/ProcheJardin/Red/Segment/1', 70)
        seq.send(qlcport, '/ProcheJardin/Green/Segment/2', 128)
        seq.send(qlcport, '/ProcheJardin/Blue/Segment/2', 247)

        seq.send(qlcport, '/ProcheCour/Red/Segment/2', 70)
        seq.send(qlcport, '/ProcheCour/Green/Segment/3', 128)
        seq.send(qlcport, '/ProcheCour/Blue/Segment/3', 247)

def le5_rabza_couplet_ct_flash(seq,timer,dimmax = 150):
        seq.scene_run_subscene(eased_fade,[seq, timer, '/ProcheJardin/Red/Segment/1', 150, 0, 0.1, 0.01])
        seq.scene_run_subscene(eased_fade,[seq, timer, '/ProcheCour/Red/Segment/1', 150, 0, 0.1, 0.01])

##################################################

def le5_meshug_fixe(seq,timer):
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/White/Segment/1', 255, 0, 0.3, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/White/Segment/2', 255, 0, 0.35, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/White/Segment/3', 255, 0, 0.4, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/White/Segment/4', 255, 0, 0.45, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/White/Segment/5', 255, 0, 0.5, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/White/Segment/6', 255, 0, 0.55, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/White/Segment/7', 255, 0, 0.6, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/Red/Segment/8', 255, 38, 1, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/Green/Segment/8', 255, 101, 1, 0.01])
    seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiLointain/Blue/Segment/8', 255, 47, 1, 0.01])

def le5_meshug_patate_flash(seq,timer, nb = 4):
    pau = 0.1
    aj = 0.05
    if nb > 7:
        aj = 0.01
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/White/Segment/1', 255, 0, pau, 0.01])
        pau = pau + aj
    if nb > 6:
        if aj > 0.03:
            aj = 0.03
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/White/Segment/2', 255, 0, pau, 0.01])
        pau = pau + aj
    if nb > 5:
        if aj > 0.04:
            aj = 0.04
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/White/Segment/3', 255, 0, pau, 0.01])
        pau = pau + aj
    if nb > 4:
        if aj > 0.05:
            aj = 0.05
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/White/Segment/4', 255, 0, pau, 0.01])
        pau = pau + aj
    if nb > 3:
        if aj > 0.05:
            aj = 0.05
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/White/Segment/5', 255, 0, pau, 0.01])
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/White/Segment/6', 255, 0, pau+aj, 0.01])
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/White/Segment/7', 255, 0, pau+aj*2, 0.01])
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/Red/Segment/8', 255, 4, pau+aj*3, 0.01])
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/Green/Segment/8', 255, 10, pau+aj*3, 0.01])
        seq.scene_run_subscene(eased_fade,[seq,timer, '/TuttiProche/Blue/Segment/8', 255, 5, pau+aj*3, 0.01])


def le5_meshug_boum1(seq, timer):
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/{4,5}', 100)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 120)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/{4,5}', 100)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 120)
    strobelights(seq, timer, 'TuttiLointain', 'Red', '{1,3,5,7}', 'together', step = 60./seq.bpm*4)

def le5_meshug_boum2(seq, timer):
    strobelights(seq, timer, 'TuttiProche', 'Red', [1,3,5,7], 'aleatoire', alea_type = ['segment', 1], ramped=[50,50,1],step = 60./seq.bpm/4)

def le5_meshug_strobelights_alea(seq,timer, *args):
    strobelights(seq, timer, 'Tutti', '{Green,Blue}', '{2,6,8}', 'aleatoire', ramped = [args[0], 0, 2] ,alea_type = ['segment', 1] )

def le5_meshug_strobelights_alea_trig(seq,timer):
    while True :
        n = normalvariate(0,1)
        if abs(n) > 0.9:
            seq.send(':/Lightseq/Scene/Play', 'le5_meshug_strobelights_alea', int((10 * n + - 9) * 255))
        timer.wait(0.6, 's')
        seq.send(':/Lightseq/Scene/Stop', 'le5_meshug_strobelights_alea')
        seq.send(qlcport, '/Tutti/{Green,Blue}/{2,6,8}', 0)

def le5_meshug_strobelights_sac(seq,timer, state):
    if state:
        strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainJardin', 'LointainCour'], 'White', 'All', 'aleatoire' ,alea_type = ['bar', 1] )
    else:
        seq.send(qlcport, '/Stop')
        seq.send(':/Lightseq/Scene/Play', 'le5_meshug_boum1')
        seq.send(':/Lightseq/Scene/Play', 'le5_meshug_boum2')

def le5_meshug_casse(seq,timer):
        strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainJardin', 'LointainCour'], ['Red', 'White', 'Green', 'Blue', '{Green,Blue}', '{Red,Blue}', '{Red,Green}'], [1,2,3,4,5,6,7,8], 'aleatoire', ramped=[12,12,1], alea_type = ['tutti', 1, 1, 1] )
