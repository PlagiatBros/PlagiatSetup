#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import normalvariate, randint, random

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
    paths = ['hilary_1', 'obama_1', 'Noumeen', 'RonMcDo', 'JohnCleeseLangue']
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
  'yep', 'trus ya mom', 'cheat u wife', 'u no nice',
  'aint no\nsingula singa', '   con\ncrete\npooo   ',
  'YOUR DOG', 'naked st phal', '  picasso\naintno\npope  ',
  'Vend BX millesime,\napl au 7 20 20\noffre sérieuse s\'abstinente'
]
def horrorcore_lyrics_glitch(seq, timer):
    while True:
        seq.send(rpicourport, '/pyta/text/*/set', 'alpha', 0)
        seq.send(rpijardinport, '/pyta/text/*/set', 'alpha', 0)

        deviation = normalvariate(0, 0.5)
        if deviation > 0.8:
            port = [rpicourport, rpijardinport][randint(0, 1)]
            t = randint(0,3)
            txt = _lyrics[randint(0, len(_lyrics) - 1)]
            seq.send(port, '/pyta/text/'+str(t)+'/set', 'alpha', 1)
            seq.send(port, '/pyta/text/'+str(t)+'/set', 'text', txt, 0.5)
            timer.wait(0.1 * len(txt), 's')

        else:
            timer.wait(0.1, 's')


def horrorcore_messe_christ(seq, timer):
    seq.send(rpicourport, '/pyta/slide/christ_2/animate', 'key_threshold', 1.1, 0, 100)
    seq.send(rpijardinport, '/pyta/slide/christ_4/animate', 'key_threshold', 1.1, 0, 90)
    timer.wait(5, 's')
    seq.send(rpicourport, '/pyta/text/*/animate', 'alpha', 1, 0, 1, 'sine')
    seq.send(rpijardinport, '/pyta/text/*/animate', 'alpha', 1, 0, 1, 'sine')



def horrorcore_disco_christ(seq, timer):
    seq.send(rpicourport, '/pyta/slide/christ_3/animate', 'alpha', 0, 1, 60)
    seq.send(rpijardinport, '/pyta/slide/christ_3/animate', 'alpha', 0, 1, 60)
    timer.wait(60, 's')
    for port in [rpijardinport, rpicourport]:
        seq.send(port, '/pyta/post_process/set', 'visible', 1)
        seq.send(port, '/pyta/post_process/strobe', 'invert', 0, 1, 0.16, 0.5)

def horrorcore_drop_merde(seq, timer):
    while True:
        port = [rpijardinport, rpicourport][randint(0,1)]
        seq.send(port, '/pyta/slide/merdehd/set', 'alpha', 1)
        x, y = [random()/2.-0.25, random()/4.+0.25]
        seq.send(port, '/pyta/slide/merdehd/animate', 'position', random()-0.5, random()-0.5, 0, x, y, 0, 0.3, 'sine')
        seq.send(port, '/pyta/slide/merdehd/animate', 'zoom', 1, 0, 0.4, 'sine')
        timer.wait(0.3, 's')
        if abs(x) < 0.1 and y < 0.8:
            seq.send(port, '/pyta/slide/mecdansefondvert/animate', 'color', 1, 0.25, 0.25, 0.5, 0.5, 0.5, 0.2, 'sine')
            seq.send(port, '/pyta/slide/mecdansefondvert/animate', 'rgbwave', 0.8, 0, 0.2, 'sine')
