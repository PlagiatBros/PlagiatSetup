#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

wholeworld_couplet_anim = [
    [[':/Lightseq/Scene/Play', 'wholeworld_faded_redflash'],[':/Lightseq/Scene/Play', 'wholeworld_faded_gbflash']], None, ([':/Lightseq/Scene/Play', 'wholeworld_faded_redpump'], [':/Lightseq/Scene/Play', 'wholeworld_faded_gbflash']), None
    ]

wholeworld_couplet_anim_surcouche = [
    None, None, None, [':/Lightseq/Scene/Play', 'wholeworld_synthflash']
    ]

wholeworld_refrain_anim = [
    [[':/Lightseq/Scene/Play', 'wholeworld_refrain_fixe'], [':/Lightseq/Scene/Play', 'wholeworld_refrain_strobe']], None, None, None,
    None, None, None, [[':/Lightseq/Scene/Stop', 'wholeworld_refrain_fixe'], [':/Lightseq/Scene/Stop', 'wholeworld_refrain_strobe'], [qlcport, '/Stop']]
    ]


