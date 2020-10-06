#!/usr/bin/python3

import ecamonitor

from datetime import datetime
import liblo
import time
from pyeca import *

while 1:
    try:
        s = ecamonitor.connect_to_server('127.0.0.1',  2868)
        break
    except:
            time.sleep(1)

def command(string):
    return(ecamonitor.issue_eiam_command(s, string))


command("cs-add PlagiatRecording")
chains = ['Kick', 'OH', 'Basses', 'Samples', 'Keyboards', 'Vx_Missy', 'Vx_Nano', 'Vx_Public', 'Ambiance', 'Master']

def create_ports():
    for chain in chains:
        print("Création de la chain " + chain)
        command("c-add " + chain)
        command("ai-add jack")
        command("ao-add jack")
        command("cop-add -eadb:0")
        command("cop-add -epp:50")


def create_wavs():
    timestamp = datetime.now().isoformat(timespec='minutes')
    chemin = '/home/ukbaison/Clips/2017-2018_Plagiat/uk/RehearsalsAndLives/' + timestamp
    subprocess.run(['mkdir', chemin])
    for chain in chains:
        if chain != 'Master':
            command("c-select " + chain)
            command("ao-add " + chemin + '/' +chain + ".wav")


create_ports()


command("cs-connect")
command("-G:jack,ecasound,notransport")
command("start")


def gain_dB(chain, gain):
    command("c-select " + chain)
    command("cop-set 1,1," + str(int(gain)))
#    print(command("cop-status"))

def pano(chain, pan):
    command("c-select " + chain)
    command("cop-set 2,1," + str(int(pan)))
#    print(command("cop-status"))

def mute(chain, toggle):
    if toggle:
        toggle = "on"
    else:
        toggle = "off"    
    command("c-mute " + toggle)

def osc(path, args):
    if path == '/ecasound/start':
        command("stop")
        create_wavs()
        command("start")
    elif path == '/ecasound/stop':
        command("stop")
    elif path == '/ecasound/gain':
        chain = args[0]
        gain = args[1]
        gain_dB(chain, gain)
    elif path == '/ecasound/pan':
        chain = args[0]
        pan = args[1]
        pano(chain, pan)
    elif path == '/ecasound/mute':
        chain = args[0]
        toggle = args[1]
        mute(chain, toggle)

server = liblo.Server(15003)
server.add_method(None, None, osc)

while 1:
    time.sleep(0.01)
    server.recv(0)
    #print(command("engine-status"))
