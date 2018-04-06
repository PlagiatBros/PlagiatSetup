#encoding: utf-8

from mididings import *
from mididings.extra.osc import SendOSC

from ports import *

from oscSendProxy import OscSendProxy

from liblo import time

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

seq24PageMap = {
    1: 114, #connassesSACEM
    2: 119, #dafist
    3: 113, #climat
    4: 115, #fifty
    5: 116, #Le5
    6: 123, #trapone
    7: 117, #sw
    8: 121, #geturfreakon + 120
    9: 122, #horrorcore
    10:118, #wholeworld
}

#### BPM Scape & Delay Vx ####
# Formule : (x-30)/134.
scapebpmpath = 'C%2A%20Scape%20-%20Stereo%20delay%20with%20chromatic%20resonances/bpm'

class scapebpm(object):
    def __init__(self, bpm):
        self.v = (bpm-30)/134.
    def __call__(self, ev):
        return self.v

# Formule : (x-30)/270.
delaybpmpath = 'Calf%20Vintage%20Delay/Tempo'
class delaybpm(object):
    def __init__(self, bpm):
        self.v = (bpm-30)/270.
    def __call__(self, ev):
        return self.v


#### Vocals ####
# VxORLMeuf
vxorlmeuf_on = [
    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 0.0),
    SendOSC(surfaceorlport, '/vxorl', 'meuf', 1),

    ] >> Discard()

vxorlmeuf_off = [
#    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLMeufPost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'meuf', 0),
    ] >> Discard()

# VxORLGars
vxorlgars_on = [
    SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 0.0),
    SendOSC(surfaceorlport, '/vxorl', 'gars', 1),
    ] >> Discard()

vxorlgars_off = [
    SendOSC(vxorlpreport, '/strip/VxORLGars/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLGarsPost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'gars', 0),
    ] >> Discard()

# VxORLDisint
vxorldisint_on = [
    SendOSC(vxorlpreport, '/strip/VxORLDisint/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLDisintPost/Gain/Mute', 0.0),
    SendOSC(surfaceorlport, '/vxorl', 'disint', 1),
    ] >> Discard()

vxorldisint_off = [
    SendOSC(vxorlpreport, '/strip/VxORLDisint/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLDisintPost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'disint', 0),
    ] >> Discard()

# VxORLDelay
vxorldelay_on = [
    SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLDelayPost/Gain/Mute', 0.0),
    SendOSC(surfaceorlport, '/vxorl', 'delay', 1),
    ] >> Discard()

vxorldelay_off = [
    SendOSC(vxorlpreport, '/strip/VxORLDelayPre/Gain/Mute', 1.0),
    SendOSC(vxorlpostport, '/strip/VxORLDelayPost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'delay', 0),
    ] >> Discard()

# VxORLVocode
vxorlvocode_on= [
    SendOSC(vxorlpreport, '/strip/VxORLMeuf/Gain/Mute', 0.0),
    SendOSC(vxorlpostport, '/strip/VxORLVocodePost/Gain/Mute', 0.0),
    # SendOSC(vxorlmeufport,  '/strip/VxORLVocod/AM%20pitchshifter/Pitch%20shift/unscaled', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'vocode', 1),
    ] >> Discard()

vxorlvocode_off= [
    SendOSC(vxorlpostport, '/strip/VxORLVocodePost/Gain/Mute', 1.0),
    SendOSC(surfaceorlport, '/vxorl', 'vocode', 0),
    ] >> Discard()

# VxJeannotMeuf
vxjeannotmeuf_on = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotMeufPost/Gain/Mute', 0.0),
    ] >> Discard()

vxjeannotmeuf_off = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotMeufPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxJeannotGars
vxjeannotgars_on = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotGarsPost/Gain/Mute', 0.0),
    ] >> Discard()

vxjeannotgars_off = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotGars/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotGarsPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxJeannotDisint
vxjeannotdisint_on = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotDisint/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDisintPost/Gain/Mute', 0.0),
    ] >> Discard()

vxjeannotdisint_off = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotDisint/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDisintPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxJeannotDelay
vxjeannotdelay_on = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/Gain/Mute', 0.0),
    ] >> Discard()

vxjeannotdelay_off = [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotDelayPre/Gain/Mute', 1.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/Gain/Mute', 1.0),
    ] >> Discard()

# VxJeannotVocode
vxjeannotvocode_on= [
    SendOSC(vxjeannotpreport, '/strip/VxJeannotMeuf/Gain/Mute', 0.0),
    SendOSC(vxjeannotpostport, '/strip/VxJeannotVocodePost/Gain/Mute', 0.0),
    # SendOSC(vxjeannotmeufport, '/strip/VxJeannotVocod/AM%20pitchshifter/Pitch%20shift/unscaled', 1.0),
    ] >> Discard()
vxjeannotvocode_off= [
    SendOSC(vxjeannotpostport, '/strip/VxJeannotVocodePost/Gain/Mute', 1.0),
    ] >> Discard()


