import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from aliases import *
import mididings

def _alias(a):
    if type(a) is mididings.units.base._Chain:
        return [_alias(x) for x in list(a[0])]
    if type(a) is list:
        return [_alias(x) for x in a]
    else:
        data = a._args[0]
        m = [data.target, data.path]
        for x in data.args:
            m.append(x)
        return m

# print(vxorlmeuf_off[])
_G = _alias(vxorlmeuf_off) + _alias(vxorlgars_on) + _alias(vxorlvocode_off)
_M = _alias(vxorlmeuf_on) + _alias(vxorlgars_off) + _alias(vxorlvocode_off)
_N = _alias(vxorlmeuf_off) + _alias(vxorlgars_off) + _alias(vxorlvocode_on)
_NG = _alias(vxorlmeuf_off) + _alias(vxorlgars_on) + _alias(vxorlvocode_on)
_NM = _alias(vxorlmeuf_on) + _alias(vxorlgars_off) + _alias(vxorlvocode_on)
_MUTE = [[bassmainport, '/strip/BassSynth/Gain/Mute', 1.0], [samplesmainport, '/strip/Keyboards/Gain/Mute', 1.0], [samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0]]
_UNMUTE = [[bassmainport, '/strip/BassSynth/Gain/Mute', 0.0], [samplesmainport, '/strip/Keyboards/Gain/Mute', 0.0], [samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0]]

dafist_outro_filter = [
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,[':/Audioseq/Scene/Play','dafist_outro_filter_close'],None,None
]

dafist_couplet_part2_vx_launcher = [
    [
        [':/Audioseq/Sequence/Disable','dafist_couplet_part2_vx_launcher'],
        [':/Audioseq/Sequence/Enable','dafist_couplet_part2_vx_a'],
        [':/Audioseq/Play'],
    ], None, None, None
]

dafist_couplet_part2_vx_a = [

    _G + _UNMUTE,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,

    _NG,None,None,None,
    None,None,None,None,

    _N,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,_NM,_N,_NM,
    _N,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,[':/Audioseq/Scene/Play', 'dafist_couplet_part2_pitchdown'],

    # on coupe la bass synth et aller hop bass batt
    [[bassmainport, '/strip/BassSynth/Gain/Mute', 1.0], [':/Audioseq/Sequence/Disable', 'dafist_couplet_part2_vx_a']]


]

dafist_couplet_part2_vx_b = [
    # NO AMBITION
    _NM + [[bassmainport, '/strip/BassSynth/Gain/Mute', 1.0]],None,None,None,
    None,None,(None,None,_G),None,

    [bassmainport, '/strip/BassSynth/Gain/Mute', 0.0],None,None,None,
    None,None,None,None,

    _G,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,(None, None, _NM),


    # STOP (we not getting it at all)
    _MUTE, None,None,None,
    None,None,(None, [samplesmainport, '/strip/Keyboards/Gain/Mute', 0.0]),None,


    _N + _UNMUTE,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,
    None,None,None,None,


]
