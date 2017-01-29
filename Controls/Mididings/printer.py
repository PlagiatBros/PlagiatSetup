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
    print ' ctrl: %s\n value: %s' % (ev.ctrl, ev.value)

run(Process(printer))
