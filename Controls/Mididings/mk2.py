# coding=utf8
from mididings import *
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC

config(
	backend='jack',
	client_name='ArturiaMk2',
	in_ports=['ArturiaMk2_in'],
	out_ports=['ArturiaMk2_out'],
)

hook(
    AutoRestart()
)

out = Output('ArturiaMk2_out', 2)

def ccToProgram(ev):
    print 'AA'
    return Program(ev.ctrl - 100)


filtering = PortFilter('ArturiaMk2_in') >> [
    Filter(CTRL) >> [
        ~CtrlFilter(range(101,109)),
        CtrlFilter(range(101,109)) >> CtrlValueFilter(127) >> NoteOn(EVENT_CTRL, 127) >> Transpose(-100) >> Program(EVENT_NOTE) >> out,
        ],
    ~Filter(CTRL)

]

run(
    scenes = {
            1: SceneGroup("filtering", [
          		Scene("filtering",
                    [
                        filtering,
                    ]
        		),
	    ]),

    },
)
