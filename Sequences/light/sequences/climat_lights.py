#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

tempsStart = [':/Lightseq/Scene/Play', 'climat_theme_temps']
bimJardin = [':/Lightseq/Scene/Play', 'climat_theme_patate']
redOff = [qlcport, '/TuttiLointain/Red/Segment/{1,4,5,8}', 0]
redOn = [':/Lightseq/Scene/Play', 'climat_theme_fixe']
climat_theme_anim = [
    [tempsStart, redOn], None, None, None, None, None, None, None,
    tempsStart, None, None, None, None, None, None, None,
    tempsStart, None, None, None, None, None, None, None,
    tempsStart, None, None, bimJardin, None, None, None, None,
    None, None, None, (tempsStart,redOff), None, None, None,

    [tempsStart, redOn], None, None, None, None, None, None, None,
    tempsStart, None, None, None, None, None, None, None,
    tempsStart, None, None, None, None, None, None, bimJardin, 
    None, None, None, None, None, None, None, (tempsStart, redOff), None, None, None
    ]


waves_l2p_red = [':/Lightseq/Scene/Play', 'climat_refrain_waves', 'l2p', 'Red']
waves_p2l_red = [':/Lightseq/Scene/Play', 'climat_refrain_waves', 'p2l', 'Red']
refrain_strobe_on = [':/Lightseq/Scene/Play', 'climat_refrain_strobelights']
refrain_strobe_off = [[':/Lightseq/Scene/Stop', 'climat_refrain_strobelights'], [qlcport, '/Tutti/White/Segment/{2,3,6,7}', 0]]
climat_refrain_anim = [
    [refrain_strobe_on, waves_l2p_red], None, None, None, None, None, refrain_strobe_off, None,
    refrain_strobe_on, None, None, None, None, None, refrain_strobe_off, None,
    [refrain_strobe_on, waves_p2l_red], None, None, None, None, None, refrain_strobe_off, None,
    refrain_strobe_on, None, (None, refrain_strobe_off), bimJardin, None, None, None, None,
    None, None, None, (refrain_strobe_on, refrain_strobe_off), None, None, None,

    [refrain_strobe_on, waves_l2p_red], None, None, None, None, None, refrain_strobe_off, None,
    refrain_strobe_on, None, None, None, None, None, refrain_strobe_off, None,
    [refrain_strobe_on, waves_p2l_red], None, None, None, None, None, refrain_strobe_off, bimJardin, 
    None, None, None, None, None, None, None, (refrain_strobe_on, refrain_strobe_off), None, None, None
    ]


climat_mandela_a_a_anim = [
    [':/Lightseq/Scene/Play', 'climat_mandela_a_a_montee'], None, None, None
    ]

climat_mandela_a_a_basse_anim = [
    [[qlcport, '/damper', '/ProcheJardin/Red/Segment/{1,2,3,4,5,6,7,8}', 0.5], [qlcport, '/damper', '/ProcheCour/Red/Segment/{1,2,3,4,5,6,7,8}', 0.5], [':/Lightseq/Scene/Play', 'climat_mandela_a_a_strobe', 'White']], None, None, None,
    None, None, None, None,
    [':/Lightseq/Scene/Play', 'climat_mandela_a_a_strobe', 'Red'], None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None
    ]

purOn = [qlcport, '/TuttiProche/Red/Segment/{4,5,6,7}', 60]
purOff = [qlcport, '/TuttiProche/Red/Segment/{4,5,6,7}', 0]
climat_climax_anim = [
    (purOff, None), (purOn,purOff), (None, purOn)
    ]
