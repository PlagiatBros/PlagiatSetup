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
    [['/pyta/text', 2, 'YE$'], ['/pyta/text/visible', 2, 1]], ['/pyta/text/visible', 2, 0], None, None,
    [['/pyta/text', 2, 'Ye$s'], ['/pyta/text/visible', 2, 1]], ['/pyta/text/visible', 2, 0], None, None,
    [['/pyta/text', 2, 'ye$$$'], ['/pyta/text/visible', 2, 1]], ['/pyta/text/visible', 2, 0], None, None,
    [['/pyta/text', 2, 'yE$$'], ['/pyta/text/visible', 2, 1]], ['/pyta/text/visible', 2, 0], None, None,
    [['/pyta/text', 2, 'yyYEs$'], ['/pyta/text/visible', 2, 1]], ['/pyta/text/visible', 2, 0], None, None,
    [['/pyta/text', 2, 'Ye$s$$'], ['/pyta/text/visible', 2, 1]], ['/pyta/text/visible', 2, 0], None, None,
    [['/pyta/text', 2, 'ye$$$$'], ['/pyta/text/visible', 2, 1]], ['/pyta/text/visible', 2, 0], None, None,
    [['/pyta/text', 2, 'YYYE$$$$'], ['/pyta/text/visible', 2, 1]], ['/pyta/text/visible', 2, 0], None, None,
]

mooncupwaters_slides = 'MoiseWaters_1 MoiseWaters_2 MoiseWaters_3 Butts_1 Butts_2 Mooncup_1 Monncup_2 Mooncup_3'
dafist_mooncupwaters_jardin = [
    [[rpijardinport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'MoiseWaters_1', 1]],
    [[rpijardinport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'MoiseWaters_2', 1]],
    [[rpijardinport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'MoiseWaters_3', 1]],
    [[rpijardinport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Butts_1', 1]],
    [[rpijardinport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Butts_2', 1]],
    [[rpijardinport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Mooncup_1', 1]],
    [[rpijardinport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Mooncup_2', 1]],
    [[rpijardinport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Mooncup_3', 1]],
]
dafist_mooncupwaters_cour = [
    [[rpicourport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'MoiseWaters_1', 1]],
    [[rpicourport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'MoiseWaters_2', 1]],
    [[rpicourport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'MoiseWaters_3', 1]],
    [[rpicourport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Butts_1', 1]],
    [[rpicourport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Butts_2', 1]],
    [[rpicourport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Mooncup_1', 1]],
    [[rpicourport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Mooncup_2', 1]],
    [[rpicourport, '/pyta/slide/visible', mooncupwaters_slides, 0], [rpijardinport, '/pyta/slide/visible', 'Mooncup_3', 1]],
]
