# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart


config(
	backend='jack',
	client_name='MIDIMON',
	in_ports=['Print']
)

def printer(ev):
    print 'Midi received:'
    print ' channel: %s\n type: %s' % (ev.channel, ev.type)
    if str(ev.type) == 'CTRL':
        print ' ctrl: %s\n value: %s' % (ev.ctrl, ev.value)
    if str(ev.type) == 'NOTEON' or str(ev.type) == 'NOTEOFF':
        print ' note: %s\n velocity: %s' % (ev.note, ev.velocity)

run(Process(printer))
