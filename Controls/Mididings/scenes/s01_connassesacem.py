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
        Ctrl(0, 0) >> tapeutapecontrol,
        zynmicrotonal_on,
        SendOSC(zyntrebleport, '/microtonal/tunings', '100.0\n200.0\n300.0\n435.0\n500.0\n600.0\n700.0\n800.0\n900.0\n1000.0\n1135.0\n2/1'),
        SendOSC(mk2inport, '/mididings/switch_scene', 3),
        mk2lights([1,2,3]),
    ]),
    jeannot >> Filter(PROGRAM) >> mk2lights([1,2,3]),
    [orl, jeannot] >> ProgramFilter([range(2,4)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter([range(2,4)]) >> [
        SendOSC(lightseqport, '/Lightseq/Sequence/Disable', '*'),
        SendOSC(lightseqport, '/Lightseq/Scene/Stop', '*'),
        SendOSC(vporlport, '/pyta/slide/visible', -1, 0),
        SendOSC(vpjeannotport, '/pyta/slide/visible', -1, 0),
        SendOSC(qlcstopport, '/Stop'),
    ] >> Discard(),
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

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'connassesacem_1', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -7.0],

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
    [orl, jeannot] >> ProgramFilter(3) >> [ # Thème Intro + guitare - Bouton 3
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

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'connassesacem_2', timestamp),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Bpm', 125),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'connasses_metallica_clignote'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'connassesacem_1', timestamp),


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

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(4) >> [ # sl 6 record
        SendOSC(slport, '/sl/6/hit', 'record'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'connassesacem_1', timestamp),
        ] >> Discard(),
    orl >> ProgramFilter(5) >> [ # sl 7 record
        SendOSC(slport, '/sl/7/hit', 'record'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'connassesacem_1', timestamp),
        ] >> Discard(),
    orl >> ProgramFilter(6) >> [ # sl 8 record
        SendOSC(slport, '/sl/8/hit', 'record'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'connassesacem_1', timestamp),
        ] >> Discard(),
    orl >> ProgramFilter(7) >> [ # sl -1 pause
        SendOSC(slport, '/sl/-1/hit', 'pause'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'connassesacem_1', timestamp),
        ] >> Discard(),
    orl >> ProgramFilter(11) >> [ # SceneSwitch -> Dafist
        SceneSwitch(2) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],


    ]