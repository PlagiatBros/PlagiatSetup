#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *


_refrain_rough = [
    ['/pyta/slide/eyes_2/set', 'alpha', 0.1],
    ['/pyta/slide/eyes_2/set', 'noise', 0],

    ['/pyta/slide/mutt_1/set', 'visible', 1],
    ['/pyta/slide/mutt_1/set', 'position_z', -1],
    ['/pyta/slide/mutt_1/set', 'gif_frame', 0],
    ['/pyta/slide/mutt_1/set', 'gif_speed', 1.5],
    ['/pyta/slide/mutt_1/animate', 'zoom', 0, 1.5, 0.7, 'exponentialout'],

    ['/pyta/slide/ronmcdo/set', 'alpha', 0],
    ['/pyta/slide/montypythonsoldathubert/set', 'alpha', 0]
]

_refrain_rough_off = [
    ['/pyta/slide/eyes_2/set', 'alpha', 0.8],
    ['/pyta/slide/mutt_1/set', 'visible', 0],
]

_refrain_snapchat = [
    ['/pyta/slide/eyes_2/set', 'charcoal', 2],
    ['/pyta/slide/eyes_2/set', 'zoom', 3],
    ['/pyta/slide/eyes_2/strobe', 'alpha', 0, 1, 0.08, 0.5],

    ['/pyta/text/3/reset'],
    ['/pyta/text/3/set', 'visible', 1],
    ['/pyta/text/3/set', 'text', '?'],
    ['/pyta/text/3/set', 'rgbwave', 0],
    ['/pyta/text/3/set', 'noise', -10],

]

_refrain_snapchat_invert = [
    ['/pyta/slide/eyes_2/set', 'noise', -10],
    ['/pyta/text/3/set', 'noise', -2],
    ['/pyta/text/3/set', 'rgbwave', 0.2],
]

_refrain_snapchat_off = [
    ['/pyta/text/3/set', 'visible', 0],
    ['/pyta/slide/eyes_2/set', 'charcoal', 0],
    ['/pyta/slide/eyes_2/set', 'zoom', 2],
    ['/pyta/slide/eyes_2/strobe_stop', 'alpha'],
    # ['/pyta/slide/eyes_2/set', 'gif_speed', 1],
]

_indien = ['/pyta/slide/montypythonsoldathubert/set', 'alpha', 1]

_cowboy = ['/pyta/slide/ronmcdo/set', 'alpha', 1],

wholeworld_refrain = [
    _refrain_rough, _refrain_rough_off, None, None,
    None, None, (_refrain_snapchat, None, _refrain_snapchat_invert, None, _refrain_snapchat_off), _indien,
    _refrain_rough, _refrain_rough_off, None, None,
    None, None, (_refrain_snapchat, None, _refrain_snapchat_invert, None, _refrain_snapchat_off), _cowboy,
]


wholeworld_refrain_eyes_jardin = [
    [rpijardinport, '/pyta/slide/eyes_2/set', 'gif_frame', x] for x in range(4)
]
wholeworld_refrain_eyes_cour = [
    [rpicourport, '/pyta/slide/eyes_2/set', 'gif_frame', x] for x in range(4)
]
