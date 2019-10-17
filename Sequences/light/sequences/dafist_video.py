#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import random


## refrain

def _on():
    return [
        ['/pyta/slide/goatz/set', 'visible', 1],
        ['/pyta/slide/goatz/animate', 'scale', 0.8, 0.8, random()/2 + 0.8, random()/2 + 0.8, 0.1 ],
    ]

_off = [
    ['/pyta/slide/goatz/set', 'visible', 0],
]

_glitch = [
    ['/pyta/post_process/animate', 'fish', 0, -20, 1],
]

_glitch_off = [
    ['/pyta/post_process/set', 'fish', 0],
]

dafist_refrain = [
    (_on(), _off, None, None), (_on(), _off, None, None), (None, _on(), _off, None), (None, _on(), _off, None),
    (None, None, None ,_on()), (_off, _on(), _off, None), (None, _on(), _off, None), (None, None, None ,_on()),
    (_off, _on(), _off, None), None, (None, _on(), _off, None), (None, _on(), _off, None),
    (None, None, None ,_on()), (_off, _on(), _off, None), (_on(), _off, _on(), _off, _on(), _off), (_on(), _off, None, None, None, None),

    (_on(), _off, None, None), (_on(), _off, None, None), (None, _on(), _off, None), (None, _on(), _off, None),
    (None, None, None ,_on()), (_off, _on(), _off, None), (None, _on(), _off, None), (None, None, None ,_on()),
    (_off, _on(), _off, None), (None, None, None, _on() + _glitch), None, (_off + _glitch_off, _on(), _off, None),
    (None, None, None ,_on()), (_off, _on(), _off, None), (_on(), _off, _on(), _off, _on(), _off), (_on(), _off, None, None, None, None),
]


## pre Refrain

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


## mooncupwaters

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
