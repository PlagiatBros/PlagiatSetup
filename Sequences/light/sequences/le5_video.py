#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *


_mean = [
    ['/pyta/text/0/animate', 'size', 0.15, .55, 0.3],
    ['/pyta/slide/sosfantome/set', 'gif_frame', 0]
]

_mean2 = [
    ['/pyta/text/0/animate', 'size', 0.55, .9, 0.2]
]

_and = None
_ugly = [
    ['/pyta/scene_recall', 'le5_refrain_ugly'],
    ['/pyta/text/2/reset'],
    ['/pyta/text/2/set', 'visible', 1],
    ['/pyta/text/2/set', 'text', 'ugly', 0.5],
    ['/pyta/text/2/set', 'align', 'c b'],
]

_reinit = [
    ['/pyta/scene_recall', 'le5_refrain_mean']
]

le5_refrain_mean = [
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, _and,
    _ugly, None, None, None, _reinit
]

_hey = ['/pyta/scene_recall', 'le5_trap_jesus']
_christ = ['/pyta/post_process/animate', 'fish', 0, -10, 0.3]
_tupac = ['/pyta/scene_recall', 'le5_trap']

le5_trap_jesus = [
    None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, _hey, None, _christ, None,
    _tupac, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None,
]

###########################

def _ah(x):
    return [':/Lightseq/Scene/Play', 'le5_rabza_refrain_word', x]

le5_rabza_refrain_karaoke = [
    [['/pyta/scene_recall', 'le5_rabza_refrain'], _ah('a')], _ah('a'), _ah('i'), _ah('o'), _ah('i'),
    _ah('a'), _ah('u'), _ah('u'), _ah('o'), _ah('i'),

    _ah('e'), _ah('a'), _ah('i'), _ah('o'), _ah('i'),
    _ah('a'), _ah('o'), _ah('u'), _ah('o'), _ah('a'),

    _ah('a'), _ah('a'), _ah('i'), _ah('o'), _ah('e'),
    _ah('e'), _ah('e'), _ah('a'), _ah('o'), _ah('i'),

    _ah('a'), _ah('a'), _ah('i'), _ah('o'), _ah('i'),
    _ah('a'), _ah('a'), _ah('i'), _ah('o'), _ah('i'),
]


le5_theme_danse = [

    [':/Lightseq/Scene/Play', 'le5_theme_danse_rotate'], None, None, None, None

]

le5_mesh_strobe_glitch = [

    None,None,None,None,None,
    None,None,None,None,None,
    None,None,None,None,None,
    None,None,None,None,None,

    None,None,None,None,None,
    None,None,None,None,None,
    None,None,None,None,None,
    None,None,None,None,None,

    None,None,None,None,None,
    None,None,None,None,None,
    None,None,None,None,None,
    None,[':/Lightseq/Scene/Play','le5_mesh_strobe_glitch'],None,None,([[':/Lightseq/Scene/Stop','le5_mesh_strobe_glitch'], [':/Lightseq/Scene/Play','le5_mesh_strobe_glitch_stop']], None, None, None),

]
