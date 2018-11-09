#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################


wholeworld_mk2lights = {
    1:'blue',
    2:'purple',
    3: 'green',
    4: 'green',
    5: 'green',
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

        mk2lights(wholeworld_mk2lights),
        SendOSC(rpijardinport, '/pyta/slide/unload', -1),
        SendOSC(rpicourport, '/pyta/slide/unload', -1),
    ]),
    jeannot_padrelease >> mk2lights(wholeworld_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    jeannot_sustain >> [ # Intro cymbaloume - Sustain
        SendOSC(rpijardinport, "/Test"),
        SendOSC(lightseqport, "/Lightseq/Scene/Play", "intro_urinoir"),
#        SendOSC(lightseqport, "/Lightseq/Play", timestamp)
        ] >> Discard(),

    orl >> ProgramFilter(2) >> [ # Pont cymbaloume - Bouton 2
        Program(65) >> cseqtrigger,
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

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

            ]),

            SendOSC(rpijardinport, '/pyta/text/visible', -1, 0),
            SendOSC(rpicourport, '/pyta/text/visible', -1, 0),

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
            SendOSC(rpijardinport, '/pyta/slide/animate', 'FreakyEye_1 BlueOnBlackEye_1 OrangeOnBlackEye_1 OrangeOnBlackEye_2 RedOnBlackEye_1', 'alpha', 0, 0.5, 13),
            SendOSC(rpicourport, '/pyta/slide/animate', 'FreakyEye_1 BlueOnBlackEye_1 OrangeOnBlackEye_1 OrangeOnBlackEye_2 RedOnBlackEye_1', 'alpha', 0, 0.5, 13),

            SendOSC(lightseqport, '/Lightseq/Bpm', 1200),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'wholeworld_reveil_sournois_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_reveil_sournois_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'wholeworld_reveil_sournois_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_reveil_sournois_cour'),
            ] >> Discard()

    ],
    jeannot >> ProgramFilter(3) >> [ # sniffed, eaten, mixed, jerked off - bouton 3
        SendOSC(lightseqport, '/Lightseq/Bpm', 90),
        SendOSC(lightseqport, '/Lightseq/Play', timestamp) >> Discard(),
        SendOSC(lightseqport, "/Lightseq/Scene/Play", "wholeworld_jerked_off") >> Discard()
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

            # SendOSC(rpijardinport, '/pyta/slide/alpha', -1, 1),
            # SendOSC(rpicourport, '/pyta/slide/alpha', -1, 1),

            # SendOSC(rpijardinport, '/pyta/slide/visible', 'Kama_1', 1),
            # SendOSC(rpicourport, '/pyta/slide/visible', 'Kama_1', 1),

            # SendOSC(rpijardinport, '/pyta/slide/position_z', 'Kama_1', -1),
            # SendOSC(rpicourport, '/pyta/slide/position_z', 'Kama_1', -1),

            # SendOSC(rpijardinport, '/pyta/slide/animate', 'Kama_1', 'rotate_z', 0, 1080, 60),
            # SendOSC(rpicourport, '/pyta/slide/animate', 'Kama_1', 'rotate_z', 0, 1080, 60),

            SendOSC(rpijardinport, '/pyta/slide/animate', 'FreakyEye_1 BlueOnBlackEye_1 OrangeOnBlackEye_1 OrangeOnBlackEye_2 RedOnBlackEye_1', 'scale_x', 800, 1200, 30),
            SendOSC(rpicourport, '/pyta/slide/animate', 'FreakyEye_1 BlueOnBlackEye_1 OrangeOnBlackEye_1 OrangeOnBlackEye_2 RedOnBlackEye_1', 'scale_x', 800, 1200, 30),

            # SendOSC(rpijardinport, '/pyta/slide/scale', 'Kama_1', 1600, 1200, 1),
            # SendOSC(rpicourport, '/pyta/slide/scale', 'Kama_1', 1600, 1200, 1),

            # SendOSC(rpijardinport, '/pyta/slide/alpha', 'Kama_1', 0.45),
            # SendOSC(rpicourport, '/pyta/slide/alpha', 'Kama_1', 0.45),

            # SendOSC(rpijardinport, '/pyta/slide/rgb', 'Kama_1', 0.5, 0, 0),
            # SendOSC(rpicourport, '/pyta/slide/rgb', 'Kama_1', 0.5, 0, 0),

#            SendOSC(rpijardinport, '/pyta/slide/scale', 'FreakyEye_1 BlueOnBlackEye_1 OrangeOnBlackEye_1 OrangeOnBlackEye_2 RedOnBlackEye_1', 800, 600, 1),
#            SendOSC(rpicourport, '/pyta/slide/scale', 'FreakyEye_1 BlueOnBlackEye_1 OrangeOnBlackEye_1 OrangeOnBlackEye_2 RedOnBlackEye_1', 800, 600, 1),

            SendOSC(lightseqport, '/Lightseq/Bpm', 90),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'wholeworld_reveil_sournois_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_reveil_sournois_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'wholeworld_reveil_sournois_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_reveil_sournois_cour'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'wholeworld_refrain'),
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

    jeannot >> ProgramFilter(4) >> [ # One sheet - Bouton 4
        SendOSC(lightseqport, '/Lightseq/Bpm', 90),
        SendOSC(lightseqport, '/Lightseq/Play', timestamp) >> Discard(),
        SendOSC(lightseqport, "/Lightseq/Scene/Play", "wholeworld_one_sheet") >> Discard()
        ],

    jeannot >> ProgramFilter(5) >> [ # Trap - Bouton 5
        # SendOSC(lightseqport, '/Lightseq/Bpm', 90),
        # SendOSC(lightseqport, '/Lightseq/Play', timestamp) >> Discard(),
        # SendOSC(lightseqport, "/Lightseq/Sequence/Enable", "wholeworld_trap") >> Discard()
        SendOSC(rpijardinport, '/pyta/slide/visible', 'BlindEye_1', 1),
        SendOSC(rpijardinport, '/pyta/slide/scale', 'BlindEye_1', 1200, 800, 1),
        SendOSC(rpijardinport, '/pyta/slide/position', 'BlindEye_1', 300, 0, 0),
        SendOSC(rpijardinport, '/pyta/slide/animate', 'BlindEye_1', 'scale_x', 1200, 1400, 30),
        SendOSC(rpicourport, '/pyta/slide/visible', 'BlindEye_1', 1),
        SendOSC(rpicourport, '/pyta/slide/scale', 'BlindEye_1', 1200, 800, 1),
        SendOSC(rpicourport, '/pyta/slide/position', 'BlindEye_1', -450, 0, 0),
        SendOSC(rpicourport, '/pyta/slide/animate', 'BlindEye_1', 'scale_x', 1200, 1400, 30),
        ],

    orl >> ProgramFilter(5) >> [ # Outro - Bouton 5
        stop,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(90)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(90)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(90)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(90)),

            SendOscState([

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 8),

            vxorlgars_on,
            vxorlmeuf_on,
            vxorldisint_on,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotdelay_on,
            vxjeannotgars_on,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,

            bassdry,
            bassscape,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(6) >> [ # Bouclage synths - bouton 6
        SendOSC(slport, '/sl/7/hit', 'record')
        ] >> Discard(),
    orl >> ProgramFilter(7) >> [ # Overdub synths - bouton 7
        SendOSC(slport, '/sl/7/hit', 'overdub')
        ] >> Discard(),
    orl >> ProgramFilter(8) >> [ # Intro cymbaloume - Via Séquenceur - Bouton 8
        Program(65) >> cseqtrigger,
        [
            NoteOff(59),
            NoteOff(58),
            ] >> tapeutapecontrol,
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

            SendOSC(lightseqport, "/Lightseq/Scene/Play", "intro_plagiat"),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0],

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
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(11) >> [ # SceneSwitch -> Dafist
        SceneSwitch(2) >> Discard(),
        Program(3) >> Output('PBCtrlOut', 1)
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
