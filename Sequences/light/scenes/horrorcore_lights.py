#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import randint
from time import sleep
from math import exp, log

### ALIASES GENERAUX

def crepitement(seq, timer, args): 
    # bars, colors et segments suivant syntaxe OSC
    while True:
        for i in range(0,len(args)):
            bars, colors, segments, cmin, cmax = args[i]
            seq.send(qlcport, '/'+bars+'/'+colors+'/Segment/'+segments, randint(cmin, cmax))
        timer.wait(0.01, 's')


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
        coef = float(log(maxo-mino+1))/duration
        boef = mino-1

    i = 0
    while True:
        if ramped is not None:
            dimmer = round(exp(coef * i * step) + boef)

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
        
###


def horrorcore_intro(seq, timer):
    seq.send(qlcport, '/TuttiProche/Green/Segment/[1-2]', 60)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[1-2]', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[7-8]', 255)

def horrorcore_couplet_stable(seq, timer):
    seq.send(qlcport, '/TuttiProche/Green/Segment/[1-2]', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/[1-3]', 255)
    seq.send(qlcport, '/TuttiProche/Red/Segment/8', 120)
    seq.send(qlcport, '/TuttiProche/Red/Segment/7', 0)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/1', 15)

def horrorcore_couplet_crepitement(seq, timer):
    crepitement(seq, timer, [["Tutti", "White", "{3,5}", 15, 30]])

def horrorcore_couplet_crepitement_stop(seq, timer):
    seq.scene_stop('horrorcore_couplet_crepitement')
    seq.send(qlcport, '/Tutti/White/Segment/{3,5}', 0)

def horrorcore_couplet_donkey(seq, timer):
    seq.send(qlcport, '/TuttiProche/*/Segment/All', 0)
    seq.send(qlcport, '/ProcheJardin/White/Segment/1', 70)
    seq.send(qlcport, '/ProcheCour/White/Segment/2', 70)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/{1,8}', 30)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{1,8}', 20)

def horrorcore_refrain_stable(seq, timer):
    seq.send(qlcport, '/TuttiProche/White/Segment/{1,2}', 200)
    seq.send(qlcport, '/TuttiProche/Green/Segment/{5,6,7,8}', 140)
    seq.send(qlcport, '/TuttiProche/Red/Segment/{5,6,7,8}', 160)
    seq.scene_run_subscene(crepitement, [seq, timer, [['TuttiProche', 'Red', '{3,4}', 15,80],['TuttiLointain', 'Red', '{1,3,5,7}', 30, 80], ['TuttiLointain', 'Green', '{1,3,5,7}', 50, 70], ['TuttiLointain', 'Red', '{2,4,6,8}', 50, 70], ['TuttiLointain', 'Green', '{2,4,6,8}', 30, 80]]])

def horrorcore_couplet2_intro(seq, timer):
    seq.send(qlcport, '/TuttiProche/White/Segment/1', 140)
    crepitement(seq, timer, [['ProcheJardin', 'Red', '2', 30, 80], ['ProcheCour', 'Red', '2', 30, 40]])

def horrorcore_sun_zoom(seq, timer):
    seq.send(rpijardinport, '/pyta/slide/Sun_1/animate', 'tiles', 1, 1, 0.1, 0.1, 1, 'sine')    
    seq.send(rpicourport, '/pyta/slide/Sun_2/animate', 'tiles', 1, 1, 0.1, 0.1, 1, 'sine')    

def horrorcore_white_flash(seq, timer):
    seq.send(rpijardinport, '/pyta/slide/white/set', 'visible', 1)
    seq.send(qlcport, '/*/White/Segment/*', 255)
    timer.wait(0.001, 's')
    seq.send(qlcport, '/*/White/Segment/*', 0)
    timer.wait(0.03, 's')
    seq.send(rpijardinport, '/pyta/slide/white/set', 'visible', 0)


