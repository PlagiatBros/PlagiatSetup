#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

climat_mk2lights = {
    1:'blue',
    2:'purple',
    3:'purple',
    4:'purple',
    6:'white',
    8:'red',
}

darkEyes=""
dark_eyes = ['FreakyEye_1', 'BlueOnBlackEye_1', 'OrangeOnBlackEye_1', 'OrangeOnBlackEye_2', 'RedOnBlackEye_1']
for i in range (1,5):
    darkEyes+=dark_eyes[i]+" "

#### Climat ####
climat = [
    Init([
        Ctrl(0, 1) >> tapeutapecontrol,
        Program(seq24PageMap[3]) >> seq24once,

        enable_microtonal,
        set_microtonal(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '135.0\n200.0\n300.0\n400.0\n500.0\n600.0\n700.0\n835.0\n900.0\n1000.0\n1135.0\n2/1'),

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(climat_mk2lights),
    ]),
    jeannot_padrelease >> mk2lights(climat_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter([range(2,12)]) >> [
        SendOSC(lightseqport, '/Lightseq/Sequence/Disable', '*'),
        SendOSC(lightseqport, '/Lightseq/Scene/Stop', '*'),
        SendOSC(rpijardinport, '/pyta/slide/animate/stop', -1),
        SendOSC(rpicourport, '/pyta/slide/animate/stop', -1),
        SendOSC(rpijardinport, '/pyta/slide/visible', -1, 0),
        SendOSC(rpicourport, '/pyta/slide/visible', -1, 0),
        SendOSC(rpijardinport, '/pyta/text/reset', -1),
        SendOSC(rpicourport, '/pyta/text/reset', -1),
	SendOSC(qlcstopport, '/Stop'),
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    jeannot >> ProgramFilter(2) >> [ # Intro mandela - Bouton 2
        Program(69) >> cseqtrigger, # seq vocodeur à caler
        [
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),


            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off, #??
            vxorlvocode_on,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off, #??
            vxjeannotvocode_on,

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -2.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],


            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 13),

        ] >> Discard()

    ],
    orl >> ProgramFilter(6) >> [
	    SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_granmounoute') >> Discard(),
    ],
    orl >> ProgramFilter(7) >> [
	    SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_dignite') >> Discard(),
    ],
    orl >> ProgramFilter(8) >> [
	    SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_eternite') >> Discard(),
    ],
    orl >> [
        ProgramFilter(2),
        ProgramFilter(10)
        ] >> [ # preCouplet Wobble - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(mk2inport, '/mididings/switch_scene', 1),


            SendOSC(rpijardinport, '/pyta/slide/animate', 'FreakyEye_1 BlueOnBlackEye_1 OrangeOnBlackEye_1 OrangeOnBlackEye_2 RedOnBlackEye_1', 'scale_x', 800, 1200, 30),
            SendOSC(rpicourport, '/pyta/slide/animate', 'FreakyEye_1 BlueOnBlackEye_1 OrangeOnBlackEye_1 OrangeOnBlackEye_2 RedOnBlackEye_1', 'scale_x', 800, 1200, 30),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_plagiat'),
            SendOSC(lightseqport, '/Lightseq/Bpm', 300),
            SendOSC(rpijardinport, '/pyta/slide/alpha', darkEyes, 1),
            SendOSC(rpicourport, '/pyta/slide/alpha', darkEyes, 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'climat_theme_strobe',1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_theme_strobe'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'climat_theme_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_theme_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'climat_theme_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_theme_cour'),

            SendOscState([
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -2.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],
            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            SendOSC(vxjeannotmeufport, '/strip/VxJeannotVocod/AM%20pitchshifter/Pitch%20shift/unscaled', 1.20),
            SendOSC(vxorlmeufport, '/strip/VxORLVocod/AM%20pitchshifter/Pitch%20shift/unscaled', 1.20),

            bassdry,
            basswobble,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]

        ],
    jeannot >> ProgramFilter(3) >> [ # Couplet sans wobble - bouton 3
        #TODO arreter seq-wobble (à priori bassdry suffit)
        [
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_smell'),
            ] >> Discard(),

        Program(6) >> seq24once,
        Program(4) >> seq24once,
        [
            bassdry,
            bassscape,
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,

            vxorldelay_off,


	    vxjeannotverb_on,

        ] >> Discard()

    ],
    jeannot >> ProgramFilter(4) >> [ # Refrain - Bouton 4
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.x'),
#            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplestremoloport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplestremoloport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -12.],
                [samplestremoloport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', 0.0],
                [samplesscapeport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplespitchport, '/strip/SamplesPitch1/AM%20pitchshifter/Pitch%20shift/unscaled', 2.],
                [samplespitchport, '/strip/SamplesPitch2/AM%20pitchshifter/Pitch%20shift/unscaled', 2.],
                [samplespitchport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -10.6],
                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -40.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
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
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(3) >> [ # couplet - Bouton 3
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(trapcutport, '/Trapcut/Bpm', 300),

            SendOSC(mk2inport, '/mididings/switch_scene', 2),

            SendOSC(slport, '/sl/0/set', 'sync', 0),
            SendOSC(slport, '/sl/0/hit', 'pause_off'),
            SendOSC(slport, '/sl/0/hit', 'trigger'),
            SendOSC(slport, '/sl/0/set', 'sync', 1),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),


            SendOscState([
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -2.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],
            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),


            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            vxjeannotverb_on,

            bassdry,
            bassscape,

            #TODO bassSUB

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(4) >> [ # The shit - Bouton 4
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplestremoloport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -7.50],
                [samplestremoloport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -6.],
                [samplespitchport, '/strip/SamplesPitch1/AM%20pitchshifter/Pitch%20shift/unscaled', 2],
                [samplespitchport, '/strip/SamplesPitch2/AM%20pitchshifter/Pitch%20shift/unscaled', 2.3],
            ]),


            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_on,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_on,

            bassdry,
            bassscape,


            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_off,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],

    jeannot >> ProgramFilter(6) >> [ # shut your dickhole -> Le5
        SceneSwitch(5) >> Discard(),
        Ctrl(102, 127) >> Output('Mk2CtrlOut', 1)
    ],

    jeannot >> ProgramFilter(8) >> SendOSC(trapcutport, '/Trapcut/Scene/Play', 'I') >> Discard(),

    ]
