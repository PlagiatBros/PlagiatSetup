#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

slowmotium_mk2lights = {
    1:'blue',
    3: 'white',
    4: 'white',
    5: 'white',
    6:'yellow',
    7:'yellow',
    8:'yellow',
}


#### Get Ur Freak On ####
geturfreakon = [
    Init([
        Program(seq24PageMap[8]) >> seq24once,
        Ctrl(0, 7) >> tapeutapecontrol,


        disable_microtonal,
        # zynmicrotonal_off,

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(slowmotium_mk2lights),
    ]),
    jeannot_padrelease >> mk2lights(slowmotium_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter([2]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # SlowMotium (bouclage bass) - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 4),
            SendOSC(slport, '/set', 'tempo', 75),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 75),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(75)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(75)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(75)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(75)),


            SendOSC(rpicourport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(rpijardinport, '/pyta/scene_recall', 'dafist_couplet'),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'no_budget'),


            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'slowmotium_main'),
            SendOSC(lightseqport, '/Lightseq/Bpm', 74),
            SendOSC(lightseqport, '/Lightseq/Play'),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            SendOSC(cmeinport, '/mididings/switch_scene', 8),

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
            bassscape,

            ] >> Discard(),
        [
            bassdetunest_off,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(11) >> [ # SceneSwitch -> HorroCore
        SceneSwitch(9) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],
    jeannot >> ProgramFilter(3) >> [ # Clap
        NoteOn(64, 127) >> Output('PBTapeutape', 3)
    ],
    jeannot >> ProgramFilter(4) >> [ # Kick
        NoteOn(54, 127) >> Output('PBTapeutape', 3)
    ],
    jeannot >> ProgramFilter(5) >> [ # Kick
        NoteOn(53, 127) >> Output('PBTapeutape', 3)
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
