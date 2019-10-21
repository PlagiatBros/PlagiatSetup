#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from video_functions import *
from random import random, shuffle, randint


def le5_intro(seq, timer):
    write(seq, timer, 0, 'RESPECTE\nPOUISSANCE', 0, 0)
    write(seq, timer, 1, 'LAAA\nPAPAAL', 0, 0)
    seq.send('/pyta/text/0/set', 'size', 0.3)
    seq.send('/pyta/text/0/animate', 'alpha', 0, 0.6, 10)

def le5_couplet1(seq, timer, level=1):
    if level == 1:
        seq.send('/pyta/slide/illuminati2/set', 'alpha', 0.2)
    elif level == 2:
        seq.send('/pyta/slide/illuminati2/set', 'alpha', 0.25)
    elif level == 3:
        seq.send('/pyta/post_process/reset')
        seq.send('/pyta/post_process/set', 'visible', 1)
        t = 60./seq.bpm*15*5
        seq.send('/pyta/slide/illuminati2/animate', 'alpha', 0.25, 0.9, t, 'exponentialin')
        seq.send('/pyta/slide/christcross_1/animate', 'alpha', 0.25, 0.75)
        seq.send('/pyta/slide/christcross_1/animate', 'noise', 0, -20, 'exponentialin')
        timer.wait(t, 's')
    elif level == 4:
        seq.send('/pyta/slide/illuminati/set', 'gif_speed', 3)


_niglou = ['Niglou', 'Niggah', 'Nigrid', 'iNgrid', 'Nigroo', 'Nicole'] * 5
_niglou_text = '\ndon\'t you know it ain\'t\n\
no heavy duty too heavy\n\
for Mi$$y $chneck One-Two?'
shuffle(_niglou)

def le5_niglou(seq, timer):
    for n in _niglou:
        write(seq, timer, text=n + _niglou_text, dur=random(), align=['c', 'b'], pos=[0, 0.1])
    write(seq, timer, text='Niggah' + _niglou_text, dur=0, align=['c', 'b'], pos=[0, 0.1])



_words = ['DO YOU', 'USE', 'KREWZ', 'KNTRL?']
_i = 0
def le5_trapcup(seq, timer):
    global _i
    seq.send('/pyta/slide/white/reset')
    seq.send('/pyta/slide/white/set', 'visible', 1)
    seq.send('/pyta/slide/white/strobe', 'color', 1,1,1, 0,0,0, 0.08, 0.5)
    seq.send('/pyta/slide/white/set', 'position_z', -10)
    seq.send('/pyta/text/0/reset')
    seq.send('/pyta/text/0/set', 'visible', 1)
    seq.send('/pyta/text/0/strobe', 'color', 0,0,0, 1,1,1, 0.08, 0.5)
    seq.send('/pyta/text/0/set', 'text', _words[_i%len(_words)])
    _i += 1
    timer.wait(0.75, 'b')
    seq.send('/pyta/slide/white/set', 'visible', 0)
    seq.send('/pyta/text/0/set', 'visible', 0)

####################################


_time = 240
def _showtime(seq):
    global _time
    m = _time / 60
    s = _time - m * 60
    sm = str(m) if m > 9 else  '0' + str(m)
    ss = str(s) if s > 9 else  '0' + str(s)
    seq.send(rpicourport, '/pyta/text/2/set', 'text', '%s:%s' % (sm, ss))

_mode = -1
def le5_ballade_timer(seq, timer, reset=0):
    global _time, _mode
    if reset:
        _mode = -1
        _time = 240

    _mode = (_mode + 1) % 3
    while True:
        if _mode == 0: #normal
            _time = _time - 1
        elif _mode == 1: #reverse
            _time = _time + 1
        elif _mode == 2: #random
            _time = _time + randint(-10, 84)
        _showtime(seq)
        timer.wait(1, 's')


####################################

_refrain = 1
def le5_rabza_refrain_disable(seq, timer):
    global _refrain
    _refrain = 0

def le5_rabza_refrain_switcher(seq, timer):
    global _refrain
    if _refrain == 1:
        seq.send(':/Lightseq/Sequence/Enable', 'le5_rabza_refrain_karaoke')
    else:
        _refrain = 1
        seq.send('/pyta/text/0/set', 'visible', 0)
        seq.send('/pyta/slide/white/set', 'visible', 0)


