#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

dafist_intro_anim = [
    [':/Lightseq/Scene/Play', 'dafist_battements']
    ]

dafist_refrain_anim = [
    [':/Lightseq/Scene/Play', 'dafist_refrain_strobe'], None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, ([':/Lightseq/Scene/Stop', 'dafist_refrain_strobe'],  [':/Lightseq/Scene/Play', 'dafist_refrain_montee']),
    [':/Lightseq/Scene/Play', 'dafist_refrain_strobe'], None, None, None,
    None, None, None, None,
    None, (None, None, None, [':/Lightseq/Scene/Stop', 'dafist_refrain_strobe'], [qlcport, '/Stop']), None, (None, [':/Lightseq/Scene/Play', 'dafist_refrain_strobe'], None, None),
    None, None, None, ([':/Lightseq/Scene/Stop', 'dafist_refrain_strobe'], [':/Lightseq/Scene/Play', 'dafist_refrain_montee'])
    ]

dafist_couplet_anim1 = [
    [[':/Lightseq/Scene/Stop', 'dafist_couplet_oscillation_up2cour'],[':/Lightseq/Scene/Play', 'dafist_couplet_oscillation_up2jardin']], None, None, None,
    None, None, None, None,
    None, None, None, None,
    [[':/Lightseq/Scene/Stop', 'dafist_couplet_oscillation_up2jardin'],[':/Lightseq/Scene/Play', 'dafist_couplet_oscillation_up2cour']], None, None, None,
    None, None, None, None,
    None, None, None, None
    ]

dafist_couplet_anim2 = [
    [':/Lightseq/Scene/Play', 'dafist_couplet_thirdpart_flash'], None
]
