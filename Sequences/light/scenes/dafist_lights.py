#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from scene_functions import *

def dafist_intro_fixe(seq, timer):
    seq.send(qlcport, '/ProcheCour/Red/Segment/{1,2,3,8}', 255)
    seq.send(qlcport, '/ProcheCour/Green/Segment/{1,2,3,8}', 140)
    seq.send(qlcport, '/ProcheCour/Blue/Segment/{1,2,3,8}', 180)

    seq.send(qlcport, '/ProcheJardin/Red/Segment/{1,2,3,8}', 255)
    seq.send(qlcport, '/ProcheJardin/Green/Segment/{1,2,3,8}', 100)
    seq.send(qlcport, '/ProcheJardin/Blue/Segment/{1,2,3,8}', 30)

    seq.send(qlcport, '/LointainCour/Red/Segment/{2,3,8}', 30)
    seq.send(qlcport, '/LointainCour/Green/Segment/{2,3,8}', 18)
    seq.send(qlcport, '/LointainCour/Blue/Segment/{2,3,8}', 22)

    seq.send(qlcport, '/LointainJardin/Red/Segment/{2,3,8}', 30)
    seq.send(qlcport, '/LointainJardin/Green/Segment/{2,3,8}', 12)
    seq.send(qlcport, '/LointainJardin/Blue/Segment/{2,3,8}', 3)

def dafist_battements(seq,timer):
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiCour/Red/Segment/{4,5,6,7}', 255, 0, 0.25*seq.bpm/60, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiCour/Green/Segment/{4,5,6,7}', 140, 0, 0.25*seq.bpm/60, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiCour/Blue/Segment/{4,5,6,7}', 180, 0, 0.25*seq.bpm/60, 0.01])

    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiJardin/Red/Segment/{4,5,6,7}', 255, 0, 0.25*seq.bpm/60, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiJardin/Green/Segment/{4,5,6,7}', 100, 0, 0.25*seq.bpm/60, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiJardin/Blue/Segment/{4,5,6,7}', 30, 0, 0.25*seq.bpm/60, 0.01])

def dafist_battements_intensity(seq,timer):
    while True:
        seq.send(qlcport, '/damper', '/TuttiCour/Red/Segment/{4,5,6,7}', randint(0,50)/100.)
        seq.send(qlcport, '/damper', '/TuttiCour/Green/Segment/{4,5,6,7}', randint(0,50)/100.)
        seq.send(qlcport, '/damper', '/TuttiCour/Blue/Segment/{4,5,6,7}', randint(0,50)/100.)

        seq.send(qlcport, '/damper', '/TuttiJardin/Red/Segment/{4,5,6,7}', randint(0,50)/100.)
        seq.send(qlcport, '/damper', '/TuttiJardin/Green/Segment/{4,5,6,7}', randint(0,50)/100.)
        seq.send(qlcport, '/damper', '/TuttiJardin/Blue/Segment/{4,5,6,7}', randint(0,50)/100.)
        timer.wait(1, 'b')

def dafist_refrain_strobe(seq,timer):
    strobelights(seq, timer, ['ProcheJardin','ProcheCour','LointainJardin','LointainCour'], 'White', 'All', 'aleatoire', alea_type = ['bar', 1])

def dafist_refrain_montee(seq,timer):
    
    seq.scene_run_subscene(eased_fade,[seq, timer, '/TuttiLointain/{Blue,Green}/Segment/All', 0, 255, 0.1*seq.bpm/60, 0.01])
    timer.wait(0.15, 'b')
    seq.scene_run_subscene(eased_fade,[seq, timer, '/TuttiLointain/{Red}/Segment/All', 0, 255, 0.1*seq.bpm/60, 0.01])
    timer.wait(0.1, 'b')
    seq.scene_run_subscene(eased_fade,[seq, timer, '/TuttiLointain/{Blue,Green}/Segment/All', 255, 0, 0.1*seq.bpm/60, 0.01])
    timer.wait(0.1, 'b')
    seq.scene_run_subscene(eased_fade,[seq, timer, '/TuttiLointain/{Red}/Segment/All', 255, 0, 0.1*seq.bpm/60, 0.01])

                       
def dafist_couplet_firstpart_fixe(seq,timer):
    seq.send(qlcport, '/ProcheCour/Red/Segment/{1,8}', 105)
    seq.send(qlcport, '/ProcheCour/Green/Segment/{1,8}', 140)
    seq.send(qlcport, '/ProcheCour/Blue/Segment/{1,8}', 100)

    seq.send(qlcport, '/ProcheJardin/Red/Segment/{4,8}', 35)
    seq.send(qlcport, '/ProcheJardin/Green/Segment/{4,8}', 80)
    seq.send(qlcport, '/ProcheJardin/Blue/Segment/{4,8}', 50)

    crepitement(seq, timer, [['LointainCour', 'Red', '{4,5,6}', 100, 105], ['LointainCour', 'Green', '{4,5,6}', 140, 150],['LointainCour', 'Blue', '{4,5,6}', 96, 110],['LointainJardin', 'Red', '{4,5,6}', 100, 105], ['LointainJardin', 'Green', '{4,5,6}', 140, 150],['LointainJardin', 'Blue', '{4,5,6}', 96, 110]])

