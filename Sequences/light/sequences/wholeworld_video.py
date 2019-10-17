#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *


_refrain_rough = [
    ['/pyta/slide/eyes_2/set', 'alpha', 0.1],

    ['/pyta/slide/mutt_1/set', 'visible', 1],
    ['/pyta/slide/mutt_1/set', 'position_z', -1],
    ['/pyta/slide/mutt_1/set', 'gif_frame', 0],
    ['/pyta/slide/mutt_1/set', 'gif_speed', 1.5],
    ['/pyta/slide/mutt_1/animate', 'zoom', 0, 1, 0.7, 'exponentialout'],
]

_refrain_rough_off = [
    ['/pyta/slide/eyes_2/set', 'alpha', 0.8],
    ['/pyta/slide/mutt_1/set', 'visible', 0],
]

_refrain_snapchat = [
    ['/pyta/slide/eyes_2/set', 'invert', 1],
    ['/pyta/slide/eyes_2/set', 'gif_speed', 4],

    ['/pyta/text/4/set', 'visible', 1]
    ['/pyta/text/4/set', 'text', '?']
    ['/pyta/text/4/set', 'noise', -10]

]

_refrain_snapchat_off = [
    ['/pyta/text/4/set', 'visible', 0]
    ['/pyta/slide/eyes_2/set', 'invert', 0],
    ['/pyta/slide/eyes_2/set', 'gif_speed', 1],
]

wholeworld_refrain = [
    _refrain_snapchat_off + _refrain_rough, _refrain_rough_off, None, None,
    _refrain_rough, _refrain_rough_off, _refrain_snapchat, None,
]
