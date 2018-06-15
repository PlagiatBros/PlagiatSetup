#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *

woods = 'Wood_1 Wood_2 Wood_3 Wood_4 Worms_1'

hc_wood_jardin=[]
for i in range(1,5):
    hc_wood_jardin.append([[rpijardinport, '/pyta/slide/visible', woods, -1], [rpijardinport, '/pyta/slide/visible', 'Wood_'+str(i), 1], [rpijardinport, '/pyta/slide/animate', 'Wood_'+str(i), 'alpha', 0.4, 0.1, 1], [rpijardinport, '/pyta/slide/animate', 'Wood_'+str(i), 'scale_x', 780, 820, 1]])

hc_wood_jardin.append([[rpijardinport, '/pyta/slide/visible', woods, -1], [rpijardinport, '/pyta/slide/visible', 'Worms_'+str(i), 1], [rpijardinport, '/pyta/slide/animate', 'Worms_'+str(i), 'alpha', 0.4, 0.1, 1], [rpijardinport, '/pyta/slide/animate', 'Worms_'+str(i), 'scale_x', 780, 820, 1]])

hc_wood_cour=[]
for i in range(1,5):
    hc_wood_cour.append([[rpicourport, '/pyta/slide/visible', woods, -1], [rpicourport, '/pyta/slide/visible', 'Wood_'+str(i), 1], [rpicourport, '/pyta/slide/animate', 'Wood_'+str(i), 'alpha', 0.4, 0.1, 1], [rpicourport, '/pyta/slide/animate', 'Wood_'+str(i), 'scale_x', 780, 820, 1]])

hc_wood_cour.append([[rpicourport, '/pyta/slide/visible', woods, -1], [rpicourport, '/pyta/slide/visible', 'Worms_'+str(i), 1], [rpicourport, '/pyta/slide/animate', 'Worms_'+str(i), 'alpha', 0.4, 0.1, 1], [rpicourport, '/pyta/slide/animate', 'Worms_'+str(i), 'scale_x', 780, 820, 1]])


beareyes = 'BearEye_1 BearEye_2 BearEye_3 BearEye_4 Worms_1'

hc_beareye_jardin=[]
for i in range(1,5):
    hc_beareye_jardin.append([[rpijardinport, '/pyta/slide/visible', woods, -1], [rpijardinport, '/pyta/slide/visible', 'BearEye_'+str(i), 1], [rpijardinport, '/pyta/slide/animate', 'BearEye_'+str(i), 'alpha', 0.4, 0.1, 1], [rpijardinport, '/pyta/slide/animate', 'BearEye_'+str(i), 'scale_x', 780, 820, 1]])

hc_beareye_cour=[]
for i in range(1,5):
    hc_beareye_cour.append([[rpicourport, '/pyta/slide/visible', woods, -1], [rpicourport, '/pyta/slide/visible', 'BearEye_'+str(i), 1], [rpicourport, '/pyta/slide/animate', 'BearEye_'+str(i), 'alpha', 0.4, 0.1, 1], [rpicourport, '/pyta/slide/animate', 'BearEye_'+str(i), 'scale_x', 780, 820, 1]])
