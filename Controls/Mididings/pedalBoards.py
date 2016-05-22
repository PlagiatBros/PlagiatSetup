# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from customosc import OSCCustomInterface

import liblo


config(
	backend='jack',
	client_name='PedalBoardsRoutes',
	out_ports=['PBseq24', 'PBAMSClassicalSynth', 'PBTapeutape', 'PBCtrlOut'],
	in_ports=['PBCtrlIn']
)

hook(
    OSCInterface(56422, 56423), # "osc.udp://CtrlOrl:56423"),
    OSCCustomInterface(56418),
    AutoRestart()
)


#### Ports OSC ################################################

klickport = 1234
slport = 9951
# testport = 1111
# qlcport = ("192.168.0.13", 7772)
# qlcstopport = ("192.168.0.13", 7771)
# #qlcport = 7777
# videoCport = ("192.168.0.31", 56418)
# videoCseqport = 12346
# videoJport = ("192.168.0.30", 56418)
# videoJseqport = 12347
# videoKport = ("192.168.0.32", 56418)
# videoKseqport = 12348
# qlcseqport = 12345 #("CtrlRegie", 12345)
# #videoseqport = ("CtrlDag", 12346)
# audioseqport=12344
# mainseqport = ("CtrlDag", 12343)
# desktoporlport = ("CtrlOrl", 12345)

# Non Mixers

vxorlpreport = 6666
vxorlmeufport = 6667
vxorlpostport = 6668
vxmainport = 6669
vxorlgarsport = 6670

vxjeannotpreport = 6671
vxjeannotmeufport = 6672
vxjeannotgarsport = 6673
vxjeannotpostport = 6674


samplesdelaymungeport = 7001
samplesreversedelayport = 7002
samplesringmodport = 7003
samplestremoloport = 7005
samplesscapeport = 7006
samplesdegradeport = 7009
samplesdisintegratorport = 7007
samplesmainport = 7008


bassmainport = 7020
monitorsorlport = 7030
monitorsjeannotport = 7031

# mainmixport = 6666
# drumsport = 6667
# bassesport = 6668
# guitarsport = 6669
# mxsynthport = 6670
# mxdrumsport = 6671
# vocalsport = 6672
# tomsport = 6673
# acousticsport = 6674
# mondagport = 6675
# monjeport = 6676
# monorlport = 6677
# mainsport = 6678



#### Outputs ################################################
seq24=Output('PBseq24',1)
seq24once=Output('PBseq24',2)

tapeutape=Output('PBTapeutape',10)


#### Functions #############################################
#### Trigger seq24 ####
p_firstpart=[range(1,65)]
p_secondpart=[range(65,129)]

note2seq = ProgramFilter(p_firstpart) >> seq24 # mute-groups seq24
note2seqNplay = ProgramFilter(p_secondpart) >> [ # mute-groups + play
			NoteOn(EVENT_PROGRAM,127) >> Transpose(-62) >> Program('PBseq24',1,EVENT_NOTE) >> seq24,
			Program('PBseq24',1,1),
		]


seq24start = Program('PBseq24',1,1)

seqtrigger = Filter(PROGRAM) >> [
		ChannelFilter(1) >> [ 
             		note2seq,
			note2seqNplay,
		],
		ChannelFilter(2) >> [
			seq24once,
		]
	]

cseqtrigger = Channel(1) >> seqtrigger

#### Bass ####

#### Vocals ####

#### Stop ####
stop = [
        Program(2) >> cseqtrigger,
        SendOSC(slport, '/sl/-1/hit', 'pause_on') >> Discard(),
        SendOSC(klickport, '/klick/metro/stop') >> Discard(),

        # [
        #     SendOSC(qlcstopport, '/AllStop', 1),
        #     SendOSC(qlcseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoCseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoCport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(videoJseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoJport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(videoKseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoKport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(audioseqport, '/Sequencer/DisableAll', 1),
        #     ] >> Discard()
]

#### FX Pedals #############################################
# ORL

#### Scenes ################################################

#### Climat ####
climat = PortFilter('PBCtrlIn') >> [
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 0.0),

            SendOSC(samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -7.0),
            SendOSC(samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -2.0),
            SendOSC(samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -2.0),



            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplestremoloport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -6.0),
            SendOSC(samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -7.50),

            ] >> Discard()
        ],
    ]

#### ConnassesSACEM ####
connassessacem = PortFilter('PBCtrlIn') >> [
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Thème Intro - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            


            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0),
            SendOSC(samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0),

            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Thème Intro - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 125),

            SendOSC(klickport, '/klick/simple/set_tempo', 125),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0),
            SendOSC(samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0),

            ] >> Discard()
        ],
    ]


#### Fifty ####
fifty = PortFilter('PBCtrlIn') >> [
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 110),

            SendOSC(klickport, '/klick/simple/set_tempo', 110),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -7.0),
            SendOSC(samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0),

            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Pont Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 110),

            SendOSC(klickport, '/klick/simple/set_tempo', 110),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Refrain - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 110),

            SendOSC(klickport, '/klick/simple/set_tempo', 110),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            ] >> Discard()
        ],
    ]

