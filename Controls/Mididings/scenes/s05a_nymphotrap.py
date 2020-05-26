#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

nymphotrap_mk2lights = {
    1:'blue',
    2:'yellow',
    3:'yellow',
    4:'yellow',
    5:'white',
    6:'purple',
    7:'white',
    # 8:'purple',
}

#### Nymphotrap ####
nymphotrap = [
    Init([
        Program(seq24PageMap[5]) >> seq24once,
        Ctrl(0, 3) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0.35, 0, 0.35, 0, 0, 0, 0, 0.35, 0, 0, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '100.0\n200.0\n300.0\n435.0\n500.0\n635.0\n700.0\n800.0\n900.0\n1000.0\n1135.0\n2/1'),

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(nymphotrap_mk2lights),
        ]),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    jeannot_padrelease >> mk2lights(nymphotrap_mk2lights),
    [orl >> ProgramFilter([range(1,12)]), jeannot >>  ProgramFilter([1,5,6,7])] >> Filter(PROGRAM) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
        SendOSC(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(surfaceorlport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.),
        SendOSC(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxpitchshifterport, '/x42/pitch', 1.),
        SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.),

    ] >> Discard(),
    orl >> ProgramFilter([2,3,11]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([range(5,8)]) >> light_reset >> Discard(),
    orl >> ProgramFilter(2) >> [ # Cloud rap ballade rhodes - Bouton 2
        stop,
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 60),

            SendOSC(klickport, '/klick/simple/set_tempo', 60),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),
            SendOSC(cmeinport, '/mididings/switch_scene', 10),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(60)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(60)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(60)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(60)),


            SendOSC(monitorsjeannotport, '/strip/Klick/Gain/Mute', 1.0),


            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_ballade_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_ballade_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_ballade_timer', 1),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_slow_bouclage', 1), # reset
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_slow_intro'),
            SendOSC(lightseqport, '/Lightseq/Bpm', 60),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            ] >> Discard(),
        [

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

            ] >> Discard()
        ],
    orl >> ProgramFilter(8) >> [ # Bouclage rhodes  - Bouton 8
            SendOSC(slport, '/sl/8/hit', 'record'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_ballade_timer'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_slow_bouclage'),
        ],
    jeannot >> ProgramFilter(2) >> [ # Vx jeannot
        vxjeannotdelay_off,
        vxjeannotgars_on,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(3) >> [ # Vx jeannot
        vxjeannotgars_off,
        vxjeannotmeuf_on,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(4) >> [ # Vx jeannot
        vxjeannotgars_off,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_on,
    ] >> Discard(),
    jeannot >> [ProgramFilter(5), ProgramFilter(6), ProgramFilter(7)]>> [ # nymphotrap bouliotte - bouton 5
        Program(75) >> cseqtrigger,
        [
            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOSC(mk2inport, '/mididings/switch_scene', 9), # sample cut
            SendOSC(cmeinport, '/mididings/switch_scene', 8),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            basswobble,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
    ],
    jeannot >> ProgramFilter(5) >> [ # intro chant/synth - bouton 5
        SendOSC(slport, '/set', 'eighth_per_cycle', 8),
        SendOSC(slport, '/set', 'tempo', 120),
        SendOSC(slport, '/sl/[7,8]/hit', 'pause_on'),

        SendOSC(rpicourport, '/pyta/scene_recall', 'le5_rabza_money'),
        SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_rabza_money'),

        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_rabza_red_flash_anim'),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_rabza_red_ct_anim'),

        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_rabza_fixe'),
        SendOSC(lightseqport, '/Lightseq/Bpm', 120),
        SendOSC(lightseqport, '/Lightseq/Play', timestamp),

        vxorlgars_off,
        vxorlmeuf_on,
        vxorldisint_off,
        vxorldelay_off,
        vxorlvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(6) >> [ # refrain (i is da one)/ 2e couplet  (there's a hole)- bouton 6
        SendOSC(slport, '/set', 'eighth_per_cycle', 10),
        SendOSC(slport, '/set', 'tempo', 120),
        SendOSC(slport, '/sl/[7,8]/hit', 'pause_on'),

        SendOSC(rpicourport, '/pyta/scene_recall', 'le5_rabza_refrain'),
        SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_rabza_refrain'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_rabza_refrain_switcher'),

        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_rabza_red_flash_anim'),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_rabza_couplet_ct_flash_anim'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_rabza_refrain_strobe'),

        SendOSC(lightseqport, '/Lightseq/Bpm', 120),
        SendOSC(lightseqport, '/Lightseq/Play', timestamp),

        vxorlgars_on,
        vxorlmeuf_off,
        vxorldisint_off,
        vxorldelay_off,
        vxorlvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(7) >> [ # nymphotrap avec orl vx vocod (couplet) / banana boat - bouton 7
        [Program(84), Program(85)] >> seq24once,
        [
        SendOSC(slport, '/set', 'eighth_per_cycle', 10),
        SendOSC(slport, '/set', 'tempo', 120),
        SendOSC(slport, '/sl/[7,8]/hit', 'pause_on'),


        SendOSC(rpicourport, '/pyta/scene_recall', 'le5_rabza_couplet'),
        SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_rabza_couplet'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_rabza_refrain_disable'),

        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_rabza_red_flash_anim'),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_rabza_couplet_ct_flash_anim'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_rabza_couplet_fixe'),

        SendOSC(lightseqport, '/Lightseq/Bpm', 120),
        SendOSC(lightseqport, '/Lightseq/Play', timestamp),

        vxorlgars_off,
        vxorlmeuf_off,
        vxorldisint_off,
        vxorldelay_off,
        vxorlvocode_on,
        vxjeannotmeuf_on,
        vxjeannotgars_off,
        ] >> Discard(),
    ],
#    jeannot >> ProgramFilter(8) >> [ # nymphotrap (couplet part 2, trig boucles bouliottes) - bouton 8
#        SendOSC(slport, '/sl/7/hit', 'trigger'),
#    ] >> Discard(),

    orl >> ProgramFilter(9) >> [ # Bouclage synth  - Bouton 9
            SendOSC(slport, '/sl/7/hit', 'record'), # synth aigu
        ],
    orl >> ProgramFilter(3) >> [ # thème ragga - bouton 3
        Program(76) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(slport, '/sl/8/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'le5_rabza_theme'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'le5_rabza_theme'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_theme_danse'),

            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_rabza_theme_anim'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_rabza_couplet_ct_flash_anim'),

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            basswobble,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
    ],
    orl >> ProgramFilter(4) >> [ # VxOrlGars on  - Bouton 4
            vxorlgars_on,
        ],
    orl >> ProgramFilter(5) >> [ # VxOrlGars off - Bouton 5
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'le5_fartingart'),
            SendOSC(cmeinport, '/mididings/switch_scene', 2),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_on,
        ],
    orl >> ProgramFilter(11) >> [ # Instouboul - bouton 11
        SceneSwitch(61) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],

    ]
