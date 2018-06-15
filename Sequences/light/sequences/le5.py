#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *

coffee_redseas = " ".join(["Coffee_" + str(i) for i in range(1,11)])
coffee_redseas+=" Dunes_1"
coffee_redseas+=" Rock_1"
coffee_redseas+=" Moon_1"
coffee_redseas+=" Moon_2"
coffee_redseas+=" Mars_1"
coffee_redseas+=" Mars_2"
coffee_redseas+=" Mountains_1"
coffee_redseas+=" Mountains_2"

le5_coffee_redsea_jardin=[]
for i in range(1, 11):
    le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Coffee_'+str(i), 1]])

le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Dunes_1', 1]])
le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Rock_1', 1]])
le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Moon_1', 1]])
le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Moon_2', 1]])
le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Mars_1', 1]])
le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Mars_2', 1]])
le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Mountains_1', 1]])
le5_coffee_redsea_jardin.append([[rpijardinport, '/pyta/slide/visible', coffee_redseas, 0], [rpijardinport, '/pyta/slide/visible', 'Mountains_2', 1]])


le5_coffee_redsea_cour=[]
for i in range(1, 11):
    le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Coffee_'+str(i), 1]])

le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Dunes_1', 1]])
le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Rock_1', 1]])
le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Moon_1', 1]])
le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Moon_2', 1]])
le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Mars_1', 1]])
le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Mars_2', 1]])
le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Mountains_1', 1]])
le5_coffee_redsea_cour.append([[rpicourport, '/pyta/slide/visible', coffee_redseas, 0], [rpicourport, '/pyta/slide/visible', 'Mountains_2', 1]])


t_off=['/pyta/text/visible', 0, 0]
le5_refrain=[
    [t_off, ['/pyta/text/rgb', 0, 255, 255, 255], [rpijardinport, '/pyta/text', 0, "MEAN"], [rpijardinport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpijardinport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpicourport, '/pyta/text', 0, "MEAN"], [rpicourport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpicourport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpijardinport, '/pyta/text', 0, "MEAN"], [rpijardinport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpijardinport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpicourport, '/pyta/text', 0, "MEAN"], [rpicourport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpicourport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpijardinport, '/pyta/text', 0, "MEAN"], [rpijardinport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpijardinport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpicourport, '/pyta/text', 0, "MEAN"], [rpicourport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpicourport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpijardinport, '/pyta/text', 0, "MEAN"], [rpijardinport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpijardinport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, ['/pyta/text/rgb', 0, 255, 0, 0], ['/pyta/text', 0, "UGLY"], ['/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], ['/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, ['/pyta/text/rgb', 0, 255, 255, 255], [rpicourport, '/pyta/text', 0, "MEAN"], [rpicourport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpicourport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpijardinport, '/pyta/text', 0, "MEAN"], [rpijardinport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpijardinport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpicourport, '/pyta/text', 0, "MEAN"], [rpicourport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpicourport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpijardinport, '/pyta/text', 0, "MEAN"], [rpijardinport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpijardinport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpicourport, '/pyta/text', 0, "MEAN"], [rpicourport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpicourport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpijardinport, '/pyta/text', 0, "MEAN"], [rpijardinport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpijardinport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, [rpicourport, '/pyta/text', 0, "MEAN"], [rpicourport, '/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], [rpicourport, '/pyta/text/visible', 0, 1]], None, None, None, None,
    [t_off, ['/pyta/text/rgb', 0, 255, 0, 0], ['/pyta/text', 0, "UGLY"], ['/pyta/text/animate', 0, 'zoom', 0.7, 1.2, 0.3], ['/pyta/text/visible', 0, 1]], None, None, None, None,
]

# le5_twerk_jardin=[]
# le5_twerk_cour=[]
# for i in range(0,5):
#     le5_twerk_jardin.append([[rpijardinport, '/pyta/slide/visible', twerks, 0],[rpijardinport, '/pyta/slide/visible', 'Twerk_1.gif']])
#     le5_twerk_cour.append([[rpicourport, '/pyta/slide/visible', twerks, 0],[rpicourport, '/pyta/slide/visible', 'Twerk_1.gif']])
# for i in range(0,2):
#     le5_twerk_jardin.append([[rpijardinport, '/pyta/slide/visible', twerks, 0],[rpijardinport, '/pyta/slide/visible', 'Twerk_2.gif']])
#     le5_twerk_cour.append([[rpicourport, '/pyta/slide/visible', twerks, 0],[rpicourport, '/pyta/slide/visible', 'Twerk_2.gif']])
#
# le5_twerk_jardin.append([[rpijardinport, '/pyta/slide/visible', twerks, 0],[rpijardinport, '/pyta/slide/visible', 'Twerk_3.gif']])
# le5_twerk_cour.append([[rpicourport, '/pyta/slide/visible', twerks, 0],[rpicourport, '/pyta/slide/visible', 'Twerk_3.gif']])

le5_nymphotrap_blow = [
  [[rpijardinport, '/pyta/text/animate', 2, 'scale_x', 780, 800, 0.1],[rpicourport, '/pyta/text/animate', 1, 'scale_x', 780, 800, 0.1]]
]

gouttes = " ".join(["Gouttes_" + str(i) for i in range(1, 5)])

le5_boum_jardin = []
le5_boum_cour = []
for i in range(1, 5):
    le5_boum_jardin.append([[rpijardinport, '/pyta/slide/visible', gouttes, 0],[rpijardinport, '/pyta/slide/visible', 'Gouttes_'+str(i), 1], [rpijardinport, '/pyta/slide/animate', 'Gouttes_'+str(i), 'scale_x', 770, 800, 0.4]])
    le5_boum_cour.append([[rpicourport, '/pyta/slide/visible', gouttes, 0],[rpicourport, '/pyta/slide/visible', 'Gouttes_'+str(i), 1], [rpicourport, '/pyta/slide/animate', 'Gouttes_'+str(i), 'scale_x', 770, 800, 0.4]])
