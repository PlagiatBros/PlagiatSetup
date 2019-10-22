#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint, normalvariate


_ports = [rpijardinport, rpicourport]
def write(seq, timer, screen=[0,1], text='win32 ERR', font=0, dur=1, mode='b', glitch=0, align=['c', 'c'], pos=[0, 0], size="auto"):
    if type(screen) is not list:
        screen = [screen]
    pos = pos + [0]
    for i in screen:
        seq.send(_ports[i], '/pyta/text/%i/reset' % font)
        seq.send(_ports[i], '/pyta/text/%i/set' % font, 'visible', 1)
        seq.send(_ports[i], '/pyta/text/%i/set' % font, 'align', *align)
        seq.send(_ports[i], '/pyta/text/%i/set' % font, 'position', *pos )
        seq.send(_ports[i], '/pyta/text/%i/set' % font, 'text', text, glitch)

    if dur != 0:
        timer.wait(dur, mode)
        for i in screen:
            seq.send(_ports[i], '/pyta/text/%i/set' % font, 'visible', 0)


def glitch(x=0.8):
    return normalvariate(0, x)> 0.8
