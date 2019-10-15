#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

# aliases généraux
whiteC_Play = [":/Lightseq/Scene/Play", "horrorcore_couplet_crepitement"]
whiteC_Stop = [":/Lightseq/Scene/Play", "horrorcore_couplet_crepitement_stop"]



horrorcore_couplet_blinkBass = [
    None, None, None, whiteC_Play,
    None, (None, whiteC_Stop), (None, None, whiteC_Play), whiteC_Stop,
    None, None, None, whiteC_Play,
    None, (None, whiteC_Stop), None, None,

    None, None, None, whiteC_Play,
    None, (None, whiteC_Stop), (None, None, whiteC_Play), whiteC_Stop,
    None, None, None, whiteC_Play,
    None, (None, whiteC_Stop), None, ([qlcport, '/TuttiLointain/Red/Segment/All', 70], [qlcport, '/TuttiLointain/Red/Segment/All', 0], None, None, None, None, None, None)
]

