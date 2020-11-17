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


gui_address = 'osc.udp://127.0.0.1:11000'


chains = ['Kick', 'OH', 'Basses', 'Samples', 'Keyboards', 'Vx_Missy', 'Vx_Nano', 'Vx_Public', 'Ambiance', 'Master']
meters = {}
state = {}
for chain in chains:
    meters[chain] = 0
    state[chain] = {
        'gain': 0,
        'pan': 50,
        'mute': 0
    }

state['OH']['mute'] = 1
state['Ambiance']['mute'] = 1
state_init = False

def get_meters():
    for chain in chains:
        command("c-select " + chain)
        meters[chain] = float(command("cop-get 3,1")[1])
        liblo.send(gui_address, '/ecasound/meter', chain, meters[chain])



def state_save():
    if state_init == False:
        return
    global state
    for chain in chains:
        command("c-select " + chain)
        state[chain]['gain'] = float(command("cop-get 1,1")[1])
        state[chain]['pan'] = float(command("cop-get 2,1")[1])
        state[chain]['mute'] = int(command("c-is-muted")[1])

def state_load():
    global state_init
    if state_init == False:
        state_init = True
    for chain in chains:
        gain_dB(chain, state[chain]['gain'])
        pano(chain, state[chain]['pan'])
        mute(chain, state[chain]['mute'])


def gain_dB(chain, gain):
    command("c-select " + chain)
    command("cop-set 1,1," + str(int(gain)))


def pano(chain, pan):
    command("c-select " + chain)
    command("cop-set 2,1," + str(int(pan)))


def mute(chain, toggle):
    command("c-select " + chain)
    if toggle:
        toggle = "on"
    else:
        toggle = "off"
    command("c-mute " + toggle)




def create_ports(record):

    state_save()

    command("stop")
    if not record:
        command("cs-remove all")
        command("cs-add PlagiatMixing")
    else:
        command("cs-remove all")
        command("cs-add PlagiatRecording")

    for chain in chains:
        print("Création de la chaine " + chain)
        command("c-add " + chain)
        command("ai-add jack")
        command("ao-add jack")
        command("cop-add -eadb:0")
        command("cop-add -epp:50")
        command("cop-add -evp")

    state_load()

    if not record:
        for chain in chains:
            if chain != 'Master':
                command("c-add " + chain + "_record")
                command("ai-add jack") #loop," + chain)
                command("ao-add jack")
    else:
        timestamp = datetime.now().isoformat(timespec='minutes')
        chemin = '/home/ukbaison/Clips/2017-2018_Plagiat/uk/RehearsalsAndLives/' + timestamp
        subprocess.run(['mkdir', chemin])
        for chain in chains:
            if chain != 'Master':
                command("c-add " + chain + "_record")
                command("ai-add jack") #loop," + chain)
                command("ao-add " + chemin + '/' +chain + ".wav")

    command("cs-connect")
    command("-G:jack,ecasound,notransport")
    command("start")



create_ports(False)

meter_toggle = True
def osc(path, args):
    if path == '/ecasound/recording':
        create_ports(True)
    elif path == '/ecasound/mixing':
        create_ports(False)
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
    elif path == '/ecasound/meter/toggle':
        global meter_toggle
        meter_toggle = bool(args[0])

server = liblo.Server(15003)
server.add_method(None, None, osc)


meter_check = 0
while 1:

    time.sleep(0.01)

    if meter_toggle:
        if meter_check == 0:
            get_meters()
        else:
            meter_check = (meter_check + 1) % 10

    while(server.recv(0)): pass

