#!/usr/bin/env python
#encoding: utf-8

"""

::: OscSendProxy :::

A proxy tool that allows setting a default osc state (a pack of osc messages really)
and that will be used to send messages packs after merging them to the defaults, thus
avoiding inconsistent state changes (ie reset all tracks' mute states and immediately 
unmute some of them)

::: Usage :::

OscSendProxy(defaults)

Constructs the proxy object

::: Methods :::

@setDefaults(defaults)

'defaults' must be an array of args arrays that would normally be given to SendOsc:

[
    [port,path,args],
    [port,path,args],
    [port,path,args],
    [port,path,args],
    # etc
]

@sendOscState(overrides)

'overrides' must be an array of args arrays that would normally be given to SendOsc. 
These will be merged with the defaults defined via @setDefaults

[
    [port,path,args],
    [port,path,args],
    [port,path,args],
    [port,path,args],
    # etc
]



"""

from liblo import send as _send
from mididings import Call as _Call

class callableSendOscState(object):
    def __init__(self,messages):
        self.messages = messages

    def __call__(self,ev):
        for item in self.messages:
            _send(*item)
            


class OscSendProxy(object):
    def __init__(self, defaults = [] ):
        self.defaults = self.makeDictionnary(defaults)   

    def makeDictionnary(self,data):
        ret = {}
        for item in data:
            key = str(item[0]) + str(item[1])
            ret[key] = item
        return ret

    def setDefaults(self,defaults):
        self.defaults = self.makeDictionnay(defaults)

    def mergeWithDefaults(self,overrides):
        copy = self.defaults.copy()
        copy.update(self.makeDictionnary(overrides))
        return copy

    def sendOscState(self,overrides):
        messages = self.mergeWithDefaults(overrides).values()
        return _Call(callableSendOscState(messages))