def horrorcore_couplet2_dubstep_extinction(seq, timer):
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'rgbwave', 0.3)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'position_z', -1)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'rgbwave', 0.3)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'position_z', -1)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'zoom', 1.5)    
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'zoom', 1.5)    
    horrorcore_sun_zoom(seq, timer)

    seq.send(':/Lightseq/Sequence/Disable', 'horrorcore_couplet_blinkBass')
    seq.send(qlcport, '/*/*/Segment/*', 0)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 1)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 1)
    horrorcore_sun_zoom(seq, timer)

    timer.wait(20, 'b')
    seq.send(':/Lightseq/Scene/Play', 'horrorcore_white_flash')
    seq.send(':/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass')
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 0)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 0)

    timer.wait(140, 'b')
    seq.send(':/Lightseq/Sequence/Disable', 'horrorcore_couplet_blinkBass')
    seq.send(qlcport, '/*/*/Segment/*', 0)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 1)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 1)
    horrorcore_sun_zoom(seq, timer)

    timer.wait(20, 'b')
    seq.send(':/Lightseq/Scene/Play', 'horrorcore_white_flash')
    seq.send(':/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass')
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 0)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 0)

    timer.wait(150, 'b')
    seq.send(':/Lightseq/Sequence/Disable', 'horrorcore_couplet_blinkBass')
    seq.send(qlcport, '/*/*/Segment/*', 0)
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 1)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 1)
    horrorcore_sun_zoom(seq, timer)

    timer.wait(20, 'b')
    seq.send(':/Lightseq/Scene/Play', 'horrorcore_white_flash')
    seq.send(':/Lightseq/Sequence/Enable', 'horrorcore_couplet_blinkBass')
    seq.send(rpijardinport, '/pyta/slide/Sun_1/set', 'visible', 0)
    seq.send(rpicourport, '/pyta/slide/Sun_2/set', 'visible', 0)

def horrorcore_couplet2_blinder_surcouche(seq, timer):
    seq.send(qlcport, '/TuttiLointain/{Red,Green}/Segment/8', 120)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/7', 70)


def horrorcore_messe(seq, timer):
    seq.send(qlcport, '/TuttiProche/{Red,Blue}/Segment/{7,8}', 100)
    seq.send(qlcport, '/TuttiLointain/{Red,Blue}/Segment/{2,7,8}', 190)
    seq.send(qlcport, '/TuttiProche/White/Segment/1', 75)

def horrorcore_ac4_intro1(seq,timer):
    crepitement(seq, timer, [['TuttiJardin', 'Red', '{4,5}', 30, 100], ['TuttiJardin', 'Blue', '{4,5}', 30, 100], ['TuttiCour', 'Red', '{4,5}', 30, 100], ['TuttiCour', 'Blue', '{4,5}', 30, 100]])
#    crepitement(seq, timer, [['LointainJardin', 'Red', '{1,3,5,7}', 30, 100], ['LointainJardin', 'Red', '{2,4,6,8}', 30, 100], ['LointainJardin', 'Blue', '{1,3,5,7}', 30, 100], ['LointainJardin', 'Blue', '{2,4,6,8}', 30, 100], ['LointainCour', 'Red', '{1,3,5,7}', 30, 100], ['LointainCour', 'Red', '{2,4,6,8}', 30, 100], ['LointainCour', 'Blue', '{1,3,5,7}', 30, 100], ['LointainCour', 'Blue', '{2,4,6,8}', 30, 100]])
    
def horrorcore_ac4_intro2(seq,timer):
    strobelights(seq, timer, ['ProcheJardin', 'ProcheCour', 'LointainJardin', 'LointainCour'], ['White'], [1, 2, 3, 6, 7, 8], 'aleatoire', step= 0.01, ramped = [0, 255, 60], alea_type = ['tutti', 1, 1, 1])


def horrorcore_dropTheBass(seq,timer):
    seq.send(qlcport, '/Tutti/Green/Segment/1', 118)
    seq.send(qlcport, '/Tutti/Blue/Segment/1', 25)
    seq.send(qlcport, '/Tutti/Red/Segment/8', 50)

def horrorcore_mooncup_maison(seq,timer):
    crepitement(seq, timer, [['Tutti', 'Red', 'All', 120, 255]])
