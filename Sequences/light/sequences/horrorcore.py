#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *

woods_all = 'Wood_1 Wood_2 Wood_3 Wood_4 Worms_1'
woods = 'Wood_1 Wood_2 Wood_3 Wood_4'.split(' ')

hc_wood = []
for i in range(len(woods)):
    hc_wood.append([[rpijardinport, '/pyta/slide/visible', woods_all, 0], [rpijardinport, '/pyta/slide/visible', woods[i], 1]])
    hc_wood.append([[rpicourport, '/pyta/slide/visible', woods_all, 0], [rpicourport, '/pyta/slide/visible', woods[i], 1]])

hc_worm = [
    [[rpijardinport, '/pyta/slide/visible', woods_all, 0], [rpijardinport, '/pyta/slide/visible', 'Worms_1', 1]],
    [[rpicourport, '/pyta/slide/visible', woods_all, 0], [rpicourport, '/pyta/slide/visible', 'Worms_1', 1]],
    None, None, None, None,
    None, None, None, None,
]

beareyes = 'BearEye_1 BearEye_2 BearEye_3 BearEye_4 Worms_1'

hc_beareye_jardin=[]
for i in range(1,5):
    hc_beareye_jardin.append([[rpijardinport, '/pyta/slide/visible', woods, -1], [rpijardinport, '/pyta/slide/visible', 'BearEye_'+str(i), 1], [rpijardinport, '/pyta/slide/animate', 'BearEye_'+str(i), 'alpha', 0.4, 0.1, 1], [rpijardinport, '/pyta/slide/animate', 'BearEye_'+str(i), 'scale_x', 780, 820, 1]])

hc_beareye_cour=[]
for i in range(1,5):
    hc_beareye_cour.append([[rpicourport, '/pyta/slide/visible', woods, -1], [rpicourport, '/pyta/slide/visible', 'BearEye_'+str(i), 1], [rpicourport, '/pyta/slide/animate', 'BearEye_'+str(i), 'alpha', 0.4, 0.1, 1], [rpicourport, '/pyta/slide/animate', 'BearEye_'+str(i), 'scale_x', 780, 820, 1]])
