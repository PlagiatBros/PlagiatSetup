#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *


le5_intro_anim = [
    [':/lightseq/Scene/Play', 'le5_intro_fixe', 'a'], None, None, None, None,
    [':/lightseq/Scene/Play', 'le5_intro_fixe', 'b'], None, None, None, None,
    [':/lightseq/Scene/Play', 'le5_intro_fixe', 'a'], None, None, None, None,
    [':/lightseq/Scene/Play', 'le5_intro_fixe', 'b'], None, None, None, None,

    [':/lightseq/Scene/Play', 'le5_intro_fixe', 'a'], None, None, None, None,
    [':/lightseq/Scene/Play', 'le5_intro_fixe', 'b'], None, None, None, None,
    [':/lightseq/Scene/Play', 'le5_intro_fixe', 'c'], None, None, None, None,
    None, None, None, None, None,
    [':/lightseq/Scene/Play', 'le5_intro_fixe', 'd'], None, None, None, None,
    None, None, None, None, None
    ]

le5_couplet1_anim1 = [
    [':/Lightseq/Scene/Play', 'le5_couplet1_white_flash_step1'], None, None, None, None,
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, [':/Lightseq/Scene/Stop', 'le5_couplet1_white_flash_step1'], None, None, 
]

le5_couplet1_anim2 = [
    [':/Lightseq/Scene/Play', 'le5_couplet1_white_flash_step2'], None, None, None, None,
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, [':/Lightseq/Scene/Stop', 'le5_couplet1_white_flash_step2'], None, None, 
    [':/Lightseq/Scene/Play', 'le5_couplet1_white_flash_step2'], None, None, None, None,
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, [':/Lightseq/Scene/Stop', 'le5_couplet1_white_flash_step2'], None, None, 
]

le5_couplet1_anim3 = [
    [':/Lightseq/Scene/Play', 'le5_couplet1_white_flash_step3'], None, None, None, None,
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, [':/Lightseq/Scene/Stop', 'le5_couplet1_white_flash_step3'], None, None, 
]

refrainOn = [[':/Lightseq/Scene/Play', 'le5_refrain_fixe', 1], [':/Lightseq/Scene/Play', 'le5_refrain_strobe', 1]]
refrainOff = [[':/Lightseq/Scene/Play', 'le5_refrain_fixe', 0], [':/Lightseq/Scene/Play', 'le5_refrain_strobe', 0]]
le5_refrain_anim = [
    refrainOn, None, None, None, None,
    None, None, None, None, None,
    None, None, None, None, None,
    None, None, None, None, None,
    None, None, None, None, None,
    None, None, None, None, None,
    None, None, None, None, None,
    None, None, refrainOff, None, None,
]

redOnTrap1 = [qlcport, '/TuttiLointain/Red/Segment/{2,4,6,8}', 255]
redOnTrap2 = [qlcport, '/ProcheJardin/Red/Segment/{2,4,6,8}', 255]
redOnTrap3 = [qlcport, '/ProcheCour/Red/Segment/{2,4,6,8}', 255]
whiteOnTrap = [qlcport, '/TuttiLointain/White/Segment/{2,4,6,8}', 255]
offTrap = [qlcport, '/*/*/Segment/{2,4,6,8}', 0]
le5_couplet2_trap = [
    redOnTrap1, offTrap, None, None, None,
    None, whiteOnTrap, offTrap, None, None,
    (redOnTrap3, None, offTrap), (None, redOnTrap2, None), (offTrap, None, redOnTrap1), (None, offTrap, None), None, 
    None, whiteOnTrap, offTrap, None, None,
    None, None, None, None, None,
    None, None, None, None, None,
    whiteOnTrap, offTrap, None, None, None,
    None, [redOnTrap1, redOnTrap2, redOnTrap3], None, None, None, None
]

le5_couplet2_anim4 = [
    [':/Lightseq/Scene/Play', 'le5_couplet2_white_flash_step4'], None, None, None, None,
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, None, None, None, 
    None, None, [':/Lightseq/Scene/Stop', 'le5_couplet2_white_flash_step4'], None, None, 
]
