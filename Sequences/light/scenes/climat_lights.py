#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from scene_functions import *
from random import normalvariate

def climat_intro_fixe(seq, timer):
    seq.send(qlcport, '/TuttiProche/Red/Segment/{1,8}', 255)
    seq.send(qlcport, '/TuttiProche/Green/Segment/{1,8}', 156)

    seq.send(qlcport, '/TuttiLointain/Red/Segment/{4,5}', 255)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 156)

    seq.send(qlcport, '/TuttiLointain/Red/Segment/{1,2,3,6,7,8}', 63)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{1,2,3,6,7,8}', 39)

def climat_theme_fixe(seq,timer):
    eased_fade(seq, timer, '/TuttiLointain/Red/Segment/{1,4,5,8}', 0, 255, 0.2, 0.01)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{1,4,5,8}',30)

def climat_theme_temps(seq,timer):
    eased_fade(seq, timer, '/Tutti/{Green,Blue}/Segment/{2,3,6,7}', 255, 0, 0.3, 0.01)

def climat_theme_patate(seq,timer):
    side = ['Jardin', 'Cour']
    i = randint(0,1)
    eased_fade(seq, timer, '/Tutti'+side[i]+'/{Green,Blue}/Segment/{2,3,6,7}', 255, 0, 0.3, 0.01)
    timer.wait(1.75,'b')
    eased_fade(seq, timer, '/Tutti'+side[(i+1)%2]+'/{Green,Blue}/Segment/{2,3,6,7}', 255, 0, 0.3, 0.01)

def climat_theme_strobelights_alea(seq,timer, *args):
    strobelights(seq, timer, 'Tutti', '{Green,Blue}', '{2,3,6,7}', 'aleatoire', ramped = [args[0], 0, 0.5] ,alea_type = ['segment', 1] )

def climat_theme_strobelights_alea_trig(seq,timer):
    while True :
        n = normalvariate(0,1)
        if abs(n) > 0.9:
            seq.send(':/Lightseq/Scene/Play', 'climat_theme_strobelights_alea', int((10 * n + - 9) * 255))
        timer.wait(0.6, 's')
        seq.send(':/Lightseq/Scene/Stop', 'climat_theme_strobelights_alea')
        seq.send(qlcport, '/Tutti/{Green,Blue}/{2,3,6,7}', 0)

def climat_theme_strobelights_jeannot(seq,timer, on):
    if on:
        strobelights(seq, timer, 'Tutti', 'Red', '{2,3,6,7}', 'aleatoire',alea_type = ['segment', 3])
    else:
        seq.send(qlcport, '/Tutti/Red/Segment/{2,3,6,7}', 0)
    

def climat_couplet1(seq, timer):
    seq.send(qlcport, '/damper', '/Tutti/{Green,Blue}/Segment/{2,3,6,7}', 0.2)
    seq.send(qlcport, '/damper', '/Tutti/{Green,Blue}/Segment/{2,3,6,7}', 0.2)
    
    seq.animate([qlcport, '/TuttiLointain/Red/Segment/{1,4,5,8}'], 255, 122, 2)
    seq.animate([qlcport, '/TuttiLointain/Green/Segment/{1,4,5,8}'], 30, 15, 2)

    timer.wait(2.1,'s')
    seq.send(qlcport, '/damper', '/TuttiLointain/Red/Segment/{1,4,5,8}', 0.5)
    seq.send(qlcport, '/damper', '/TuttiLointain/Green/Segment/{1,4,5,8}', 0.5)


def climat_refrain_fixe(seq,timer):
    seq.send(qlcport, '/TuttiProche/Green/Segment/{1,8}', 30)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 70)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{1,2,3,6,7,8}', 20)


def climat_refrain_strobelights(seq,timer):
    strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainJardin', 'LointainCour'], 'White', '{2,3,6,7}', 'aleatoire',alea_type = ['bar', 1])

def climat_refrain_waves(seq,timer,*args):
    if args[0] == 'p2l':
        seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/'+args[1]+'/Segment/{1,8}', 30, 170, 2, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiProche/'+args[1]+'/Segment/{1,8}', 70, 30, 2, 0.01])
        timer.wait(1.8, 'b')
        seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/'+args[1]+'/Segment/{4,5}', 30, 170, 2, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiProche/'+args[1]+'/Segment/{4,5}', 70, 30, 2, 0.01])

    elif args[0] == 'l2p':
        seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiProche/'+args[1]+'/Segment/{1,8}', 30, 70, 2, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/'+args[1]+'/Segment/{1,8}', 170, 30, 2, 0.01])
        timer.wait(1.8, 'b')
        seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiProche/'+args[1]+'/Segment/{4,5}', 30, 70, 2, 0.01])
        seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/'+args[1]+'/Segment/{4,5}', 170, 30, 2, 0.01])        

def climat_mandela_a_a_montee(seq,timer):
    bar_chase(seq, timer, 'LointainJardin', [[255,0,0], [0,255,255]], segments_s = ['tb'], step = [0.125, 'b'])
    bar_chase(seq, timer, 'LointainCour', [[255,0,0], [0,255,255]], segments_s = ['tb'], step = [0.125, 'b'])
    bar_chase(seq, timer, 'LointainJardin', [[255,0,0], [0,255,255]], segments_s = ['bt'], step = [0.125, 'b'])
    bar_chase(seq, timer, 'LointainCour', [[255,0,0], [0,255,255]], segments_s = ['bt'], step = [0.125, 'b'])


def climat_mandela_a_a_strobe(seq,timer,color):
    strobelights(seq, timer, ['ProcheJardin', 'ProcheCour'], color, '{1,2,3,4,5,6,7,8}', 'aleatoire',alea_type = ['bar', 1])


def climat_climax_fixe(seq,timer):
    seq.send(qlcport,'/TuttiLointain/Red/Segment/{4,5}',130)
    seq.send(qlcport,'/TuttiLointain/Blue/Segment/{4,5}',40)

    seq.send(qlcport,'/TuttiProche/Red/Segment/8',130)
    seq.send(qlcport,'/TuttiProche/Blue/Segment/8',40)

    seq.send(qlcport,'/ProcheJardin/Red/Segment/1',180)
    seq.send(qlcport,'/ProcheJardin/Green/Segment/1',70)
    seq.send(qlcport,'/ProcheJardin/Blue/Segment/1',40)

    seq.send(qlcport,'/ProcheCour/Red/Segment/1',180)
    seq.send(qlcport,'/ProcheCour/Green/Segment/1',70)
    seq.send(qlcport,'/ProcheCour/Blue/Segment/1',40)

def climat_climax_up(seq,timer):
    crepitement(seq, timer, [['TuttiLointain', 'Red', '{7,8}', 50, 95],['TuttiLointain', 'Blue', '{7,8}', 20, 65],['TuttiLointain', 'Green', '{7,8}', 30, 65]])

