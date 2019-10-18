#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint



_look_txt= ["Look", "LOOK", "L00K", "lOoK", "LoOk", "LooK", "l00k", "k00l"]
def dafist_look(seq, timer):
    seq.send('/pyta/text/*/reset')
    ti = str(randint(0,3))
    seq.send('/pyta/slide/white/set', 'noise', 0)
    seq.send('/pyta/text/'+ti+'/set', 'visible', 1)
    seq.send('/pyta/text/'+ti+'/set', 'text', _look_txt[randint(0, len(_look_txt) -1)], 0.2)
    timer.wait(0.04, 's')
    seq.send('/pyta/slide/white/set', 'noise', -50)
    timer.wait(1, 'beat')
    seq.send('/pyta/text/'+ti+'/set', 'visible', 0)


_transebass = False # bouton 8 d'orl -> debut transeload OU drop bass
def dafist_transe_basse_reset(seq, timer):
    global _transebass
    _transebass = False

_tot = 0
def dafist_loading_increment_init(seq, timer):
    global _tot, _transebass
    _tot = 0
    if _transebass:
        # bouton 8 orl -> drop basse avant disco
        seq.send(':/Lightseq/Scene/Play', 'dafist_drop_basse')
    else:
        _transebass = True

def dafist_loading_increment(seq, timer):
    global _tot
    _tot += 1
    if _tot >= 10:
        _tot = 0
        seq.send('/pyta/slide/white/animate', 'scale', '+0', '+0', 1, '+0', 10)
        seq.send('/pyta/slide/smoke_1/animate', 'alpha', '+0', 0.2, 10)
    else:
        seq.send('/pyta/slide/white/animate', 'scale', '+0', '+0', '+.1', '+0', 10)
        seq.send('/pyta/slide/smoke_1/animate', 'alpha', '+0', '+0.01', 10)


def dafist_drop_basse(seq, timer):
    seq.send(rpijardinport, '/pyta/scene_recall', 'dafist_drop_basse_jardin')
    seq.send(rpicourport, '/pyta/scene_recall', 'dafist_drop_basse_cour')
    while True:
        seq.send('/pyta/slide/multiplesdanseuses/set', 'gif_frame', 0)
        seq.send(rpijardinport, '/pyta/slide/multiplesdanseuses/set', 'key_color', 1, 1, 1)
        seq.send(rpicourport, '/pyta/slide/multiplesdanseuses/set', 'key_color', 0, 0, 0)
        timer.wait(2, 'b')
        seq.send(rpijardinport, '/pyta/slide/multiplesdanseuses/set', 'key_color', 0, 0, 0)
        seq.send(rpicourport, '/pyta/slide/multiplesdanseuses/set', 'key_color', 1, 1, 1)
        timer.wait(2, 'b')
