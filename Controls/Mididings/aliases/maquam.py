from mididings import *

def maquam(notes, bend):

    def fixBug(ev):
        ev.value = bend
        return ev

    maquam = [
            KeyFilter(notes) >> [
                Filter(NOTEON) >> Pitchbend(bend) >> Process(fixBug),
                Filter(NOTEOFF) >> Pitchbend(0)
            ] >> Output('PBCtrlOut', 1),
            Output('PBCtrlOut', 1)
        ]

    return maquam
