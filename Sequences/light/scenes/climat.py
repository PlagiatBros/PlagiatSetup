#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *
from random import choice, shuffle

_words = {
    0: ['win32 error'],
    1: ['Gran Mounouté', 'Grand Moumouté ?', 'Wizzzdom', 'Grand Mère sait faire\n un bon café ?', 'Kond0m'],
    2: ['Dingité', 'Dingle Dongle', 'Infirmité', 'Soirée Infrimières ???' ],
    3: ['Éternité', 'Enuclée', 'NUclear Weap', 'Zzzzzz', '?? ZnuKzz']
}
_backs = ['Kwakwa', 'Mandalaa', 'Mendicité', 'Mamacito', 'Gnagnagna', 'lälalA']

def climat_mandela_subs(seq, timer, x=0):
    words = [choice(_words[x]), choice(_backs)]
    ports = [rpijardinport, rpijardinport]
    shuffle(ports)
    for i in range(2):
        seq.send(ports[i], '/pyta/text/0/reset')
        seq.send(ports[i], '/pyta/text/0/set', 'visible', 1)
        seq.send(ports[i], '/pyta/text/0/set', 'text', words[i])
