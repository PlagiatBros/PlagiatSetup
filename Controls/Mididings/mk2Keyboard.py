# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from utils import OSCCustomInterface
from ports import *
from math import log10

from liblo import ServerThread
from time import sleep


config(
	backend='jack',
	client_name='Mk2KeyBoardRoutes',
	out_ports=['Mk2OutBass', 'Mk2OutTreble', 'Mk2OutRhodes', 'Mk2OutTapeutape', 'Mk2OutWobble'],
	in_ports=['Mk2In']
)


hook(
    OSCInterface(mk2inport, mk2outport),
    AutoRestart()
)

gatecancel = CtrlFilter(41,64) >> [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gate/Threshold%20(dB)/unscaled', lambda ev: -ev.value/127 * 54.0 - 24),
    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gate/Threshold%20(dB)/unscaled', lambda ev: -ev.value/127 * 54.0 - 24),
    ] >> Discard()

bassfilter = CtrlFilter(18) >> [
    SendOSC(bassmainport, '/strip/BassMain/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.))),
    SendOSC(bassmainport, '/strip/BassDry/Calf%20Filter/Frequency/unscaled', lambda ev: 20000. * pow(10,((-log10(71/20000.))*ev.value) / 127. + log10(71/20000.)))
]

looperctl = CtrlFilter(range(109,117)) >> [

	CtrlFilter(109) >> SendOSC(slport, '/sl/4/hit', 'record'), #pre
	CtrlFilter(110) >> SendOSC(slport, '/sl/4/hit', 'overdub'),
	CtrlFilter(111) >> SendOSC(slport, '/sl/4/hit', 'pause_on'),
	CtrlFilter(112) >> SendOSC(slport, '/sl/5/hit', 'record'), #post
	CtrlFilter(113) >> SendOSC(slport, '/sl/5/hit', 'overdub'),
	CtrlFilter(114) >> SendOSC(slport, '/sl/5/hit', 'pause_on'),
	CtrlFilter(116) >> SendOSC(slport, '/sl/-1/hit', 'reverse'), #reverse

]

run(
    scenes = {
        1: 	Scene("BassWobbleCtrl",
                [
                [Filter(NOTE), Filter(PITCHBEND)] >> Output('Mk2OutWobble', 1),
                bassfilter,
                gatecancel,
				looperctl
                ]
          ),
        2: 	Scene("VxDelayCtrl",
                [
                KeyFilter(notes=['f2','c3','g3']) >> [
                    Filter(NOTEON) >> SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0),
                    Filter(NOTEOFF) >> SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
                    ] >> Discard(),
                bassfilter,
                gatecancel,
				looperctl
                ]
              ),
        3: Scene("Connasses SACEM samples",
                [
                Filter(NOTEON) >> Output('Mk2OutTapeutape', 1),
                bassfilter,
                gatecancel,
				looperctl
                ]
              ),
        4: Scene("Samples cut",
                [
                    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> [
                        SendOSC(samplesmainport, '/strip/SamplesMain/Gain/Mute', 1.0)
                    ],
                    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [
                        SendOSC(samplesmainport, '/strip/SamplesMain/Gain/Mute', 0.0)
                    ],
                    bassfilter,
                    gatecancel,
					looperctl
                ] >> Discard()
              ),
        5: Scene("HorroCore RIP",
                [
                    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> [

                        SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 0.0),
                        SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 0.0),
                        SendOSC(surfaceorlport, '/vxorl', 'meuf', 1),
                        SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 1.0),
                        SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 1.0),
                        SendOSC(surfaceorlport, '/vxorl', 'gars', 0),
                        SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 0.0),
                        SendOSC(vxjeannotpostport, '/strip/VxJeannotMeufPost/Gain/Mute', 0.0),
                        SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gain/Mute', 1.0),
                        SendOSC(vxjeannotpostport, '/strip/VxJeannotGarsPost/Gain/Mute', 1.0),

                    ],
                    KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEOFF) >> [

                        SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 0.0),
                        SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 0.0),
                        SendOSC(surfaceorlport, '/vxorl', 'gars', 1),
                        SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 1.0),
                        SendOSC(surfaceorlport, '/vxorl', 'meuf', 0),
                        SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gain/Mute', 0.0),
                        SendOSC(vxjeannotpostport, '/strip/VxJeannotGarsPost/Gain/Mute', 0.0),
                        SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 1.0),
                        SendOSC(vxjeannotpostport, '/strip/VxJeannotMeufPost/Gain/Mute', 1.0),

                    ],
                    bassfilter,
                    gatecancel,
					looperctl
                ] >> Discard()
              ),
          6: 	Scene("Clap",
                  [
                  KeyFilter(notes=['f2','c3','g3']) >> Filter(NOTEON) >> NoteOn(64,127) >> Output('Mk2OutTapeutape', 1),
                  bassfilter,
                  gatecancel,
				  looperctl
                  ]
                ),

    },
    control = Filter(PROGRAM) >> SceneSwitch(),
    pre = ~Filter(PROGRAM)
)
