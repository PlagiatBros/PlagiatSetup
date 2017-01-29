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
    print 'Midi received:\n channel: %s\n type: %s' % (ev.channel, ev.type)

run(Process(printer))
