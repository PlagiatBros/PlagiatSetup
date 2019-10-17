#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from random import randint

from ports import *

dafist_clignotage = [
    [':/Lightseq/Scene/Play', 'dafist_clignotageA'],[':/Lightseq/Scene/Play', 'dafist_clignotageB']
]

dafist_entreeinstru_leslie = [
    [[':/Lightseq/Scene/Play', 'dafist_leslie_o'],[':/Lightseq/Scene/Play', 'dafist_leslie_j']], None, None, None,
    None, None, None, None
]

dafist_roulettearabesques = [
    [[':/Lightseq/Scene/Play', 'dafist_roulettearabesques'],[4444,'/oui']],
    [4444,'/ouioui']
]


dafist_themerefrain_clignotagestrob = [

    [[':/Lightseq/Sequence/Enable', 'dafist_clignotage'],[':/Lightseq/Scene/Play', 'dafist_patatetemps']], [':/Lightseq/Scene/Play', 'dafist_patatetemps'], None, None,
    [':/Lightseq/Scene/Play', 'dafist_patatesyncope'], None, None, [':/Lightseq/Scene/Play', 'dafist_patatesyncope'],
    None, None, None, None,
    [':/Lightseq/Scene/Play', 'dafist_patatesyncope'], None, None, [[':/Lightseq/Sequence/Disable', 'dafist_clignotage'], [':/Lightseq/Scene/Play', 'dafist_blinderstrob'], [':/Lightseq/Scene/Play', 'dafist_vpoff']],

    [[':/Lightseq/Sequence/Enable', 'dafist_clignotage'],[':/Lightseq/Scene/Play', 'dafist_patatetemps']], [':/Lightseq/Scene/Play', 'dafist_patatetemps'], None, None,
    [':/Lightseq/Scene/Play', 'dafist_patatesyncope'], None, None, [':/Lightseq/Scene/Play', 'dafist_patatesyncope'],
    None, None, None, None,
    None, None, None, [[':/Lightseq/Sequence/Disable', 'dafist_clignotage'], [':/Lightseq/Scene/Play', 'dafist_blinderstrob'], [':/Lightseq/Scene/Play', 'dafist_vpoff']]

]

def _on():
    return [
        ['/pyta/slide/visible', 'GoatEye_10', 1],
        ['/pyta/slide/animate', 'GoatEye_10', 'scale_'+ ('y' if randint(0,1) else 'x'), 350, 800, 0.1 ],
    ]

_off = [
    ['/pyta/slide/visible', 'GoatEye_10', 0],
    ['/pyta/slide/scale_x', 'GoatEye_10', 350],
    ['/pyta/slide/scale_y', 'GoatEye_10', 350],
]

dafist_refrain = [
    (_on(), _off, None, None), (_on(), _off, None, None), (None, _on(), _off, None), (None, _on(), _off, None),
    (None, None, None ,_on()), (_off, _on(), _off, None), (None, _on(), _off, None), (None, None, None ,_on()),
    (_off, _on(), _off, None), None, (None, _on(), _off, None), (None, _on(), _off, None),
    (None, None, None ,_on()), (_off, _on(), _off, None), (_on(), _off, _on(), _off, _on(), _off), (_on(), _off, None, None, None, None),

    (_on(), _off, None, None), (_on(), _off, None, None), (None, _on(), _off, None), (None, _on(), _off, None),
    (None, None, None ,_on()), (_off, _on(), _off, None), (None, _on(), _off, None), (None, None, None ,_on()),
    (_off, _on(), _off, None), (None, None, None, _on()), (_off, None, None, None), (None, _on(), _off, None),
    (None, None, None ,_on()), (_off, _on(), _off, None), (_on(), _off, _on(), _off, _on(), _off), (_on(), _off, None, None, None, None),
]