_ono = {
    'a': ['ah', 'aie', 'bla', 'haa', 'ahh', 'ja', 'raaa', 'bag'],
    'i': [' ***ing ', '*ing', 'bing', 'ding', 'mouick', 'couic', 'chips', 'jeez'],
    'o': ['word', 'ohh', 'coke', 'god', 'dog', 'dong', 'donkey'],
    'u': ['bus', 'wuss', 'nuts', 'guts', 'plug', 'butter'],
    'e': ['tell', 'hell', 'damn', 'hey', 'dang', 'pain']
}
_latest = ''
def le5_rabza_refrain_word(seq, timer, o):
    global _latest
    words = _ono[o]
    word = -1
    while word == -1 or word == _latest:
        word = words[randint(0, len(words)-1)]
    _latest = word
    seq.send('/pyta/text/0/set', 'visible', 1)
    seq.send('/pyta/text/0/set', 'text', word, 0.1)
    seq.send('/pyta/text/0/animate', 'size', 0.25, 0.35, 0.1, 'sine')
    seq.send('/pyta/slide/white/animate', 'position_y', 0.25, 0.35, 0.25, -1, 'circularout')
    seq.send('/pyta/slide/white/animate', 'scale', 0.14, 0.08, 0.1, 0.1, 0.25, -1, 'exponentialout')


def le5_theme_danse_rotate(seq, timer):
    seq.send('/pyta/slide/1344*/set', 'rotate_y', '+180')
    seq.send('/pyta/slide/1344*/set', 'gif_frame', 0)



def le5_mesh_up(seq, timer):
    seq.send('/pyta/slide/tournesurlatete/animate', 'fish', '+0', '/3', 5)
    seq.send('/pyta/slide/tournesurlatete/animate', 'noise', '+0', '/3', 5)


def le5_mesh_strobe(seq, timer):
    seq.send('/pyta/slide/tournesurlatete/set', 'fish', 0)
    seq.send('/pyta/slide/tournesurlatete/set', 'noise', 0)


def le5_mesh_strobe_glitch(seq, timer):
    t = 3 * 60./seq.bpm
    seq.send('/pyta/post_process/animate', 'rgbwave', 0, 0.6, t)
    seq.send('/pyta/post_process/animate', 'fish', 0, 2, t)
    seq.send('/pyta/post_process/animate', 'zoom', 1, 1.5, t)


def le5_mesh_strobe_glitch_stop(seq, timer):
    t = 3/4. * 60./seq.bpm
    seq.send('/pyta/post_process/animate', 'rgbwave', 0.5, 0, t, 'exponentialin')
    seq.send('/pyta/post_process/animate', 'fish', 2, 0, t, 'exponentialin')
    seq.send('/pyta/post_process/animate', 'zoom', 1.5, 1, t, 'exponentialin')


_loubs = ['Instoubolu','Instoublou','Instoulbou','Instolubuo','Instlouubo','Insltouubo','Inlstuouob','Ilnsutooub','Linustoubo','Lunistobou','Loutsoubou','Loubinstou','Loubisnotu','Loubsiontu','Loubointon','Louboutsoin','Loubotchoin']
def le5_louboutin_words(seq, timer):
    seq.send('/pyta/text/0/reset')
    seq.send('/pyta/post_process/reset')
    seq.send('/pyta/post_process/set', 'visible', 1)
    seq.send('/pyta/text/0/set', 'visible', 1)
    seq.send('/pyta/text/0/set', 'size', 0.25)
    seq.send('/pyta/text/0/set', 'text', 'Instouboul', 0.1)
    seq.send('/pyta/post_process/set', 'rgbwave', 0.2)
    timer.wait(2, 's')
    for word in _loubs:
        seq.send('/pyta/post_process/set', 'rgbwave', 0.5 if glitch(0.7) else 0.2)
        seq.send('/pyta/text/0/set', 'text', word, 0.2)
        timer.wait(0.3, 's')
    timer.wait(1, 's')
    seq.send('/pyta/text/0/set', 'text', 'L\'ouboutain', 0.3)
    seq.send('/pyta/post_process/animate', 'rgbwave', 0.2, 0, 0.3)
    timer.wait(4, 's')
    seq.send('/pyta/text/0/animate', 'position_y', '+0', -1, 4)
    seq.send('/pyta/text/0/animate', 'fish', 0, 2, 6)

    seq.send(rpijardinport, '/pyta/slide/louboutin_1/animate', 'alpha', 0, 1, 4)
    seq.send(rpijardinport, '/pyta/slide/louboutin_1/set', 'visible', 1)
    seq.send(rpijardinport, '/pyta/slide/louboutin_1/position', 0.2, -0.4, 0)
    seq.send(rpijardinport, '/pyta/slide/louboutin_1/zoom', 1.8)

    seq.send(rpicourport, '/pyta/slide/louboutin_1/animate', 'alpha', 0, 1, 4)
    seq.send(rpicourport, '/pyta/slide/louboutin_1/set', 'visible', 1)
    seq.send(rpicourport, '/pyta/slide/louboutin_1/position', 0.2, 0.2, 0)
    seq.send(rpicourport, '/pyta/slide/louboutin_1/zoom', 1.4)
