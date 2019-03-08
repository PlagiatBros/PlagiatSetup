#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

sw_mk2lights = {
    1:'blue',
    2:'purple',
    3:'purple',
    5:'yellow',
    6:'yellow',
    7:'yellow',
    8:'green',
}


#### SW ####
sw = [
    Init([
        Program(seq24PageMap[7]) >> seq24once,
        Ctrl(0, 4) >> tapeutapecontrol,

        disable_microtonal,
        # zynmicrotonal_off,

        SendOSC(mk2inport, '/mididings/switch_scene', 2),
        mk2lights(sw_mk2lights),
    ]),
    jeannot_padrelease >> mk2lights(sw_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*')
    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([2]) >> light_reset >> Discard(),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    orl >> ProgramFilter(2) >> [ # intro - Bouton 2
        #TODO filtre --> Degrade déjà en place ?
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOSC(lightseqport, '/Lightseq/Bpm', 178.5),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_leboncoin'),


            SendOscState([

                [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

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
            ] >> Discard()
        ],
    jeannot >> ProgramFilter(2) >> [ # Lanceur du Couplet (delais = 2 mesures) - Bouton 2
        [
            SendOSC(audioseqport, '/Audioseq/Bpm', 178.5),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_couplet_auto', timestamp),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'XxXx'),
            SendOSC(klickport, '/klick/metro/start'),

            ] >> Discard()
        ],
    orl >> ProgramFilter(3) >> [ # Couplet - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOscState([

                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,
            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,
            ] >> Discard()
        ],

    orl >> ProgramFilter(4) >> [ # Refrain - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOSC(rpijardinport, '/pyta/text', 0, 'MORONESS'),
            SendOSC(rpijardinport, '/pyta/text/strobe', 0, 1, 5, 0.5),
            SendOSC(rpijardinport, '/pyta/text/colorstrobe', 0, 1, 7, 0.5),
            SendOSC(rpijardinport, '/pyta/slide/strobe', 'White', 1, 4, 0.5),
            SendOSC(rpijardinport, '/pyta/slide/visible', 'White', 1),
            SendOSC(rpicourport, '/pyta/slide/strobe', 'White', 1, 4, 0.5),
            SendOSC(rpicourport, '/pyta/slide/visible', 'White', 1),
            SendOSC(rpicourport, '/pyta/text', 0, 'MORONESS'),
            SendOSC(rpicourport, '/pyta/text/strobe', 0, 1, 5, 0.5),
            SendOSC(rpicourport, '/pyta/text/colorstrobe', 0, 1, 7, 0.5),
            SendOSC(rpicourport, '/pyta/slide/strobe', 'White', 1, 4, 0.5),
            SendOSC(rpicourport, '/pyta/slide/visible', 'White', 1),




            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -4.5],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_on,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,
            vxjeannotdelay_on,
            vxjeannotvocode_off,

            ] >> Discard()
        ],

    orl >> ProgramFilter(5) >> [ # Couplet 2 - Bouton 5
        Program(66) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Bpm', 178.5),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_couplet_auto2', timestamp),

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOscState([

                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],
                [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -3.0],
                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_on,
            vxorlvocode_off,
            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,
            ] >> Discard()
        ],
    orl >> ProgramFilter(6) >> [ # Couplet 2 - Bouton 6
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOSC(rpijardinport, '/pyta/slide/animate', 'Water_1', 'alpha', 0.1, 1, 200),
            SendOSC(rpijardinport, '/pyta/slide/strobe', 'Water_1', 1, 4, 0.5),
            SendOSC(rpijardinport, '/pyta/slide/visible', 'Water_1', 1),
            SendOSC(rpijardinport, '/pyta/slide/strobe', 'Water_1', 1, 6, 0.5),
            SendOSC(rpijardinport, '/pyta/slide/visible', 'Water_1', 1),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

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
            ] >> Discard()
        ],

    jeannot >> ProgramFilter(3) >> [ # stop Three get the shit going- Bouton 3
#        Program(65) >> cseqtrigger,
        stop,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(178.5)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(178.5)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(178.5)),

            SendOscState([

                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0],

                [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_on,
            vxorldelay_on,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,
            vxjeannotdelay_on,
            vxjeannotvocode_off,

            SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
            SendOSC(vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 1.0),

            SendOSC(audioseqport, '/Audioseq/Bpm', 178.5),
            SendOSC(audioseqport, '/Audioseq/Scene/Play', 'sw_shit_going', timestamp),

            ] >> Discard()
        ],

    jeannot >> ProgramFilter(5) >> [
        vxjeannotdelay_off,
        vxjeannotgars_on,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(6) >> [
        vxjeannotgars_off,
        vxjeannotmeuf_on,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_off,
    ] >> Discard(),
    jeannot >> ProgramFilter(7) >> [
        vxjeannotgars_off,
        vxjeannotmeuf_off,
        vxjeannotdisint_off,
        vxjeannotdelay_off,
        vxjeannotvocode_on,
    ] >> Discard(),

    jeannot >> ProgramFilter(8) >> [ # video: one/two - Bouton 8
        SendOSC(lightseqport, '/Lightseq/Bpm', 22.3125),
        SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'sw_onetwo_jardin', 1),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_onetwo_jardin'),
        SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'sw_onetwo_cour', 1),
        SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'sw_onetwo_cour'),
        SendOSC(lightseqport, '/Lightseq/Play', timestamp),
    ],

    orl >> ProgramFilter(11) >> [ # SlowMotium
        SceneSwitch(8) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],

    ]
