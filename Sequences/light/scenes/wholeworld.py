#encoding: utf-8

import sys
sys.path.append('../Controls/Mididings/')

from ports import *

from random import shuffle


# Intro

def intro_respect(sequencer, timer):

    for port in [rpijardinport, rpicourport]:
        # sequencer.send(port, '/pyta/text/visible', -1, 0)
        sequencer.send(port, '/pyta/text/size', 0, 0.45)
        sequencer.send(port, '/pyta/text/animate', 0, 'size', 0.45, 0.5, 50)
        sequencer.send(port, '/pyta/text/visible', 0, 1)
        sequencer.send(port, '/pyta/text', 0, 'RESPECT')

def intro_urinoir(sequencer, timer):
    timer.wait(2, 's')
    sequencer.send(rpijardinport, '/pyta/text/strobe', 0, 1, 2, 0.3)
    sequencer.send(rpicourport, '/pyta/text/strobe', 0, 1, 2, .4)
    timer.wait(0.4, 's')
    sequencer.send(rpijardinport, '/pyta/text/strobe', 0, 1, 6, 0.8)
    sequencer.send(rpicourport, '/pyta/text/strobe', 0, 1, 4, .7)
    timer.wait(2, 's')
    sequencer.send(rpijardinport, '/pyta/text/strobe', 0, 1, 2, 0.5)
    sequencer.send(rpicourport, '/pyta/text/strobe', 0, 1, 2, .5)

    timer.wait(2, 's')

    sequencer.send(56418, '/pedalBoard/button', 8)

def intro_plagiat(sequencer, timer):

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/text/visible', 0, 0)
        sequencer.send(port, '/pyta/text/size', 2, 0.22)
        sequencer.send(port, '/pyta/text', 2, '[plaʒia]')
        sequencer.send(port, '/pyta/text/strobe', 2, 1, 2, 0.5)
        sequencer.send(port, '/pyta/text/visible', 2, 1)

    timer.wait(1.5, 's')
    sequencer.send(rpijardinport, '/pyta/text/strobe', 2, 0)
    sequencer.send(rpicourport, '/pyta/text/strobe', 2, 0)

    timer.wait(2, 's')
    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/text/visible', 3, 1)
        sequencer.send(port, '/pyta/text/size', 3, 0.08)
        sequencer.send(port, '/pyta/text/align', 3, 'center', 'bottom')
        sequencer.send(port, '/pyta/text', 3, 'faute d\'ordre moral')


# Couplet 1

def wholeworld_jerked_off(sequencer, timer):
    timer.wait(0.75, 'beat')
    sequencer.send(rpijardinport, '/pyta/text/visible', 0, 1)
    sequencer.send(rpijardinport, '/pyta/text/size', 0, 0.5)
    sequencer.send(rpijardinport, '/pyta/text', 0, 'SNIFFED')

    timer.wait(0.5, 'beat')
    sequencer.send(rpijardinport, '/pyta/text/visible', 0, 0)
    sequencer.send(rpicourport, '/pyta/text/visible', 0, 1)
    sequencer.send(rpicourport, '/pyta/text/size', 0, 0.5)
    sequencer.send(rpicourport, '/pyta/text', 0, 'MIXED')

    timer.wait(0.5, 'beat')
    sequencer.send(rpicourport, '/pyta/text/visible', 0, 0)
    sequencer.send(rpijardinport, '/pyta/text/visible', 0, 1)
    sequencer.send(rpijardinport, '/pyta/text', 0, 'EATEN')

    timer.wait(0.5, 'beat')
    sequencer.send(rpijardinport, '/pyta/text/visible', 0, 0)
    sequencer.send(rpicourport, '/pyta/text/visible', 0, 1)
    sequencer.send(rpicourport, '/pyta/text', 0, 'JERKED')

    timer.wait(0.5, 'beat')
    sequencer.send(rpijardinport, '/pyta/text', 0, 'OFF')
    sequencer.send(rpijardinport, '/pyta/text/visible', 0, 1)

    timer.wait(0.25, 'beat')
    sequencer.send(rpijardinport, '/pyta/text', 0, '?')
    sequencer.send(rpicourport, '/pyta/text', 0, '?')
    sequencer.send(rpijardinport, '/pyta/text/strobe', 0, 1, 4, 0.5)
    sequencer.send(rpicourport, '/pyta/text/strobe', 0, 1, 4, 0.5)
    timer.wait(0.25, 'beat')
    sequencer.send(rpijardinport, '/pyta/text', 0, 'JERKED')
    sequencer.send(rpicourport, '/pyta/text', 0, 'OFF')
    sequencer.send(rpijardinport, '/pyta/text/strobe', 0, 1)
    sequencer.send(rpicourport, '/pyta/text/strobe', 0, 1)
    timer.wait(1.5, 'beat')
    sequencer.send(rpijardinport, '/pyta/text/visible', 0, 0)
    sequencer.send(rpicourport, '/pyta/text/visible', 0, 0)


