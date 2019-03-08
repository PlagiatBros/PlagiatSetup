#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *
import random

def glitch_timeout(seq, timer):
    timer.wait(random.randint(1,4)/2., 's')
    for port in [rpijardinport,rpicourport]:
        seq.send(port, '/pyta/post_process/active', 0.0)
