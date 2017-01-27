# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from utils import OSCCustomInterface


config(
	backend='jack',
	client_name='PedalBoardsRoutes',
	out_ports=['PBseq24', 'PBAMSClassicalSynth', 'PBTapeutape', 'PBCtrlOut'],
	in_ports=['PBCtrlIn', 'PBMk2In']
)

from scenes import *

hook(
    OSCInterface(56422, 56423), # "osc.udp://CtrlOrl:56423"),
    OSCCustomInterface(56418),
    AutoRestart()
)
def p(ev):
    ev.value = -2500
    return ev

run ( PortFilter('PBMk2In') >> [
        KeyFilter(notes=['c3', 'c4']) >> [
            Filter(NOTEON) >> Pitchbend(-2500) >> Process(p),
            Filter(NOTEOFF) >> Pitchbend(0)
        ] >> Output('PBCtrlOut', 1),
        Filter(CTRL) >> [
            CtrlValueFilter(127) >> [
                CtrlFilter(101) >> [NoteOn(7, 1), NoteOn(8,127)],
                CtrlFilter(102) >> [NoteOn(7, 80), NoteOn(8,127)],
                CtrlFilter(103) >> [NoteOn(7, 93), NoteOn(8,127)],
                CtrlFilter(104) >> [NoteOn(7, 100), NoteOn(8,127)],
                CtrlFilter(105) >> [NoteOn(7, 87), NoteOn(8,127)],
                CtrlFilter(106) >> NoteOn(6, 100),
                CtrlFilter(107) >> NoteOn(7,127),
                CtrlFilter(108) >> NoteOn(8,127),
            ],
            CtrlValueFilter(0) >> [NoteOn(8,1), NoteOn(6,63)]
        ] >> Output('PBCtrlOut', 1),
    #    Output('PBCtrlOut', 1)
    ]
)
