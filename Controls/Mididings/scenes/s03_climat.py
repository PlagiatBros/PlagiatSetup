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
    5:'green',
    6:'purple',
    7:'white',
    8:'white',
}


climat_metro = [
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
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150))
]
climat_metro_2 = [
    SendOSC(slport, '/set', 'eighth_per_cycle', 74),
    SendOSC(slport, '/set', 'tempo', 150),
    SendOSC(slport, '/sl/-1/hit', 'pause_on'),

    SendOSC(klickport, '/klick/simple/set_tempo', 150),
    SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
    SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.xX.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.x'),
    SendOSC(klickport, '/klick/metro/start'),

    SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
    SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
    SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150))
]


#### Climat ####
climat = [
    Init([
        Ctrl(0, 1) >> tapeutapecontrol,
        Program(seq24PageMap[3]) >> seq24once,

        enable_microtonal,
        set_microtonal(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0),

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(climat_mk2lights),
    ]),
    jeannot_padrelease >> mk2lights(climat_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([2,4,7]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    jeannot >> ProgramFilter(2) >> [ # Intro mandela - Bouton 2
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/metro/stop'),


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

            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_intro'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_intro'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_intro'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_intro_fixe'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 150 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOSC(surfaceorlport, '/mandela_modal', 1),


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

            bassdry,

        ] >> Discard()

    ],
    orl >> [ProgramFilter(2), ProgramFilter(10)] >> [ # preCouplet Wobble - Bouton 2
        Program(65) >> cseqtrigger,
        [

            climat_metro,

            SendOSC(mk2inport, '/mididings/switch_scene', 1),

            SendOSC(surfaceorlport, '/mandela_modal', 0),


            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_precouplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_precouplet'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_precouplet'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_precouplet_moise'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_theme_fixe'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_theme_strobelights_alea_trig'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_theme_anim'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 150 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


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

            bassdry,
            basswobble,

            ] >> Discard(),

        ],
    jeannotCtrl >> CtrlFilter(1) >> [
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_wobble_strobe', lambda ev: ev.value),
    ] >> Discard(),
    jeannot >> ProgramFilter(3) >> [ # Couplet Ia (smell it smell it)  - bouton 3
        Program(66) >> cseqtrigger,
        [

            climat_metro_2,

            SendOscState([
                [monosynthpitcherport, '/monosynth/control', 'traphigh', 'filterFreq', 2]
                ]), # mute samples

            SendOSC(audioseqport, '/Audioseq/Bpm', 150),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'climat_couplet1b', timestamp),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),

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


        ] >> Discard()

    ],
    orl >> ProgramFilter(93) >> [ # Couplet Ib (smell it quick) - Bouton 93 (auto)
        Program(66) >> cseqtrigger,
        [
            climat_metro_2,


            SendOscState([
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -6.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],

                [monosynthpitcherport, '/monosynth/control', 'traphigh', 'filterFreq', 12]

            ]), # unmute samples

            SendOSC(mk2inport, '/mididings/switch_scene', 4), # samples/keys cut
        ] >> Discard(),

    ],
    orl >> ProgramFilter(3) >> [ # Couplet Ic (see it's easy) - Bouton 3
        [
            Program(9),
            Program(10),
            Program(11),
            Program(12),

            Program(14),
            Program(15),
            Program(16)
            ] >> seq24once,
        [
            SendOSC(mk2inport, '/mididings/switch_scene', 4), # samples/keys cut
        ] >> Discard(),

    ],
    jeannot >> ProgramFilter(4) >> [ # Refrain - Bouton 4
        Program(67) >> cseqtrigger,
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


            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_refrain_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_refrain_cour'),
            # SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_precouplet'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_refrain_bardanse'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_refrain_fixe'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_refrain_anim'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 150 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),



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

                [monosynthpitcherport, '/monosynth/control', 'traphigh', 'filterFreq', 12],
#                [bassmainport, '/strip/Trapsynth_barkline/Gain/Mute', 0.0],
                [keyboardsport, '/strip/Trapsynth_fifth/Gain/Mute', 0.0],


            ]),

            vxorlgars_on,
            vxorlmeuf_off,
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
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(4) >> [ # Couplet II - Bouton 4
        Program(68) >> cseqtrigger,
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



            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_precouplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_precouplet'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_precouplet'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_precouplet_dimmer'),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_theme_fixe'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_theme_anim'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_couplet1'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 150 * 2),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(audioseqport, '/Audioseq/Bpm', 150),

            SendOscState([
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0],

                [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0],
                [samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -2.0],
                [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0],

                [monosynthpitcherport, '/monosynth/control', 'traphigh', 'filterFreq', 12]

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_on,
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
    jeannot >> ProgramFilter(5) >> [ # Couplet IIb (boutros boutros) - Bouton 5
        SendOSC(audioseqport, '/Audioseq/Scene/Play', 'climat_couplet2b', timestamp),
        SendOSC(trapcutport, '/Trapcut/Scene/Play', 'IIII', timestamp),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_boutros_cut', timestamp),
    ],

    ## goto Mpko

    orl >> ProgramFilter(5) >> [
        SceneSwitch(31) >> Discard(),
        Program(5) >> Output('PBCtrlOut', 1)
    ]


]
