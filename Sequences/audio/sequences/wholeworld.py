from ports import *

def SendOSC(*args):
    return list(args)

pitch_up = [

    SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'gars', 0),
    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 0.0),
    SendOSC(surfaceorlport, '/vxorl', 'meuf', 1),

]

pitch_down = [

    SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 0.0),
    SendOSC(surfaceorlport, '/vxorl', 'gars', 1),
    SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'meuf', 0),

]

wholeworld_refrain = [
    pitch_down, None, None, None,
    None, pitch_up, None, None,
]
