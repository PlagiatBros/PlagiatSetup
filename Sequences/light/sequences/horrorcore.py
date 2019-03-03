#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *

woods_all = 'Wood_1 Wood_2 Wood_3 Wood_4 Worms_1'
woods = woods_all.split(' ')

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

bears_all = 'BearEye_1 BearEye_2 BearEye_3 BearEye_4 Worms_1'
bears = bears_all.split(' ')

hc_beareye_jardin=[]
for i in range(5):
    b = bears[i]
    hc_beareye_jardin.append([[rpijardinport, '/pyta/slide/visible', bears_all, 0], [rpijardinport, '/pyta/slide/visible', b, 1], [rpijardinport, '/pyta/slide/animate', b, 'alpha', 0.4, 0.1, 1], [rpijardinport, '/pyta/slide/animate', b, 'scale_x', 780, 820, 1]])

hc_beareye_cour=[]
for i in range(5):
    b = bears[i]
    hc_beareye_cour.append([[rpicourport, '/pyta/slide/visible', bears_all, 0], [rpicourport, '/pyta/slide/visible', b, 1], [rpicourport, '/pyta/slide/animate', b, 'alpha', 0.4, 0.1, 1], [rpicourport, '/pyta/slide/animate', b, 'scale_x', 780, 820, 1]])