#### Le5 ####
le5 = PortFilter('PBCtrlIn') >> [
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Intro - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Couplet A - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Couplet B - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(5) >> [ # Couplet C - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(6) >> [ # Refrain - Bouton 6
        Program(69) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(7) >> [ # Couplet A - Bouton 7 - #TODO INUTILE?
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(8) >> [ # Couplet Bbis - Bouton 8
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(9) >> [ # Couplet Cbis - Bouton 9
        Program(72) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ]


#### SW ####
sw = PortFilter('PBCtrlIn') >> [
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0),
            SendOSC(samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0),
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Couplet - Bouton 3
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0),
            SendOSC(samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0),
            ] >> Discard()
        ],

    ProgramFilter(4) >> [ # Pont Refrain - Bouton 4
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -70.0),
            SendOSC(samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -4.5),
            ] >> Discard()
        ],

    ProgramFilter(5) >> [ # Couplet - Bouton 5
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 178.5),

            SendOSC(klickport, '/klick/simple/set_tempo', 178.5),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -18.0),
            SendOSC(samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0),
            ] >> Discard()
        ],

    ]

#### Whole World ####
wholeworld = PortFilter('PBCtrlIn') >> [
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Couplet - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0),
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Refrain - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0),
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Pont - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 90),

            SendOSC(klickport, '/klick/simple/set_tempo', 90),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -6.0),
            ] >> Discard()
        ],
    ]

#### Da Fist ####
dafist = PortFilter('PBCtrlIn') >> [
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [ # Intro Thème - Bouton 2
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),
            ] >> Discard()
        ],
    ProgramFilter(3) >> [ # Intro Thème 2 - Bouton 3
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0),
            ] >> Discard()
        ],
    ProgramFilter(4) >> [ # Couplet - Bouton 4
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -10.0),
            SendOSC(samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -9.0),
            ] >> Discard()
        ],
    ProgramFilter(5) >> [ # Couplet part 2 - Bouton 5
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),    

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0),        
            ] >> Discard()
        ],
    ProgramFilter(6) >> [ # Intro Refrain - Bouton 6
        Program(69) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0),
            ] >> Discard()
        ],
    ProgramFilter(7) >> [ # Refrain - Bouton 7
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eight_per_cycle', 8),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 4, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxx'),
            SendOSC(klickport, '/klick/metro/start'),            

            SendOSC(samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/Samples5Dry/Gain/Mute', 0.0),

            SendOSC(samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0),
            SendOSC(samplesmainport, '/strip/SamplesScape/Gain/Mute', 0.0),
            SendOSC(samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0),

            SendOSC(samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -5.0),
            ] >> Discard()
        ],
    ]


#### RUN ###################################################

run(
    scenes = {
        1: SceneGroup("Climat", [
  		Scene("Bass ORL",
                      [
                        climat,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        ]
		),
		Scene("Tune Select",
                      [
                        climat,
                        ]
		),
	    ]
        ),
        2: SceneGroup("ConnassesSACEM", [
  		Scene("Bass ORL",
                      [
                        connassessacem,
                        ]
		),
	    ]
        ),
        3: SceneGroup("Fifty", [
  		Scene("Bass ORL",
                      [
                        fifty,
                        ]
		),
	    ]
        ),
        4: SceneGroup("Le5", [
  		Scene("Bass ORL",
                      [
                        le5,
                        ]
		),
	    ]
        ),
        5: SceneGroup("SW", [
  		Scene("Bass ORL",
                      [
                        sw,
                        ]
		),
	    ]
        ),
        6: SceneGroup("Wholeworld", [
  		Scene("Bass ORL",
                      [
                        wholeworld,
                        ]
		),
	    ]
        ),
        7: SceneGroup("Da Fist", [
  		Scene("Bass ORL",
                      [
                        dafist,
                        ]
		),
	    ]
        ),
        # 2: SceneGroup("", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte1,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte1,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte1,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte1,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte1,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte1,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte1
	# 	),
	# 	Scene("Bank Select",
        #               acte1
	# 	),
	# 	Scene("Tune Select",
        #               acte1
	# 	)
	#     ]
        # ),
        # 3: SceneGroup("Acte II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte2,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte2,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte2,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte2,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte2,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte2,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte2
	# 	),
	# 	Scene("Bank Select",
        #               acte2
	# 	),
	# 	Scene("Tune Select",
        #               acte2
	# 	)
	#     ]
        # ),
        # 4: SceneGroup("Forain Acte II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 forainacte2,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 forainacte2,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 forainacte2,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 forainacte2,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 forainacte2,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 forainacte2,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               forainacte2
	# 	),
	# 	Scene("Bank Select",
        #               forainacte2
	# 	),
	# 	Scene("Tune Select",
        #               forainacte2
	# 	)
	#     ]
        # ),
        # 5: SceneGroup("Acte III", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3
        #               ),
	# 	Scene("Bank Select",
        #               acte3
        #               ),
	# 	Scene("Tune Select",
        #               acte3
	# 	)
	#     ]
        # ),
        # 6: SceneGroup("Acte III Part II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3partII,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3partII,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3partII,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3partII,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3partII,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3partII,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3partII
	# 	),
	# 	Scene("Bank Select",
        #               acte3partII
	# 	),
	# 	Scene("Tune Select",
        #               acte3partII
	# 	)
	#     ]
        # ),
        # 7: SceneGroup("Acte III Part III", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3partIII,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3partIII,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3partIII,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3partIII,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3partIII,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3partIII,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3partIII,
	# 	),
	# 	Scene("Bank Select",
        #               acte3partIII
	# 	),
	# 	Scene("Tune Select",
        #               acte3partIII
	# 	)
	#     ]
        # ),
        # 8: SceneGroup("Acte IV", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte4,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte4,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte4,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte4,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte4,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte4,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
	# 	    acte4
	# 	),
	# 	Scene("Bank Select",
	# 	    acte4
	# 	),
	# 	Scene("Tune Select",
	# 	    acte4
	# 	)
	#     ]
        # ),

    },
)