#### Bass ####
# Dry #
bassdry = [
    SendOSC(bassmainport, '/strip/BassScapePre/Gain/Mute', 1.0),
    SendOSC(bassmainport, '/strip/BassDegradePre/Gain/Mute', 1.0),
    SendOSC(bassmainport, '/strip/BassWobblePost/MDA%20RezFilter/Freq/unscaled', 0.0),
    ] >> Discard()

# Scape #
bassscape = [
    SendOSC(bassmainport, '/strip/BassScapePre/Gain/Mute', 0.0),
    ] >> Discard()

# Degrade #
bassdegrade = [
    SendOSC(bassmainport, '/strip/BassDegradePre/Gain/Mute', 0.0),
    ] >> Discard()

# Wobble #
basswobble = [
    SendOSC(bassmainport, '/strip/BassWobblePre/Gain/Mute', 0.0),
    ] >> Discard()


# Guitarix - Stages - Control Changes #
bassdetunest_on = Ctrl(0, 127) >> guitarixst
bassvibest_on = Ctrl(1, 127) >> guitarixst
bassringst_on = Ctrl(2, 127) >> guitarixst
bassbufferst_on = Ctrl(3, 127) >> guitarixst
bassdetunest_off = Ctrl(0, 0) >> guitarixst
bassvibest_off = Ctrl(1, 0) >> guitarixst
bassringst_off = Ctrl(2, 0) >> guitarixst
bassbufferst_off = Ctrl(3, 0) >> guitarixst


# pedal Select

pedalselect = ProgramFilter([range(12,24)]) >> NoteOn(EVENT_PROGRAM, 127) >> Transpose(-12) >> SubSceneSwitch(EVENT_NOTE) >> Discard()

# Bass Pedal
basspedal= [
    ProgramFilter(13) >> SendOSC(slport, '/sl/0/hit', 'record') >> Discard(),
    ProgramFilter(14) >> SendOSC(slport, '/sl/0/hit', 'overdub') >> Discard(),
    ProgramFilter(15) >> SendOSC(slport, '/sl/0/hit', 'pause_on') >> Discard(),
    ProgramFilter(16) >> SendOSC(slport, '/sl/1/hit', 'record') >> Discard(),
    ProgramFilter(17) >> SendOSC(slport, '/sl/1/hit', 'overdub') >> Discard(),
    ProgramFilter(18) >> SendOSC(slport, '/sl/1/hit', 'pause_on') >> Discard(),
    ProgramFilter(19) >> bassscape,
    ProgramFilter(20) >> bassdegrade,
    ProgramFilter(21) >> [bassdry, bassdetunest_on, bassvibest_on, bassringst_on, bassbufferst_on],
    ProgramFilter(22) >> [bassdry, bassdetunest_off, bassvibest_on, bassringst_on, bassbufferst_on],
    ProgramFilter(23) >> [bassdry, bassdetunest_on, bassvibest_on, bassringst_off, bassbufferst_off],
    ]

# Vx Pedal
vxpedal= [
    ProgramFilter(13) >> SendOSC(slport, '/sl/2/hit', 'record') >> Discard(),
    ProgramFilter(14) >> SendOSC(slport, '/sl/2/hit', 'overdub') >> Discard(),
    ProgramFilter(15) >> SendOSC(slport, '/sl/2/hit', 'pause_on') >> Discard(),
    ProgramFilter(16) >> SendOSC(slport, '/sl/3/hit', 'record') >> Discard(),
    ProgramFilter(17) >> SendOSC(slport, '/sl/3/hit', 'overdub') >> Discard(),
    ProgramFilter(18) >> SendOSC(slport, '/sl/3/hit', 'pause_on') >> Discard(),
    ProgramFilter(19) >> vxorldelay_on,
    ProgramFilter(20) >> vxorldisint_on,
    ProgramFilter(21) >> [vxorlmeuf_on, vxorlgars_on, vxorldelay_off, vxorlvocode_off, vxorldisint_off],
    ProgramFilter(22) >> [vxorlmeuf_off, vxorlgars_on, vxorldelay_off, vxorlvocode_off, vxorldisint_off],
    ProgramFilter(23) >> [vxorlmeuf_on, vxorlgars_off, vxorldelay_off, vxorlvocode_off, vxorldisint_off],
    ]




#### Stop ####
stop = [
        Program(2) >> cseqtrigger,
        [
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),
            SendOSC(klickport, '/klick/metro/stop'),
            # SendOSC(audioseqport, '/Audioseq/DisableAll'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Disable', '*'),
            SendOSC(lightseqport, '/Lightseq/Scene/Stop', '*'),
        ]  >> Discard(),
]


### Microtonal ###

vocodports = [vocoderjeannotport, vocoderjeannotportgars, vocoderjeannotportmeuf, vocoderorlport, vocoderorlportgars, vocoderorlportmeuf]

zynmicrotonal_on = SendOSC(zyntrebleport, '/microtonal/Penabled', True)
zynmicrotonal_off = SendOSC(zyntrebleport, '/microtonal/Penabled', False)

