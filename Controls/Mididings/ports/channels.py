from mididings import *

jeannot = PortFilter('PBMk2In') >> Filter(CTRL) >> CtrlFilter(range(101,109)) >> CtrlValueFilter(127) >> NoteOn(EVENT_CTRL, 127) >> Transpose(-100) >> Program(EVENT_NOTE)

jeannotKeys = PortFilter('PBMk2In') >> [
    Filter(CTRL) >> ~CtrlFilter(range(101,109)),
    ~Filter(CTRL)
]

orl     = PortFilter('PBCtrlIn') >> ChannelFilter(1)
