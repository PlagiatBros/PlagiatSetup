import sys
sys.path.append("../Controls/Mididings/")

from ports import *



#  Intro


# Couplet


dark_eyes = ['FreakyEye_1', 'BlueOnBlackEye_1', 'OrangeOnBlackEye_1', 'OrangeOnBlackEye_2', 'RedOnBlackEye_1']

eye_shut_jardin = [rpijardinport, '/pyta/slide/visible', " ".join(dark_eyes), 0]
eye_shut_cour = [rpicourport, '/pyta/slide/visible', " ".join(dark_eyes), 0]

wholeworld_reveil_sournois_jardin = [
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[0], 1]],
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[1], 1]],
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[2], 1]],
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[3], 1]],
    [eye_shut_jardin, [rpijardinport, '/pyta/slide/visible', dark_eyes[4], 1]]
]

wholeworld_reveil_sournois_cour = [
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[0], 1]],
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[1], 1]],
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[2], 1]],
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[3], 1]],
    [eye_shut_cour, [rpicourport, '/pyta/slide/visible', dark_eyes[4], 1]]
]

wholeworld_refrain = [
    [':/lightseq/scene/play', 'wholeworld_refrain_rough'], None, None, None,
    [':/lightseq/scene/play', 'wholeworld_refrain_rough'], None, [':/lightseq/scene/play', 'wholeworld_refrain_snapshat'], None
]
