#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################


wholeworld_mk2lights = {
    1:'blue',
    2:'purple',
    3: 'purple',
    4: 'purple',
    # 5: 'green',
    6:'yellow',
    7:'yellow',
    8:'yellow',
}


#### Whole World ####
wholeworld = [
    Init([
        Program(seq24PageMap[10]) >> seq24once,
        Ctrl(0, 5) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0, 0, 0.35, 0, 0, 0, 0, 0, 0, 0.35, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '135.0\n200.0\n300.0\n400.0\n500.0\n635.0\n700.0\n800.0\n900.0\n1000.0\n1100.0\n2/1'),


        SendOSC(mk2inport, '/mididings/switch_scene', 4),

        mk2lights(wholeworld_mk2lights),

        SendOSC(rpijardinport, '/pyta/slide/*/reset'),
        SendOSC(rpijardinport, '/pyta/text/*/reset'),
        SendOSC(rpijardinport, '/pyta/post_process/reset'),
        SendOSC(rpicourport, '/pyta/slide/*/reset'),
        SendOSC(rpicourport, '/pyta/text/*/reset'),
        SendOSC(rpicourport, '/pyta/post_process/reset'),

    ]),
    jeannot_padrelease >> mk2lights(wholeworld_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([4]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    # jeannot_sustain >> [
    #     ## ça peut servir...?
    #     ] >> Discard(),
    orl >> ProgramFilter(2) >> [ # Pont cymbaloume - Bouton 2
        Program(65) >> cseqtrigger,
        [NoteOff(57), NoteOff(59)] >> Output('PBTapeutape', 1), # intro cymbalum off
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(90)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(90)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(90)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(90)),

            SendOSC(rpijardinport, '/pyta/scene_recall', 'wholeworld_intro_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'wholeworld_intro_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'wholeworld_pont'),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
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
    orl >> ProgramFilter(3) >> [ # Couplet - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(90)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(90)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(90)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(90)),


            # SendOSC(rpijardinport, '/pyta/scene_recall', 'wholeworld_intro_jardin'),
            # SendOSC(rpicourport, '/pyta/scene_recall', 'wholeworld_intro_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'wholeworld_couplet'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_couplet_anim'),
            SendOSC(lightseqport, '/Lightseq/Bpm', 90),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
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
    jeannot >> ProgramFilter(2) >> [ # sequence synthé toggle - bouton 2
        Program(14) >> seq24once,
        [
            SendOSC(rpijardinport, '/pyta/scene_recall', 'wholeworld_couplet_synth_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'wholeworld_couplet_synth_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'wholeworld_couplet_synth_fade'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_couplet_anim_surcouche'),

        ] >> Discard()
    ],
    orl >> ProgramFilter(4) >> [ # Refrain - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),


            SendOSC(audioseqport, '/Audioseq/Scene/Stop', '*'),
            SendOSC(audioseqport, '/Audioseq/Bpm', 90),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),
            SendOSC(audioseqport, '/Audioseq/Sequence/Enable', 'wholeworld_refrain'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(90)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(90)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(90)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(90)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 5),



            SendOSC(rpijardinport, '/pyta/scene_recall', 'wholeworld_refrain_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'wholeworld_refrain_cour'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_refrain'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'wholeworld_refrain_eyes_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'wholeworld_refrain_eyes_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_refrain_eyes_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_refrain_eyes_cour'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_refrain_anim'),


            SendOSC(lightseqport, '/Lightseq/Bpm', 90),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
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

    jeannot >> ProgramFilter(3) >> [ # Trap - Bouton 3

        SendOSC(rpijardinport, '/pyta/scene_recall', 'wholeworld_trap_jardin'),
        SendOSC(rpicourport, '/pyta/scene_recall', 'wholeworld_trap_cour'),

        ],
    orlCtrl >> CtrlFilter(110) >> [
        SendOSC(qlcport, '/damper', '/TuttiProche/White/Segment/{2,8}', lambda ev: max(0, ev.value / 101. - 26/101.)),
        SendOSC(qlcport, '/damper', '/TuttiLointain/{Green,Blue}/Segment/{4,5}', lambda ev: max(0, ev.value / 101. - 26/101.)),
        SendOSC(qlcport, '/damper', '/TuttiLointain/Red/Segment/{4,5}', lambda ev: max(0, ev.value / 101. - 26/101.)),
    ] >> Discard(),
    jeannot >> ProgramFilter(4) >> [ # Boomboclatsome - Bouton 4


        SendOSC(rpijardinport, '/pyta/scene_recall', 'wholeworld_boomboclaat_jardin'),
        SendOSC(rpicourport, '/pyta/scene_recall', 'wholeworld_boomboclaat_cour'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'wholeworld_boomboclaat_glitch'),


        SendOSC(lightseqport, '/Lightseq/Scene/Stop', 'wholeworld_couplet'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'wholeworld_boomboclaat'),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_couplet_anim'),


        vxorlgars_on,
        vxorlmeuf_off,
        vxorldisint_off,
        vxorldelay_off,
        vxorlvocode_off,

    ] >> Discard(),
    orl >> ProgramFilter(11) >> [ # SceneSwitch -> Dafist
        SceneSwitch(2) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
    ],
    jeannot >> ProgramFilter(6) >> [ # Vx jeannot
        vxjeannotdelay_off,
        vxjeannotgars_on,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(7) >> [ # Vx jeannot
        vxjeannotgars_off,
        vxjeannotmeuf_on,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(8) >> [ # Vx jeannot
        vxjeannotgars_off,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_on,
    ] >> Discard(),
]
