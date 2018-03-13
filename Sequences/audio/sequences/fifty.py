from ports import *

def SendOSC(*args):
    return list(args)


fifty_refrain_cutdown = [
    None,None,None,None,
    None,None,None,None,
    None,None,[':/Audioseq/Scene/Play','fifty_refrain_cutdown_close'], None
]


delay_on = [[vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0], [vxorlpostport, '/strip/VxORLDelayPost/Gain/Mute', 0.0], [surfaceorlport, '/vxorl', 'delay', 1], [vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 0.0], [vxjeannotpostport, '/strip/VxJeannotDelayPost/Gain/Mute', 0.0], [surfaceorlport, '/vxjeannot', 'delay', 1]]
delay_off = [[vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0], [vxorlpostport, '/strip/VxORLDelayPost/Gain/Mute', 1.0], [surfaceorlport, '/vxorl', 'delay', 0], [vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 1.0], [vxjeannotpostport, '/strip/VxJeannotDelayPost/Gain/Mute', 1.0], [surfaceorlport, '/vxjeannot', 'delay', 0]]

pitch_up = [

    SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'gars', 0),
    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 0.0),
    SendOSC(surfaceorlport, '/vxorl', 'meuf', 1),
    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotMeufPost/Gain/Mute', 0.0),
    SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotGarsPost/Gain/Mute', 1.0),

]

pitch_down = [

    SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 0.0),
    SendOSC(surfaceorlport, '/vxorl', 'gars', 1),
    SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'meuf', 0),
    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotMeufPost/Gain/Mute', 1.0),
    SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotGarsPost/Gain/Mute', 0.0),


]

fifty_refrain_stagiaire = [
    None,None,None,None,
    None,None,None,delay_on,
    None,None,pitch_up,None,
    None,pitch_down,None,None,
    None,delay_off,None,None,
    None,None,None,delay_on,
    None,delay_off,None,None,
    None,None,None,delay_on,
]
