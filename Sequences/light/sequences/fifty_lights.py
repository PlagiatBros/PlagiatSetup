#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *


fifty_dark_couplet_anim = [
    [[':/Lightseq/Scene/Stop', 'fifty_dark_couplet_switchcourjar'], [':/Lightseq/Scene/Play', 'fifty_dark_couplet_switchjarcour']], None, None, None,
    None, None, None, None,
    [[':/Lightseq/Scene/Stop', 'fifty_dark_couplet_switchjarcour'], [':/Lightseq/Scene/Play', 'fifty_dark_couplet_switchcourjar']], None, None, None,
    None, None, None, None,
    ]

bimProche = [':/Lightseq/Scene/Play', 'fifty_ragga_aleaproche']
stopProche = [qlcport, '/TuttiProche/*/Segment/*', 0]
boumProche = [':/Lightseq/Scene/Play', 'fifty_ragga_boum']
fifty_ragga_anim = [
    (None, None, bimProche, stopProche, bimProche, stopProche),     (None, None, bimProche, stopProche, bimProche, stopProche) 
    ]

fifty_ragga_anim_firststep = [
    boumProche, None
    ]

boumTheme = [':/Lightseq/Scene/Play', 'fifty_petit_theme_boum']
whooTheme = [':/Lightseq/Scene/Play', 'fifty_petit_theme_whoo']
fifty_petit_theme_anim = [
    boumTheme, whooTheme, whooTheme, whooTheme
    ]

bimRefrain = [':/Lightseq/Scene/Play', 'fifty_refrain_aleaproche']
stopRefrain = [qlcport, '/Tutti/*/Segment/[1-7]', 0]
fifty_refrain_anim = [
    (bimRefrain, stopRefrain, bimProche, stopProche, bimRefrain, stopRefrain),     (None, None, bimProche, stopProche, bimProche, stopProche), 
    ]
