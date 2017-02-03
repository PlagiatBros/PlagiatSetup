#encoding: utf-8

from mididings import *

## OSC

klickport = 1234
slport = 9951
testport = 1111

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


samplespitchport = 7000
samplesdelaymungeport = 7001
samplesreversedelayport = 7002
samplesringmodport = 7003
samplestremoloport = 7005
samplesscapeport = 7006
samplesdisintegratorport = 7007
samplesmainport = 7008
samplesdegradeport = 7009

keyboardsport = 7010

bassmainport = 7020
monitorsorlport = 7030
monitorsjeannotport = 7031

vocodereannotport = 7050
vocoderorlport = 7051


## OSC Sequencers

trapcutport = 8001
audioseqport = 8002

## Zynadd

zyntrebleport = 10000
zynbassport = 10001

## CME keyboard programs

cmeinport = 56424
cmeoutport = 56425

## Mk2 keyboard programs

mk2inport = 56426
mk2outport = 56427


## MIDI

try:

    seq24=Output('PBseq24',1)
    seq24once=Output('PBseq24',2)

    tapeutape=Output('PBTapeutape',10)
    tapeutapecontrol=Output('PBTapeutape',1)

    guitarixst = Output('PBguitarix', 1)

except:

    pass