dafist_prerefrain = [
    [['/pyta/text', 2, 'YE$'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text', 2, 'ZøøM3'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text', 2, 'ye$$$'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text', 2, 'Lâ$T'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text', 2, 'yyYEs$'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text', 2, 'ZoN'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text', 2, 'ye$$$$'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text', 2, 'Smurf'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
]

mooncupwaters_slides = '{Moise_1,Moise_2,Moise_3,Butts_1,Butts_2,Mooncup_1,Mooncup_2,Mooncup_3}'
dafist_mooncupwaters_jardin = [
    [[rpijardinport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpijardinport, '/pyta/slide/Moise_1/set', 'visible', 1]],
    [[rpijardinport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpijardinport, '/pyta/slide/Moise_2/set', 'visible', 1]],
    [[rpijardinport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpijardinport, '/pyta/slide/Moise_3/set', 'visible', 1]],
    [[rpijardinport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpijardinport, '/pyta/slide/Butts_1/set', 'visible', 1]],
    [[rpijardinport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpijardinport, '/pyta/slide/Butts_2/set', 'visible', 1]],
    [[rpijardinport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpijardinport, '/pyta/slide/Mooncup_1/set', 'visible', 1]],
    [[rpijardinport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpijardinport, '/pyta/slide/Mooncup_2/set', 'visible', 1]],
    [[rpijardinport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpijardinport, '/pyta/slide/Mooncup_3/set', 'visible', 1]],
]
dafist_mooncupwaters_cour = [
    [[rpicourport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpicourport, '/pyta/slide/Moise_1/set', 'visible', 1]],
    [[rpicourport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpicourport, '/pyta/slide/Moise_2/set', 'visible', 1]],
    [[rpicourport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpicourport, '/pyta/slide/Moise_3/set', 'visible', 1]],
    [[rpicourport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpicourport, '/pyta/slide/Butts_1/set', 'visible', 1]],
    [[rpicourport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpicourport, '/pyta/slide/Butts_2/set', 'visible', 1]],
    [[rpicourport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpicourport, '/pyta/slide/Mooncup_1/set', 'visible', 1]],
    [[rpicourport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpicourport, '/pyta/slide/Mooncup_2/set', 'visible', 1]],
    [[rpicourport, '/pyta/slide/'+mooncupwaters_slides+'/set', 'visible', 0], [rpicourport, '/pyta/slide/Mooncup_3/set', 'visible', 1]],
]
dafist_mooncupwaters_alpha = [
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.01],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.02],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.03],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.04],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.06],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.07],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.08],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.09],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.1],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.11],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.12],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.13],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.14],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.15],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.16],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.17],
]
dafist_mooncupwaters_rgb = [
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 1, 0, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 1, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0, 1],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.5, 0.5, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0.5, 0.5],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.5, 0, 0.5],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 1, 1],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 1, 1, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 1, 0, 1],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 1, 1, 1],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.5, 0.5, 0.5],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.3, 0, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0.3, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0, 0.3],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.3, 0.3, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.3, 0, 0.3],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0.3, 0.3],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.3, 0.3, 0.3],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.8, 0, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0.8, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0, 0.8],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.8, 0.8, 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0, 0.8, 0.8],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.8, 0, 0.8],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'color', 0.8, 0.8, 0.8],

]

barre = 'Dafist_trance_bar'
dafist_transe_blinkload = [
    ['/pyta/slide/visible', barre, 1], ['/pyta/slide/visible', barre, 0]
] * 2

_hide_bar = ['/pyta/slide/animate', 'Dafist_trance_bar', 'zoom', 1, 0, 0.15]
_show_bar = ['/pyta/slide/animate', 'Dafist_trance_bar', 'zoom', 0, 1, 0.15]

dafist_transe_cutoff = [
    _show_bar, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, (_hide_bar, None, None, None), None, (_show_bar, None),
]

smokes = " ".join(['Smoke_'+str(i) for i in range(1,20)])

dafist_transe_smokes_jardin = []
for i in range (1,20):
    dafist_transe_smokes_jardin.append([[rpijardinport, '/pyta/slide/visible', smokes, 0], [rpijardinport, '/pyta/slide/visible', 'Smoke_'+str(i), 1]])
dafist_transe_smokes_cour = []
for i in range (1,20):
    dafist_transe_smokes_cour.append([[rpicourport, '/pyta/slide/visible', smokes, 0], [rpicourport, '/pyta/slide/visible', 'Smoke_'+str(i), 1]])
