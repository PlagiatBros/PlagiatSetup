#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

#### HorroCore ####
horrorcore = [
    Init([
        Program(seq24PageMap[9]) >> seq24once,
        Ctrl(0, 9) >> tapeutapecontrol,
        zynmicrotonal_on,
        SendOSC(zyntrebleport, '/microtonal/tunings', '135.0\n200.0\n300.0\n400.0\n500.0\n600.0\n700.0\n835.0\n900.0\n1000.0\n1065.0\n2/1'),
        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        SubSceneSwitch(2),
    ]),
    [orl, jeannot] >> Filter(PROGRAM) >> [
        SendOSC(audioseqport, '/Audioseq/Sequences/Disable', '*')
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # Couplet (orl meuf) - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],

                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -12.0],
                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -15.0],

            ]),


            vxorlmeuf_on,
            vxorlgars_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesreversedelayport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],


            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_on,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(4) >> [ # Couplet 2 (orl gars, jeannot rabbits) - Bouton 4
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],

                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -12.0],
                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -15.0],

            ]),


            vxorlmeuf_off,
            vxorlgars_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    jeannot >> ProgramFilter(2) >> [ # WE IS DA REAL RABBITS (stop milieu couplet) - Bouton 2
        stop,
        [

            vxorlmeuf_on,
            vxorlgars_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_on,
            vxjeannotmeuf_on,
            vxjeannotdelay_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            ] >> Discard()
        ],
    orl >> ProgramFilter(5) >> [ # Refrain grand messe - bouton 5
        stop,
        [


            SendOscState([

            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 12),

            vxorlmeuf_off,
            vxorlgars_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(6) >> [ # Outro africa - Bouton 6
        Program(67) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            vxorlmeuf_off,
            vxorlgars_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_on,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_on,
            vxjeannotvocode_on,

            ] >> Discard()
        ],
    orl >> ProgramFilter(7) >> [ # Bouclage synths - bouton 7
        SendOSC(slport, '/sl/7/hit', 'record')
        ] >> Discard(),
    orl >> ProgramFilter(8) >> [ # Overdub synths - bouton 8
        SendOSC(slport, '/sl/7/hit', 'overdub')
        ] >> Discard(),
    ]
