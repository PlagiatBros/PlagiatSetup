#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

horrorcore_mk2lights = {
    1:'blue',
    2:'purple',
    3:'purple',
    4:'purple',
    5:'purple',
    6:'yellow',
    7:'yellow',
    8:'yellow',
}

#### HorroCore ####
horrorcore = [
    Init([
        Program(seq24PageMap[9]) >> seq24once,
        Ctrl(0, 9) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0, 0, 0, 0, 0.35, 0, 0, -0.35, 0, 0.35, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '135.0\n200.0\n300.0\n400.0\n500.0\n600.0\n700.0\n835.0\n900.0\n1000.0\n1065.0\n2/1'),

        SubSceneSwitch(2),
        mk2lights(horrorcore_mk2lights),
    ]),
    jeannot_padrelease >> mk2lights(horrorcore_mk2lights),
    orl >> ProgramFilter([range(1,12)]) >> [
        SendOSC(mk2inport, '/mididings/switch_scene', 4),
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
        SubSceneSwitch(2),
    ] >> Discard(),
    jeannot >> ProgramFilter([range(1,9)]) >> [
        SendOSC(mk2inport, '/mididings/switch_scene', 4),
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
    ] >> Discard(),
    jeannot >> ProgramFilter([range(1,6)]) >> [
        SubSceneSwitch(2),
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter([range(2,12)]) >> [
        SendOSC(lightseqport, '/Lightseq/Sequence/Disable', '*'),
        SendOSC(lightseqport, '/Lightseq/Scene/Stop', '*'),
        SendOSC(rpijardinport, '/pyta/slide/animate/stop'),
        SendOSC(rpicourport, '/pyta/slide/animate/stop'),
        SendOSC(rpijardinport, '/pyta/slide/visible', -1, 0),
        SendOSC(rpicourport, '/pyta/slide/visible', -1, 0),
        SendOSC(rpijardinport, '/pyta/text/reset', -1),
        SendOSC(rpicourport, '/pyta/text/reset', -1),
	SendOSC(qlcstopport, '/Stop'),	         
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    [orl, jeannot] >> ProgramFilter(2) >> [ # Couplet (orl meuf) - Bouton 2 (mk2 notes = vx jean meuf; vx orl vocod; stop samples)
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
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(mk2inport, '/mididings/switch_scene', 5),

            SendOSC(rpijardinport, '/pyta/text', 0, 'PLAGIAT'),
            SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),
            SendOSC(rpicourport, '/pyta/text', 0, 'PLAGIAT'),
            SendOSC(rpicourport, '/pyta/text/visible', 0, 1),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'hc_notheft'),
            

            

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],

                # [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                #
                # [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -15.0],

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
    orl >> ProgramFilter(3) >> [ # Stupid donkey - Bouton 3
        Program(5) >> cseqtrigger,
        [
#            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
#            SendOSC(slport, '/set', 'tempo', 150),
#            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

#            SendOSC(klickport, '/klick/simple/set_tempo', 150),
#            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
#            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
#            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'hc_wood_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'hc_wood_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'hc_wood_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'hc_wood_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesreversedelayport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],


            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
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
    jeannot >> ProgramFilter(3) >> [ # Refrain - Bouton 3
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
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(lightseqport, '/Lightseq/Bpm', 75),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'hc_wood_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'hc_wood_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'hc_wood_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'hc_wood_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesreversedelayport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', 0.0],


            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_on,

            bassdry,

            SendOSC(cmeinport, '/mididings/switch_scene', 5),



            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    jeannot >> ProgramFilter(4) >> [ # Couplet 2 - Bouton 4
        Program(69) >> cseqtrigger,

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
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(cmeinport, '/mididings/switch_scene', 7),
            SendOSC(mk2inport, '/mididings/switch_scene', 6),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],

                # [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                #
                # [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -15.0],

            ]),


            vxorlmeuf_on,
            vxorlgars_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

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
    jeannot >> ProgramFilter(5) >> [ # Yep (orl meuf) - Bouton 5
        Program(70) >> cseqtrigger,
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
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0],

                # [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                #
                # [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -12.0],
                # [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -15.0],

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
    orl >> ProgramFilter(5) >> [ # Refrain grand messe - bouton 5
        stop,
        Program(72) >> cseqtrigger,
        [


            SendOscState([

            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 12),

            vxorlmeuf_off,
            vxorlgars_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_on,

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
        Program(71) >> cseqtrigger,
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
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            vxorlmeuf_off,
            vxorlgars_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_off,

            SubSceneSwitch(1),

            ] >> Discard()
        ],
    orl >> ProgramFilter(7) >> [ # relance boucles

            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(slport, '/sl/[0,3,5]/set', 'sync', 0),
            SendOSC(slport, '/sl/[0,3,5]/hit', 'pause_off'),
            SendOSC(slport, '/sl/[0,3,5]/hit', 'trigger'),
            SendOSC(slport, '/sl/[0,3,5]/set', 'sync', 1),

        ] >> Discard(),
    jeannot >> ProgramFilter(6) >> [
        vxjeannotdelay_off,
        vxjeannotgars_on,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(7) >> [
        vxjeannotgars_off,
        vxjeannotmeuf_on,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(8) >> [
        vxjeannotgars_off,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_on,
    ] >> Discard(),
    ]
