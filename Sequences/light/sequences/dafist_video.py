#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import random

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
