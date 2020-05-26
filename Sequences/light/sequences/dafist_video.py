#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import random


## refrain

def _on():
    return [
        ['/pyta/slide/goatz/set', 'visible', 1],
        ['/pyta/slide/goatz/animate', 'scale', 0.8, 0.8, random() + 0.8, random()/2 + 0.8, 0.1 ],
    ]

_off = [
    ['/pyta/slide/goatz/set', 'visible', 0],
]

_glitch = [
    ['/pyta/post_process/set', 'visible', 1],
    ['/pyta/post_process/animate', 'fish', 0, -20, 1],
]

_glitch_off = [
    ['/pyta/post_process/set', 'visible', 0],
    ['/pyta/post_process/set', 'fish', 0],
    ['/pyta/post_process/animate_stop', 'fish'],
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


# _blast_on = [
#     ['/pyta/post_process/strobe', 'invert', 0, 1, 0.08, 0.5]
# ]
# _blast_off = [
#     ['/pyta/slide/souleyman/stop_strobe', 'invert'],
#     ['/pyta/slide/souleyman/set', 'invert', 0]
# ]
#
#
# dafist_refrain_blast = [
#     (_blast_on, _blast_off, None, None), (_blast_on, _blast_off, None, None), (None, _blast_on, _blast_off, None), (None, _blast_on, _blast_off, None),
#     (None, None, None ,_blast_on), (_blast_off, _blast_on, _blast_off, None), (None, _blast_on, _blast_off, None), (None, None, None ,_blast_on),
#     (_blast_off, _blast_on, _blast_off, None), None, (None, _blast_on, _blast_off, None), (None, _blast_on, _blast_off, None),
#     (None, None, None ,_blast_on), (_blast_off, _blast_on, _blast_off, None), (_blast_on, _blast_off, _blast_on, _blast_off, _blast_on, _blast_off), (_blast_on, _blast_off, None, None, None, None),
#
#     (_blast_on, _blast_off, None, None), (_blast_on, _blast_off, None, None), (None, _blast_on, _blast_off, None), (None, _blast_on, _blast_off, None),
#     (None, None, None ,_blast_on), (_blast_off, _blast_on, _blast_off, None), (None, _blast_on, _blast_off, None), (None, None, None ,_blast_on),
#     (_blast_off, _blast_on, _blast_off, None), (None, None, None, _blast_on + _glitch), None, (_blast_off + _glitch_off, _blast_on, _blast_off, None),
#     (None, None, None ,_blast_on), (_blast_off, _blast_on, _blast_off, None), (_blast_on, _blast_off, _blast_on, _blast_off, _blast_on, _blast_off), (_blast_on, _blast_off, None, None, None, None),
# ]

## pre Refrain


dafist_prerefrain_zoom = [
    ['/pyta/text/2/animate', 'zoom', 1, 1.2, 0.12],
    None, None, None
]

dafist_prerefrain = [
    [['/pyta/text/2/set', 'text', 'YE$'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text/2/set', 'text', 'ZøøM3'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text/2/set', 'text', 'ye$$$'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text/2/set', 'text', 'Lâ$T'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text/2/set', 'text', 'yyYEs$'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text/2/set', 'text', 'ZoN'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text/2/set', 'text', 'ye$$$$'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
    [['/pyta/text/2/set', 'text', 'Smurf'], ['/pyta/text/2/set', 'visible', 1]], ['/pyta/text/2/set', 'visible', 0], None, None,
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
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.01],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.02],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.03],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.04],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.05],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.06],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.07],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.08],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.09],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.1],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.11],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.12],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.13],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.14],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.15],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.16],
    ['/pyta/slide/'+mooncupwaters_slides+'/set', 'alpha', 0.05 + 0.17],
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

## pdiddy

dafist_couplet_ragga_pdiddz = [
    ['/pyta/slide/pddz/animate', 'zoom', 1, 1.2, 0.2]
]

## disco

_transe_off = [
    ['/pyta/slide/dansefrenetique/animate', 'fish', 0, -20, 0.8],
]

_transe_on = [
    ['/pyta/slide/dansefrenetique/animate', 'fish', -20, 0, 0.45],
]

dafist_transe_cutoff = [
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, (_transe_off , None, None, None), None, (_transe_on, None),
]

dafist_transe_roll_jardin = [
    [
        [rpijardinport, '/pyta/slide/dansefrenetique/animate', 'rotate_x', 0, 1080, 2.5, 'exponentialout']
    ],
    [
        [rpijardinport, '/pyta/slide/dansefrenetique/animate', 'rotate_x', 0, -1080, 2.5, 'exponentialout']
    ],
    None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
]
dafist_transe_roll_cour = [
    [
        [rpicourport, '/pyta/slide/dansefrenetique/animate', 'rotate_x', 0, 1080, 2.5, 'exponentialout']
    ], None, None, None,
    [
        [rpicourport, '/pyta/slide/dansefrenetique/animate', 'rotate_x', 0, 1440, 2.2, 'exponentialout']
    ], None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
]
