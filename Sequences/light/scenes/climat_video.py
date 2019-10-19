#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint, random, shuffle, choice

def climat_intro(seq, timer):
    seq.send(rpijardinport, '/pyta/slide/moise_1/set', 'rotate_y', 180)

_mwords = {
    0: ['win32 error'],
    1: ['Gran Mounouté', 'Grand Moumouté ?', 'Wizzzdom', 'Grand Mère sait faire\n un bon café ?', 'Kond0m'],
    2: ['Dingité', 'Dingle Dongle', 'Infirmité', 'Soirée Infirmier.e.s ???' ],
    3: ['Éternité', 'Enuclée', 'NUclear Weap', 'Zzzzzz', '?? ZnuKzz']
}
_mbacks = ['Kwakwa', 'Mandalaa', 'Mendicité', 'Mamacito', 'Gnagnagna', 'lälalA', 'Vend 06 12 7 20 20']

def climat_mandela_subs(seq, timer, x=0):
    words = [choice(_mwords[x]), choice(_mbacks)]
    ports = [rpijardinport, rpicourport]
    shuffle(ports)
    for i in range(2):
        seq.send(ports[i], '/pyta/text/0/reset')
        seq.send(ports[i], '/pyta/text/0/set', 'visible', 1)
        seq.send(ports[i], '/pyta/text/0/set', 'text', words[i], 1)
    timer.wait(5, 's')
    seq.send('/pyta/text/0/set', 'visible', 0)





def climat_precouplet(seq, timer):
    seq.send(rpijardinport, '/pyta/slide/{reptilianeye_1,moise_1,moise_3}/set', 'rotate_y', 180)


def climat_precouplet_moise_flash(seq, timer):
    seq.send('/pyta/slide/moise_1/animate', 'alpha', 1, 0, 4*60./seq.bpm, "exponentialout")

def climat_precouplet_moise_flash2(seq, timer):
    seq.send('/pyta/slide/moise_3/animate', 'alpha', 1, 0, 4*60./seq.bpm, "exponentialout")


def climat_wobble_strobe(seq, timer, subdivision=0):
    if subdivision == 0:
        seq.send('/pyta/post_process/recall', 'climat_wobble_strobe')
        seq.send(':/Lightseq/Scene/Play', 'climat_theme_strobelights_jeannot', 0)
    else:
        if subdivision == 32:
            subdivision = 3/2.
        seq.send('/pyta/post_process/save', 'climat_wobble_strobe')
        seq.send('/pyta/post_process/reset')
        seq.send('/pyta/post_process/set', 'visible', 1)
        seq.send('/pyta/post_process/set', 'rgbwave', 0.3)
        seq.send('/pyta/post_process/strobe', 'invert', 1, 0, 60./seq.bpm/subdivision, 0.5)
        seq.send(':/Lightseq/Scene/Play', 'climat_theme_strobelights_jeannot', 1)


def climat_precouplet_dimmer(seq, timer):
    seq.send('/pyta/post_process/set', 'visible', 1)
    seq.send('/pyta/post_process/strobe_stop')
    seq.send('/pyta/post_process/animate', 'color', 0.5, 0.5, 0.5, 0.4, 0, 0.2, 2)


def climat_refrain_bardanse(seq, timer):
    bars = range(0,5)
    shuffle(bars)
    for i in range(0, randint(1,4)):
        seq.send('/pyta/slide/white%i/animate' % bars[i], 'rotate_x', 0, 180, 60./seq.bpm * 2)



_boutros = ['BOUTROS', 'MUtRos3' ,'GloUBros', 'ShuKrOss', 'BouTroS']
def climat_boutros_cut(seq, timer):
    seq.send('/pyta/clone', 'white', 'whiteboutros')
    seq.send('/pyta/slide/whiteboutros/reset')
    for i in range(0,8):
        seq.send('/pyta/post_process/save', 'boutros')
        seq.send('/pyta/post_process/reset')
        seq.send('/pyta/slide/whiteboutros/strobe', 'alpha', 0.2, 1, 0.08, 0.5)
        seq.send('/pyta/slide/whiteboutros/set', 'visible', 1)
        seq.send('/pyta/slide/whiteboutros/set', 'position_z', -50)
        seq.send('/pyta/text/0/reset')
        seq.send('/pyta/text/0/set', 'visible', 1)
        seq.send('/pyta/text/0/set', 'color', 0,0,0)
        seq.send('/pyta/text/0/set', 'text', _boutros[randint(0,len(_boutros)-1)])
        timer.wait(1, 'b')
        seq.send('/pyta/slide/whiteboutros/set', 'visible', 0)
        seq.send('/pyta/text/0/set', 'visible', 0)
        seq.send('/pyta/post_process/recall', 'boutros')
        timer.wait(1, 'b')



def climat_mandela_danse(seq, timer):
    seq.send(rpijardinport, '/pyta/post_process/set', 'rotate_y', 180)
