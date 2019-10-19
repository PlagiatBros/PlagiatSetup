#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *



tempsStart = [':/Lightseq/Scene/Play', 'climat_precouplet_moise_flash']
bimJardin = [':/Lightseq/Scene/Play', 'climat_precouplet_moise_flash2']

climat_precouplet_moise = [
    tempsStart, None, None, None, None, None, None, None,
    tempsStart, None, None, None, None, None, None, None,
    tempsStart, None, None, None, None, None, None, None,
    tempsStart, None, None, bimJardin, None, None, None, None,
    None, None, None, tempsStart, None, None, None,

    tempsStart, None, None, None, None, None, None, None,
    tempsStart, None, None, None, None, None, None, None,
    tempsStart, None, None, None, None, None, None, bimJardin,
    None, None, None, None, None, None, None, tempsStart, None, None, None
]


_d = [':/Lightseq/Scene/Play', 'climat_refrain_bardanse']
climat_refrain_bardanse = [_d, None] * 19 + [_d] + [_d, None] * 17 + [_d]


climat_mandela_danse = [
    ([[rpicourport, '/pyta/slide/white/set', 'alpha', 1], [rpijardinport, '/pyta/slide/white/set', 'alpha', 0]],
    [[rpicourport, '/pyta/slide/white/set', 'alpha', 0], [rpijardinport, '/pyta/slide/white/set', 'alpha', 1]])
]
