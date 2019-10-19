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

dafist_transe_anim = [
    ([qlcport, '/TuttiProche/White/Segment/4', 255], [qlcport, '/TuttiProche/White/Segment/4', 0], None, None)
    ]

dafist_transe_toto = [':/Lightseq/Scene/Play', 'dafist_transe_tot']

dafist_transe_tata = [
    [[':/Lightseq/Scene/Play', 'dafist_transe_tota'],dafist_transe_toto], dafist_transe_toto, dafist_transe_toto, dafist_transe_toto,
    [[':/Lightseq/Scene/Play', 'dafist_transe_tota'],dafist_transe_toto], dafist_transe_toto, dafist_transe_toto, dafist_transe_toto,
    [[':/Lightseq/Scene/Play', 'dafist_transe_tota'],dafist_transe_toto], dafist_transe_toto, dafist_transe_toto, dafist_transe_toto,
    [[':/Lightseq/Scene/Play', 'dafist_transe_tota'],dafist_transe_toto], dafist_transe_toto, dafist_transe_toto, dafist_transe_toto,
    [[':/Lightseq/Scene/Play', 'dafist_transe_tota'],dafist_transe_toto], dafist_transe_toto, dafist_transe_toto, dafist_transe_toto,
    [[':/Lightseq/Scene/Play', 'dafist_transe_tota'],dafist_transe_toto], dafist_transe_toto, dafist_transe_toto, dafist_transe_toto,
    [[':/Lightseq/Scene/Play', 'dafist_transe_tota'],dafist_transe_toto], dafist_transe_toto, dafist_transe_toto, dafist_transe_toto,
    [[':/Lightseq/Scene/Play', 'dafist_transe_tota'],dafist_transe_toto], [':/Lightseq/Scene/Play', 'dafist_refrain_strobe'], None, (None, [[':/Lightseq/Scene/Stop', 'dafist_refrain_strobe'], [qlcport, '/Stop']])
    ]
