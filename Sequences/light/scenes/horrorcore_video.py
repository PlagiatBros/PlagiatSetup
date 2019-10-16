#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import normalvariate, randint

def horrorcore_mooncup_glitch(seq, timer):
    while True:
        deviation = normalvariate(0, 0.5)
        if deviation > 0.8:
            deviation = 1
        else :
            deviation = deviation / 100

        seq.send(rpijardinport, '/pyta/slide/mooncup_1/set', 'rgbwave', deviation)
        seq.send(rpicourport, '/pyta/slide/mooncup_1/set', 'rgbwave', deviation)
        timer.wait(0.01, 's')

def horrorcore_stupidDonkeys_trigger(seq, timer):
    # du fait qu'on appuie n'importe quand
    seq.send(":/Lightseq/Sequence/Enable", "horrorcore_stupidDonkeys")
    timer.wait(8, 'b')
    seq.send(":/Lightseq/Sequence/Disable", "horrorcore_stupidDonkeys")

def horrorcore_mooncup_obama(seq, timer):
    paths = ['hilary_1', 'obama_1']
    while True:
        for port in [rpijardinport, rpicourport]:
            seq.send(port, '/pyta/slide/{' + ','.join(paths) + '}/set', 'visible', 0)

        seq.send(rpijardinport, '/pyta/slide/' + paths[randint(0,len(paths)-1)] + '/set', 'visible', 1)
        seq.send(rpicourport, '/pyta/slide/' + paths[randint(0, len(paths)-1)] + '/set', 'visible', 1)

        timer.wait(3, 'b')



def horrorcore_autruche_glitch(seq, timer):
    while True:
        deviation = normalvariate(0, 0.5)
        if deviation > 0.8:
            deviation = 4
        else :
            deviation = 0

        seq.send(rpicourport, '/pyta/slide/autruch*/set', 'charcoal', deviation)
        seq.send(rpicourport, '/pyta/slide/autruch*/set', 'invert', deviation)

        timer.wait(0.1, 's')

_lyrics = [

]
def horrorcore_lyrics_glitch(seq, timer):
    while True:
        seq.send(rpicourport, '/pyta/text/0/set', 'alpha', 0)
        seq.send(rpicourport, '/pyta/text/0/set', 'alpha', 0)
        deviation = normalvariate(0, 0.5)
        if deviation > 0.8:
            port = [rpicourport, rpijardinport][random.randint(0, 1)]
            seq.send(port, '/pyta/text/0/set', 'alpha', 1)
            seq.send(port, '/pyta/text/0/set', 'text', _lyrics[random.randint(0, len(_lyrics) - 1)])


        timer.wait(0.1, 's')
