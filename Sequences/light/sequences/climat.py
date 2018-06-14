#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *




darkEyes=""
dark_eyes = ['FreakyEye_1', 'BlueOnBlackEye_1', 'OrangeOnBlackEye_1', 'OrangeOnBlackEye_2', 'RedOnBlackEye_1']
for i in range (1,5):
    darkEyes+=dark_eyes[i]+" "

climat_theme_strobe = []
for i in range(1, 10):
    climat_theme_strobe.append(['/pyta/slide/strobe', darkEyes, 1, 2, 0.5])
for i in range(1, 10):
    climat_theme_strobe.append(['/pyta/slide/strobe', darkEyes, 0])


eye_shut_jardin = [rpijardinport, '/pyta/slide/visible', " ".join(dark_eyes), 0]
eye_shut_cour = [rpicourport, '/pyta/slide/visible', " ".join(dark_eyes), 0]

climat_theme_jardin = [
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[0], 1]],
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[1], 1]],
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[2], 1]],
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[3], 1]],
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[4], 1]]
]

climat_theme_cour = [
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[0], 1]],
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[1], 1]],
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[2], 1]],
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[3], 1]],
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[4], 1]]
]

colos = " ".join(['Colo_'+str(i) for i in range(1,47)])
twerks = " ".join(['Twerk_'+str(i) for i in range(1,9)])

for i in range(0,46):
  climat_theme_jardin.append([[rpijardinport, '/pyta/slide/visible', colos, 0], [rpijardinport, '/pyta/slide/visible'], 'Colo_'+str(i), 1])
  climat_theme_cour.append([[rpicourport, '/pyta/slide/visible', colos, 0], [rpicourport, '/pyta/slide/visible'], 'Colo_'+str(i), 1])
