# coding=utf8
from mididings import *
from mididings.extra.inotify import AutoRestart
from utils import OSCCustomInterface

config(
	backend='jack',
	client_name='vocodTranspo',
	out_ports=['to-x42-fat1-up', 'to-x42-fat1-down'],
	in_ports=['from-seq24']
)

hook(
    AutoRestart()
)

from ports import *

#### Transpo ####
transpo = PortFilter('from-seq24') >> [
    Filter(NOTE) >>
    [
        Transpose(+4) >> Output('to-x42-fat1-up', 1),
        Transpose(-4) >> Output('to-x42-fat1-down', 1)
    ]
]

#### RUN ###################################################

run(transpo)
