#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint
from time import sleep
from math import exp, log, pi, sin



#### CREPITEMENT LUMINEUX
def crepitement(seq, timer, args):
    # bars, colors et segments suivant syntaxe OSC
    while True:
        for i in range(0,len(args)):
            bars, colors, segments, cmin, cmax = args[i]
            seq.send(qlcport, '/'+bars+'/'+colors+'/Segment/'+segments, randint(cmin, cmax))
        timer.wait(0.01, 's')


### STROBE
def strobelights(seq, timer, bars, colors, segments, mode, ramped = None, step = 0.1, alea_type = ['segment', 1]):
    # mode = together | aleatoire : tous les segments ensemble / segments au hasard
    # ramped = [min, max, duration] : rampe d'intensité
    # alea_type = [bar, nb_bar] | [color, nb_color] | [segment, nb_segment] | [tutti, nb_bar, nb_color, nb_segment]

    path = '/'+str(bars)+'/'+str(colors)+'/Segment/'+str(segments)
    path = path.replace('[', '{').replace(']', '}').replace(' ', '')

    if segments == "All":
        segments = range(1, 9)

    if ramped is not None:
        mino, maxo, duration = ramped
        coef = float(maxo-mino)/duration
        boef = mino

    i = 0
    while True:
        if ramped is not None:
            dimmer = int(coef * i * step + boef)

            if dimmer > 255:
                dimmer = 255
            elif dimmer < 0:
                dimmer = 0
        else:
            dimmer = 255

        if mode == 'together':
            seq.send(qlcport, path, dimmer)

        elif mode == 'aleatoire':
            if alea_type[0] == 'segment':
                seg = []
                for s in range(0,alea_type[1]):
                    seg.append(segments[randint(0,len(segments)-1)])
                path = '/'+str(bars)+'/'+str(colors)+'/Segment/'+str(seg)


            elif alea_type[0] == 'bar':
                bar = []
                for b in range(0,alea_type[1]):
                    bar.append(bars[randint(0,len(bars)-1)])
                path = '/'+str(bar)+'/'+str(colors)+'/Segment/'+str(segments)


            elif alea_type[0] == 'color':
                color = []
                for c in range(0,alea_type[1]):
                    color.append(colors[randint(0,len(colors)-1)])
                path = '/'+str(bars)+'/'+str(color)+'/Segment/'+str(segments)

            elif alea_type[0] == 'tutti':
                nb_bar = alea_type[1]
                nb_color = alea_type[2]
                nb_segment = alea_type[3]
                bar = []
                for b in range(0,nb_bar):
                    bar.append(bars[randint(0,len(bars)-1)])

                color = []
                for c in range(0,nb_color):
                    color.append(colors[randint(0,len(colors)-1)])
                seg = []
                for s in range(0,nb_segment):
                    seg.append(segments[randint(0,len(segments)-1)])

                path = '/'+str(bar)+'/'+str(color)+'/Segment/'+str(seg)

            path = path.replace("'", "").replace('[', '{').replace(']', '}').replace(' ', '')
            seq.send(qlcport, path, dimmer)
        
        sleep(step/2)
        seq.send(qlcport, path, 0)
        sleep(step/2)

        i = i+1

# EXAMPLES
# def testStrobe(seq, timer):
#     strobelights(seq, timer, 'Tutti', 'White', 'All', 'aleatoire', ramped = [0, 255, 10] ,alea_type = ['segment', 3] )

# def testStrobeBar(seq, timer):
#     strobelights(seq, timer, ['ProcheJardin','ProcheCour','LointainJardin','LointainCour'], 'White', 'All', 'aleatoire', alea_type = ['bar', 3])

# def testStrobeColor(seq, timer):
#     strobelights(seq, timer, 'Tutti', ['Red','Green','Blue'], 'All', 'aleatoire', alea_type = ['color', 1])

# def testStrobeTotal(seq, timer):
#     strobelights(seq, timer, ['ProcheJardin','ProcheCour','LointainJardin','LointainCour'], ['Red','Green','Blue'], 'All', 'aleatoire', alea_type = ['tutti', 2, 1, 4])


# EASED FADE
def eased_fade(seq, timer, path, mino, maxo, duration, step):
    coef = float(maxo-mino)/duration

    max_i = int(round(duration / step))
    step = float(duration) / max_i

    i = 0
    dimmer = mino
    for i in range(0,max_i+1):
        dimmer = coef * i * step + mino
        if type(path[0]) is not list:
            seq.send(qlcport, path, dimmer)

        else:
            for j in range(0,len(path)):
                seq.send(qlcport, path[j], dimmer)
        timer.wait(step)


# CHASE par barre
def bar_chase(seq, timer, bar, colors_s, segments_s = ['tb'], step = [1, 'b']):
    # colors_s = [[255, 200, 200], [240, 200, 140],...]
    # segments_s = [1, 3, 5, ...] | segments_s = ['tb'], segments_s = ['bt'], segments_s = ['alea']
    # step = [duration, unit]
    

    if segments_s == ['tb']:
        segments_s = []
        for i in range(1,9):
            segments_s.append(i)
    elif segments_s == ['bt']:
        segments_s = []
        for i in range(1,9):
            segments_s.append(9-i)
    elif segments_s == ['alea']:
        segments_s = []
        for i in range(1,9):
            x = randint(1,8)
            while x in segments_s:
                x = randint(1,8)
            segments_s.append(x)
    
    for i in range(0,8):
        seq.send(qlcport, '/'+str(bar)+'/*/Segment/*', 0)
        seq.send(qlcport, '/'+str(bar)+'/Red/Segment/'+str(segments_s[i]), colors_s[i%len(colors_s)][0])
        seq.send(qlcport, '/'+str(bar)+'/Green/Segment/'+str(segments_s[i]), colors_s[i%len(colors_s)][1])
        seq.send(qlcport, '/'+str(bar)+'/Blue/Segment/'+str(segments_s[i]), colors_s[i%len(colors_s)][2])
        timer.wait(step[0], step[1])

    seq.send(qlcport, '/'+str(bar)+'/*/Segment/*', 0)
                     


