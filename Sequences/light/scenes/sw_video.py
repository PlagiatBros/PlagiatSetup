#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from video_functions import *

def no_budget_andra(seq, timer):
    write(seq, timer, 0, text='dans l\'attente d\'une subvention\nde l\'andra et, nous vous prions', glitch=5, dur=20)
    write(seq, timer, 1, text='de t\'imaginer un voyage pédagoqique\net de one million d\'années au coeur\nde galerie mordorée à l\'automne de printanières\nsensations à la droite éxtrême du spectre qui\nvous inviterai' , glitch=5, dur=20)

def no_budget_pastis(seq, timer):
    write(seq, timer, 0, text='un pastis d\'iode ?', glitch=0.5, dur=1)
    timer.wait(1, 's')
    write(seq, timer, 1, text='La vie c com un tractopel', glitch=0.5, dur=1)
    timer.wait(1, 's')
    write(seq, timer, 2, text='Pa bezo1 de permit\'', glitch=0.5, dur=1)
