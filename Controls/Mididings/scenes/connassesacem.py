#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

#### ConnassesSACEM ####
connassessacem = [
    Init([
        Program(seq24PageMap[1]) >> seq24once,
        Ctrl(0, 1) >> tapeutapecontrol,
        zynmicrotonal_on,
        SendOSC(zyntrebleport, '/microtonal/tunings', '100.0\n200.0\n300.0\n435.0\n500.0\n600.0\n700.0\n800.0\n900.0\n1000.0\n1135.0\n2/1')
        ]),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    [orl, jeannot] >> ProgramFilter(2) >> [ # Thème Intro - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.35185),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            SendOSC(cmeinport, '/mididings/switch_scene', 5),


            ] >> Discard()
        ],
    [orl, jeannot] >> ProgramFilter(3) >> [ # Thème Intro - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, 0.708955),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, 0.35185),

            SendOscState([
                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB]/unscaled', -7.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,


            ] >> Discard()
        ],
    orl >> ProgramFilter(4) >> [
        SendOSC(slport, '/sl/6/hit', 'record')
        ] >> Discard(),
    orl >> ProgramFilter(5) >> [
        SendOSC(slport, '/sl/7/hit', 'record')
        ] >> Discard(),
    orl >> ProgramFilter(6) >> [
        SendOSC(slport, '/sl/8/hit', 'record')
        ] >> Discard(),
    orl >> ProgramFilter(7) >> [
        SendOSC(slport, '/sl/-1/hit', 'pauseon')
        ] >> Discard(),
    orl >> ProgramFilter(11) >> [
        SceneSwitch(2) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],


    ]
