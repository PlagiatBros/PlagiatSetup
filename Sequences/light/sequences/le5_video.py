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
_ugly = None

le5_refrain_mean = [
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, None,
    _mean, None, _mean2, None, _and,
    _ugly, None, None, None, None
]
