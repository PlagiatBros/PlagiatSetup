# READ

import json

state = {}

for m in ['MonitorsJeannot', 'MonitorsORL']:

    state[m] = []
    id = ''
    pos = 0

    snapshot = open('../Sounds/NonMixer/' + m + '/snapshot', 'r').read()

    for line in snapshot.split('\n'):

        pos += 1

        if 'Mixer_Strip' in line:
            id = line.split(' ')[4][1:-1]
        elif 'Gain_Module' in line and id != '':
            state[m].append({
                'id': id,
                'value': float(line.split(' ')[4][1:-1].split(':')[0]),
                'line': pos
            })

file = open('../Interfaces/monitors.json', 'w')
file.write(json.dumps(state))
file.close()

# WRITE

import liblo
import time

server = liblo.Server(15001)

def save(path, args):
    m, data = args
    data = json.loads(data)
    if m not in ['MonitorsJeannot', 'MonitorsORL']:
        return
    mstate = state[m]
    for sstate in mstate:
        if sstate['id'] in data:
            sstate['value'] = data[sstate['id']]

    file = open('../Sounds/NonMixer/' + m + '/snapshot', 'r')
    cstate = file.read().split('\n')
    for sstate in mstate:
        line = sstate['line'] - 1
        if len(cstate) <= line or 'Gain_Module' not in cstate[line]:
            print('ERROR: snapshot changed, could not save')
            return
        x = cstate[line].split(' ')
        if x[4][0] != '"':
            print('ERROR: snapshot changed, could not save')
            return
        x[4] = '"%f:%s"' % (sstate['value'], x[4].split(':')[1][:-1])
        cstate[line] = ' '.join(x)

    file = open('../Sounds/NonMixer/' + m + '/snapshot', 'w')
    file.write('\n'.join(cstate))
    file.close()

server.add_method('/save', None, save)

while True:
    server.recv(0)
    time.sleep(0.01)
