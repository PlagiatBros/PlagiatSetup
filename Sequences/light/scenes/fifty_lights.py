#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from scene_functions import *

def fifty_intro(seq, timer):
    seq.send(qlcport, '/TuttiProche/Red/Segment/{1,4,8}', 236)
    seq.send(qlcport, '/TuttiProche/Green/Segment/{1,4,8}', 201)
    seq.send(qlcport, '/TuttiProche/Blue/Segment/{1,4,8}', 152)

    seq.send(qlcport, '/TuttiLointain/Red/Segment/8', 118)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/8', 100)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/8', 76)

    seq.send(qlcport, '/TuttiLointain/Red/Segment/{4,5}', 236)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 201)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/{4,5}', 152)

def fifty_dark_couplet(seq, timer):
    seq.scene_run_subscene(crepitement,[seq, timer, [['TuttiProche', 'Blue', '{1,7,8}', 70, 92]]])
    seq.scene_run_subscene(crepitement,[seq, timer, [['ProcheCour', 'Red', '{1,7,8}', 190, 216]]])
    seq.scene_run_subscene(crepitement,[seq, timer, [['ProcheCour','Green','{1,7,8}', 190, 216]]])
    seq.scene_run_subscene(crepitement,[seq, timer, [['ProcheJardin','Red', '{1,7,8}', 190, 216]]])
    seq.scene_run_subscene(crepitement,[seq, timer, [['ProcheJardin','Green','{1,7,8}', 190, 216]]])
    seq.send(qlcport, '/damper', '/TuttiProche/Blue/Segment/{1,7,8}', 0.5)

    seq.send(qlcport, '/TuttiLointain/Red/Segment/{4,5}', 236)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 201)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/{4,5}', 152)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/8', 69)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/8', 50)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/8', 38)

def fifty_dark_couplet_switchjarcour(seq,timer):
    seq.animate([qlcport, '/damper', '/ProcheCour/Red/Segment/{1,7,8}'], 0.3, 0.6, 8, 'b')
    seq.animate([qlcport, '/damper', '/ProcheCour/Green/Segment/{1,7,8}'], 0.6, 0.3, 8, 'b')
    seq.animate([qlcport, '/damper', '/ProcheJardin/Red/Segment/{1,7,8}'], 0.6, 0.3, 8, 'b')
    seq.animate([qlcport, '/damper', '/ProcheJardin/Green/Segment/{1,7,8}'], 0.3, 0.6, 8, 'b')

def fifty_dark_couplet_switchcourjar(seq,timer):
    seq.animate([qlcport, '/damper', '/ProcheCour/Red/Segment/{1,7,8}'], 0.6, 0.3, 8, 'b')
    seq.animate([qlcport, '/damper', '/ProcheCour/Green/Segment/{1,7,8}'], 0.3, 0.6, 8, 'b')
    seq.animate([qlcport, '/damper', '/ProcheJardin/Red/Segment/{1,7,8}'], 0.3, 0.6, 8, 'b')
    seq.animate([qlcport, '/damper', '/ProcheJardin/Green/Segment/{1,7,8}'], 0.6, 0.3, 8, 'b')


def fifty_ragga(seq,timer):
    seq.send(qlcport, '/TuttiLointain/Red/Segment/{4,5}', 236)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/{4,5}', 201)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/{4,5}', 152)
    seq.send(qlcport, '/TuttiLointain/Red/Segment/8', 69)
    seq.send(qlcport, '/TuttiLointain/Green/Segment/8', 50)
    seq.send(qlcport, '/TuttiLointain/Blue/Segment/8', 38)

def fifty_ragga_aleaproche(seq,timer):
    i = range(1,9)
    j = i[randint(0,7)]
    seq.send(qlcport,'/TuttiProche/Red/Segment/'+str(j), 118)
    seq.send(qlcport,'/TuttiProche/Green/Segment/'+str(j), 100) 
    seq.send(qlcport,'/TuttiProche/Blue/Segment/'+str(j), 100)

def fifty_ragga_boum(seq,timer):
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiProche/{Red}/Segment/All', 180, 0, 0.2, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiProche/{Green}/Segment/All', 100, 0, 0.2, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiProche/{Blue}/Segment/All', 130, 0, 0.2, 0.01])


def fifty_petit_theme_boum(seq,timer):
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/{Red}/Segment/All', 255, 200, 0.2, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/{Green}/Segment/All', 120, 100, 0.2, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/{Blue}/Segment/All', 130, 110, 0.2, 0.01])
    
def fifty_petit_theme_whoo(seq,timer):
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/{Red}/Segment/All', 180, 150, 0.2, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/{Green}/Segment/All', 100, 70, 0.2, 0.01])
    seq.scene_run_subscene(eased_fade, [seq, timer, '/TuttiLointain/{Blue}/Segment/All', 110, 105, 0.2, 0.01])

def fifty_refrain(seq,timer):
    seq.send(qlcport, '/Tutti/Red/Segment/8', 200)

def fifty_refrain_aleaproche(seq,timer):
    i = range(1,8)
    j = i[randint(0,6)]
    bars = ['ProcheJardin', 'ProcheCour', 'LointainJardin', 'LointainCour']
    bar = bars[randint(0,3)]
    seq.send(qlcport,'/'+str(bar)+'/Red/Segment/'+str(j), 168)
    seq.send(qlcport,'/'+str(bar)+'/Green/Segment/'+str(j), 100) 
    seq.send(qlcport,'/'+str(bar)+'/Blue/Segment/'+str(j), 100)