def dafist_couplet_oscillation_up2cour(seq,timer):
    seq.animate([qlcport, '/damper', '/LointainCour/Red/Segment/{4,5,6}'], 0.01, 1, 8, 'b')
    seq.animate([qlcport, '/damper', '/LointainCour/Blue/Segment/{4,5,6}'], 0.01, 1, 8, 'b')
    seq.animate([qlcport, '/damper', '/LointainCour/Green/Segment/{4,5,6}'], 0.01, 1, 8, 'b')

    seq.animate([qlcport, '/damper', '/LointainJardin/Red/Segment/{4,5,6}'], 1, 0.01, 8, 'b')
    seq.animate([qlcport, '/damper', '/LointainJardin/Blue/Segment/{4,5,6}'], 1, 0.01, 8, 'b')
    seq.animate([qlcport, '/damper', '/LointainJardin/Green/Segment/{4,5,6}'], 1, 0.01, 8, 'b')

def dafist_couplet_oscillation_up2jardin(seq,timer):
    seq.animate([qlcport, '/damper', '/LointainJardin/Red/Segment/{4,5,6}'], 0.01, 1, 8, 'b')
    seq.animate([qlcport, '/damper', '/LointainJardin/Blue/Segment/{4,5,6}'], 0.01, 1, 8, 'b')
    seq.animate([qlcport, '/damper', '/LointainJardin/Green/Segment/{4,5,6}'], 0.01, 1, 8, 'b')

    seq.animate([qlcport, '/damper', '/LointainCour/Red/Segment/{4,5,6}'], 1, 0.01, 8, 'b')
    seq.animate([qlcport, '/damper', '/LointainCour/Blue/Segment/{4,5,6}'], 1, 0.01, 8, 'b')
    seq.animate([qlcport, '/damper', '/LointainCour/Green/Segment/{4,5,6}'], 1, 0.01, 8, 'b')

def dafist_couplet_secondpart_fixe(seq,timer):
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/8', 200)
    seq.send(qlcport, '/LointainCour/Blue/Segment/{1,7}', 130)
    seq.send(qlcport, '/ProcheJardin/White/Segment/{1,2}', 200)

    seq.send(qlcport, '/damper', '/LointainJardin/Red/Segment/{4,5,6}', 0)
    seq.send(qlcport, '/damper', '/LointainJardin/Blue/Segment/{4,5,6}', 0)
    seq.send(qlcport, '/damper', '/LointainJardin/Green/Segment/{4,5,6}', 0)

    seq.send(qlcport, '/damper', '/LointainCour/Red/Segment/{4,5,6}', 0)
    seq.send(qlcport, '/damper', '/LointainCour/Blue/Segment/{4,5,6}', 0)
    seq.send(qlcport, '/damper', '/LointainCour/Green/Segment/{4,5,6}', 0)

def dafist_couplet_thirdpart_fixe(seq,timer):
    seq.send(qlcport, '/TuttiProche/Blue/Segment/8', 200)
    seq.send(qlcport, '/LointainCour/Blue/Segment/{2,6}', 130)


transe_bass = 0
def dafist_couplet_thirdpart_flash(seq,timer):
    global transe_bass
    transe_bass = 0 # sécu si jamais transe jouée en balances
    seq.scene_run_subscene(eased_fade,[seq, timer, '/Tutti/Blue/Segment/{1,4,5,7}', 0, 255, 0.1*seq.bpm/60, 0.01])
    timer.wait(0.45, 'b')
    eased_fade(seq, timer, '/Tutti/Green/Segment/{1,4,5,7}', 160, 255, 0.1*seq.bpm/60, 0.01)
    eased_fade(seq, timer, '/Tutti/{Blue,Green}/Segment/{1,4,5,7}', 255, 0, 0.1*seq.bpm/60, 0.01)


    
def dafist_transe_intro(seq,timer):
    global transe_bass
    crepitement(seq, timer, [['TuttiLointain', 'Red', '{1,4,5,8}', 85, 104], ['TuttiLointain', 'Green', '{1,4,5,8}', 125, 140], ['TuttiLointain', 'Blue', '{1,4,5,8}', 85, 100]])


transe_step = 0
prev_damp = 0
def dafist_transe_intro_init(seq,timer):
    global transe_step, prev_damp, transe_bass
    transe_step = 0
    prev_damp = 0.01
    if transe_bass == 1:
        prev_damp = 1
    else:
        transe_bass = 1
    seq.send(qlcport, '/damper', '/TuttiLointain/Red/Segment/{1,4,5,8}', prev_damp)
    seq.send(qlcport, '/damper', '/TuttiLointain/Green/Segment/{1,4,5,8}', prev_damp)
    seq.send(qlcport, '/damper', '/TuttiLointain/Blue/Segment/{1,4,5,8}', prev_damp)
    seq.send(qlcport, '/damper', '/TuttiProche/White/Segment/4', prev_damp)
    transe_step = 1



def dafist_transe_intro_step(seq,timer):
    global transe_step, prev_damp
    croissance = transe_step * 0.08
    seq.animate([qlcport, '/damper', '/TuttiLointain/Red/Segment/{1,4,5,8}'], prev_damp, croissance, 5)
    seq.animate([qlcport, '/damper', '/TuttiLointain/Green/Segment/{1,4,5,8}'], prev_damp, croissance, 5)
    seq.animate([qlcport, '/damper', '/TuttiLointain/Blue/Segment/{1,4,5,8}'], prev_damp, croissance, 5)
#    seq.animate([qlcport, '/damper', '/TuttiProche/White/Segment/4'], prev_damp, croissance, 10)
    prev_damp = croissance
    transe_step = transe_step + 1

def dafist_transe_tot(seq,timer):
    bar_chase(seq, timer, 'TuttiLointain', [[255, 255, 255]], ['bt'], [0.12, 'b'])

def dafist_transe_tota(seq,timer):
    bar_chase(seq, timer, 'TuttiProche', [[30, 120, 140]], ['bt'], [0.25, 'b'])

