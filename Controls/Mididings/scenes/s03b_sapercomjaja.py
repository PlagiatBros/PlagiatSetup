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
sapercomjaja = [
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

    orl >> ProgramFilter(5) >> [ # Solo ethiotrap
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_climax_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_climax_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_glitch1'),


            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_climax_anim'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_fixe'),



            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(surfaceorlport, '/mandela_modal', 0),


            SendOscState([

                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],

            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 7),
            SendOSC(mk2inport, '/mididings/switch_scene', 8),

            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            bassdry,


            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_off,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],

    orl >> ProgramFilter(6) >> [ # Mandela-A-A-A-A  - Bouton 6
        Program(72) >> cseqtrigger,
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

            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_mandela_danse'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_mandela_danse'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_mandela_danse'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_mandela_danse'),


            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_mandela_a_a_anim'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_mandela_a_a_basse_anim'),



            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(surfaceorlport, '/mandela_modal', 0),


            SendOscState([

                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],

            ]),


            SendOSC(cmeinport, '/mididings/switch_scene', 16),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_on,


            bassdry,


            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_off,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(7) >> [ # There will be 21  - Bouton 7
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),

            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_climax_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_climax_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_glitch1'),


            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_climax_anim'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_fixe'),



            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(surfaceorlport, '/mandela_modal', 0),


            SendOscState([

                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [bassmainport, '/strip/Trapsynth_barkline/Gain/Mute', 0.0],

            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 16),
            SendOSC(mk2inport, '/mididings/switch_scene', 8),

            vxorlgars_off,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            bassdry,


            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_off,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],

    orl >> ProgramFilter(8) >> [ # Climax  - Bouton 8
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),


            SendOSC(trapcutport, '/Trapcut/Bpm', 300. * 4 / 3),

            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_climax_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_climax_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_glitch1'),


            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_climax_anim'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_fixe'),



            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(surfaceorlport, '/mandela_modal', 0),


            SendOscState([

                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [bassmainport, '/strip/Trapsynth_barkline/Gain/Mute', 0.0],

            ]),

            SendOSC(cmeinport, '/mididings/switch_scene', 16),
            SendOSC(mk2inport, '/mididings/switch_scene', 8),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,

            bassdry,


            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_off,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(9) >> [ # mama zbaking eggz
        SendOSC(trapcutport, '/Trapcut/Scene/Play', 'III', timestamp),
    ] >> Discard(),
    orl >> ProgramFilter(10) >> [ # rimdogged
            stop, [
                    SendOSC(slport, '/set', 'eighth_per_cycle', 8),
                    SendOSC(slport, '/set', 'tempo', 150),

                    SendOSC(klickport, '/klick/simple/set_tempo', 150),
                    SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
                    SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
                    SendOSC(klickport, '/klick/metro/start'),

                    vxjeannotdelay_off,
                    vxjeannotgars_off,
                    vxjeannotmeuf_off,
                    vxjeannotvocode_on,
                    vxjeannotdisint_on,


                    SendOSC(cmeinport, '/mididings/switch_scene', 17),

            ] >> Discard(),
        ],
    orl >> ProgramFilter(11) >> [ # Mandela-A-A-A-A II
        Program(74) >> cseqtrigger,
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

            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_mandela_danse'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_mandela_danse'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_mandela_danse'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_mandela_danse'),


            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_mandela_a_a_anim'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_mandela_a_a_basse_anim'),



            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(surfaceorlport, '/mandela_modal', 0),


            SendOscState([

                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],

            ]),


            SendOSC(cmeinport, '/mididings/switch_scene', 7),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_on,


            bassdry,


            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_off,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],

    jeannot >> ProgramFilter(6) >> [ # sythé DRE - Bouton 6
        Program(73) >> cseqtrigger,
        Program(70) >> seq24once,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 3, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(150)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(150)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(150)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(150)),


            SendOSC(trapcutport, '/Trapcut/Bpm', 300. * 4 / 3),

            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_climax_jardin'),
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_climax_cour'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_glitch1'),


            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'climat_climax_anim'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_fixe'),



            SendOSC(lightseqport, '/Lightseq/Bpm', 150),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOSC(surfaceorlport, '/mandela_modal', 0),


            SendOscState([

                [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0],
                [bassmainport, '/strip/Trapsynth_barkline/Gain/Mute', 0.0],

            ]),

        ],
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_up'),
        SendOSC(lightseqport, '/Lightseq/Scene/Stop', 'climat_climax_glitch1'),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_glitch2'),

    ],
    jeannot >> ProgramFilter(7) >> [ # cock ya gun - Bouton 7

            # stop,
            SendOSC(rpicourport, '/pyta/scene_recall', 'climat_cock'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'climat_cock'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'climat_climax_cock'),
            NoteOn(65,127) >> Output('PBTapeutape', 3),
    ],
    jeannot >> ProgramFilter(8) >> [ # shut your dickhole -> Le5
	[
            SendOSC(audioseqport, '/Audioseq/Scene/Stop', '*'),
            SendOSC(samplesmainport,'/strip/SamplesMain/Calf%20Filter/Frequency/unscaled', 20000.),
            SendOSC(samplesmainport,'/strip/Keyboards/Calf%20Filter/Frequency/unscaled', 20000.),
	] >> Discard(),
        SceneSwitch(5) >> Discard(),
        Ctrl(102, 127) >> Output('Mk2CtrlOut', 1),
    ],


]
