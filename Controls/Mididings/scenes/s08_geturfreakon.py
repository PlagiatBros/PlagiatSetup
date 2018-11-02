#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

#### Get Ur Freak On ####
geturfreakon = [
    Init([
        Program(seq24PageMap[8]) >> seq24once,
        Ctrl(0, 7) >> tapeutapecontrol,


        disable_microtonal,
        # zynmicrotonal_off,

        SendOSC(mk2inport, '/mididings/switch_scene', 6),
        mk2lights([1]),
    ]),
    jeannot_padrelease >> mk2lights([1]),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    [orl, jeannot] >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
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


            SendOSC(rpijardinport, '/pyta/slide/animate', 'TearEye_1', 'alpha', 0, 1, 180 ),
            SendOSC(rpijardinport, '/pyta/slide/visible', 'TearEye_1', 1),
            SendOSC(rpicourport, '/pyta/slide/animate', 'TearEye_1', 'alpha', 0, 1, 180 ),
            SendOSC(rpicourport, '/pyta/slide/visible', 'TearEye_1', 1),


            SendOSC(rpijardinport, '/pyta/text/align', 2, 'left', 'top'),
            SendOSC(rpijardinport, '/pyta/text', 2, '[plaʒia]                             '),
            SendOSC(rpijardinport, '/pyta/text/animate', 2, 'zoom', 0.8, 0.1, 4),
            SendOSC(rpijardinport, '/pyta/text', 1, 'for sensitive people'),
            SendOSC(rpijardinport, '/pyta/text', 0, 'sensitivepeople@plagiat.org'),
            SendOSC(rpijardinport, '/pyta/text/visible', -1, 1),
            SendOSC(rpicourport, '/pyta/text', 2, '[plaʒia]                             '),
            SendOSC(rpicourport, '/pyta/text/align', 2, 'left', 'top'),
            SendOSC(rpicourport, '/pyta/text/animate', 2, 'zoom', 0.8, 0.1, 4),
            SendOSC(rpicourport, '/pyta/text', 1, 'for sensitive people'),
            SendOSC(rpicourport, '/pyta/text', 0, 'sensitivepeople@plagiat.org'),
            SendOSC(rpicourport, '/pyta/text/visible', -1, 1),

            SendOSC(lightseqport, '/Lightseq/Bpm', 20),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sm_blinkinterns'),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,
            SendOSC(vxorlmeufport,     '/strip/VxORLVocod/AM%20pitchshifter/Pitch%20shift/unscaled', 1.2),

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
    orl >> ProgramFilter(3) >> [ # Refrain - Bouton 3
        stop,
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 225),

            SendOSC(klickport, '/klick/simple/set_tempo', 225),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(225)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(225)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(225)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(225)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],

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
            #bassscape,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(11) >> [ # SceneSwitch -> HorroCore
        SceneSwitch(9) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],

    ]