_dark_eyes = " ".join(['FreakyEye_1', 'BlueOnBlackEye_1', 'OrangeOnBlackEye_1', 'OrangeOnBlackEye_2', 'RedOnBlackEye_1'])
_mutt_imgs = ['PencilMutt_1', 'PiedMainMutt_1', 'MangeMutt_1', 'PiedMainMutt_2', 'DegueuMutt_1']
_mutt_imgs_str = " ".join(_mutt_imgs)

def wholeworld_refrain_rough_off(sequencer, timer):

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/slide/alpha', _dark_eyes, 1)
        sequencer.send(port, '/pyta/slide/visible', _mutt_imgs_str, 0)

def wholeworld_refrain_rough(sequencer, timer):
    shuffle(_mutt_imgs)
    pi = ''
    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/slide/alpha', _dark_eyes, 0)
        sequencer.send(port, '/pyta/slide/rgb', _mutt_imgs_str, 1.0, 0, 0)
        sequencer.send(port, '/pyta/slide/animate', _mutt_imgs_str, 'scale_x', 200, 800, 0.3)
        sequencer.send(port, '/pyta/slide/animate', _mutt_imgs_str, 'scale_y', 150, 600, 0.3)
    for i in _mutt_imgs:
        for port in [rpijardinport, rpicourport]:
            if pi:
                sequencer.send(port, '/pyta/slide/visible', pi, 0)
            sequencer.send(port, '/pyta/slide/visible', i, 1)
        timer.wait(1/10.,'b')
        pi = i
    wholeworld_refrain_rough_off(sequencer, timer)

def wholeworld_refrain_snapshat(sequencer, timer):

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/text', 3, '?')
        sequencer.send(port, '/pyta/text/rgb', 3, 255, 255, 255)
        sequencer.send(port, '/pyta/text/size', 3, 0.5)
        sequencer.send(port, '/pyta/text/strobe', 3, 1)
        sequencer.send(port, '/pyta/text/align', 3, 'center', 'right' if port == rpijardinport else 'left')
        sequencer.send(port, '/pyta/text/visible', 3, 1)

    timer.wait(1.5, 'beats')

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/text/visible', 3, 0)


def wholeworld_one_sheet(sequencer, timer):
    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/text', 3, '[uVm]')
        sequencer.send(port, '/pyta/text/rotate_z', 3, 180)
        sequencer.send(port, '/pyta/text/size', 3, 0.2)
        sequencer.send(port, '/pyta/text/rgb', 3, 255, 0, 180)
        sequencer.send(port, '/pyta/text/align', 3, 'center', 'center')
        sequencer.send(port, '/pyta/text/visible', 3, 1)

    timer.wait(4, 'beats')

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/text', 3, '[tu:]')
        sequencer.send(port, '/pyta/text/rotate_z', 3, 0)
        sequencer.send(port, '/pyta/text/size', 3, 0.25)
        sequencer.send(port, '/pyta/text/rgb', 3, 255, 0, 180)
        sequencer.send(port, '/pyta/text/align', 3, 'center', 'center')
        sequencer.send(port, '/pyta/text/visible', 3, 1)


    timer.wait(4, 'beats')

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/text', 3, '[øri:]')
        sequencer.send(port, '/pyta/text/rotate_z', 3, 0)
        sequencer.send(port, '/pyta/text/size', 3, 0.3)
        sequencer.send(port, '/pyta/text/rgb', 3, 255, 0, 180)
        sequencer.send(port, '/pyta/text/align', 3, 'center', 'center')
        sequencer.send(port, '/pyta/text/visible', 3, 1)



    timer.wait(4, 'beats')

    for port in [rpijardinport, rpicourport]:
        sequencer.send(port, '/pyta/text', 3, '::')
        sequencer.send(port, '/pyta/text/rotate_z', 3, 0)
        sequencer.send(port, '/pyta/text/size', 3, 0.35)
        sequencer.send(port, '/pyta/text/rgb', 3, 255, 0, 180)
        sequencer.send(port, '/pyta/text/align', 3, 'center', 'center')
        sequencer.send(port, '/pyta/text/visible', 3, 1)

    for i in range(1,8):
        for port in [rpijardinport, rpicourport]:
            sequencer.send(port, '/pyta/text/strobe', 3, 1, 128 / (i*i) , 0.5)
        timer.wait(0.5, 'b')