enable_microtonal = [
	SendOSC(zyntrebleport, '/microtonal/Penabled', True)
]

disable_microtonal = [
	SendOSC(zyntrebleport, '/microtonal/Penabled', True)
]

for port in vocodports:
	for i in range(12):
		disable_microtonal.append(SendOSC(port, '/x42/parameter', i + 24, 0.0))


def set_microtonal(*tunings):

	commands = []

	zynshift = tunings[10:] + tunings[:10] # zyn commence au Si bémol
	zynscale = "\n".join([str(100.0 + i * 100 + zynshift[i] * 100) for i in range(12)]).replace('1200.0', '2/1')

	commands.append(SendOSC(zyntrebleport, '/microtonal/tunings', zynscale))

	for port in vocodports:
		transpo = range(12)
		if port is vocoderjeannotportgars or port is vocoderorlportgars:
			transpo = transpo[-4:] + transpo[:-4]
		elif port is vocoderjeannotportmeuf or port is vocoderorlportmeuf:
			transpo = transpo[4:] + transpo[:4]
		else:
			transpo = transpo[:]

		for i in transpo:
			commands.append(SendOSC(port, '/x42/parameter', i + 24, float(tunings[i])))


	return commands

### OSC send proxy #####################################

oscsendproxy = OscSendProxy([
    # SamplesMain
    [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/Samples4Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/Samples5Dry/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesDrumKlit/Gain/Mute', 0.0],
    [samplesmainport, '/strip/SamplesMunge/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesReverseDelay/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesScape/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesTremolo/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesDegrade/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesDisintegrator/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesPitch/Gain/Mute', 1.0],
    [samplesmainport, '/strip/SamplesRingMod/Gain/Mute', 1.0],

    # SamplesDelayMunge
    [samplesdelaymungeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdelaymungeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdelaymungeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdelaymungeport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdelaymungeport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesReverseDelay
    [samplesreversedelayport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesreversedelayport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesreversedelayport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesreversedelayport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesreversedelayport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesScape
    [samplesscapeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/SamplesTremolo/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/SamplesDegrade/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesscapeport, '/strip/SamplesPitch/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesTremolo
    [samplestremoloport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplestremoloport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplestremoloport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplestremoloport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplestremoloport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesDegrade
    [samplesdegradeport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdegradeport, '/strip/SamplesScape/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesDisintegrator
    [samplesdisintegratorport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdisintegratorport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdisintegratorport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdisintegratorport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesdisintegratorport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesPitch
    [samplespitchport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplespitchport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplespitchport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplespitchport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplespitchport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],

    # SamplesRingMod
    [samplesringmodport, '/strip/Samples1/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesringmodport, '/strip/Samples2/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesringmodport, '/strip/Samples3/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesringmodport, '/strip/Samples4/Gain/Gain%20(dB)/unscaled', -70.0],
    [samplesringmodport, '/strip/Samples5/Gain/Gain%20(dB)/unscaled', -70.0],


])

SendOscState = oscsendproxy.sendOscState

"""

zitaNotes = {
    'c': 7,
    'c#':8,
    'd' :9,
    'd#':10,
    'e':11,
    'f':12,
    'f#':13,
    'g':14,
    'g#':15,
    'a':16,
    'a#':17,
    'b':18,
}

def vocodernote(note, value, port=[vocoderjeannotport, vocoderorlport]):
    ev = []

    if type(port) != list:
        port = [port]
    if type(note) != list:
        note = [note]

    value = float(bool(value))

    for p in port:
        for n in note:
            ev.append(SendOSC(port, '/x42/parameter', zitanotes[n.lower()], value))

def vocoderscale(notes, port=[vocoderjeannotport, vocoderorlport]):

    ev = []

    for note in zitaNotes:
        if note in notes:
            ev.append(
                vocodernote_on(port, 1.0, note)
            )
        else:
            ev.append(
                vocodernote_off(port, 0.0, note)
            )

    return ev

"""

def timestamp(ev):
    return ('t', time())

mk2colors = {
    'red':1,
    'blue':16,
    'green':4,
    'purple':17,
    'cyan':20,
    'yellow':5,
    'white':127
}
mk2colordefaults = [
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # pedalboards scenes btns
	mk2colors['red'], mk2colors['red'],mk2colors['yellow'], # sl vx pre rec/overdub/pause
	mk2colors['red'], mk2colors['red'],mk2colors['yellow'], # sl vx post rec/overdub/pause
	0x00, mk2colors['purple']
]
def mk2lights(pads):
    m = []
    for i in range(1,17):
        color = mk2colordefaults[i-1]
        if i in pads:
            color = mk2colors['purple']
            if type(pads) == dict:
                color =  mk2colors[pads[i]]
            elif i == 1:
                color = mk2colors['blue']
            elif i == 8:
                color = mk2colors['red']
        m.append(SysEx('Mk2SysexOut', [0xf0,0x00,0x20,0x6b,0x7f,0x42,0x02,0x00,0x10,111+i,color,0xf7]))
    return m
