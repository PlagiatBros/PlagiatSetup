
from math import sin, asin, pi

def barDmxRangeAdapter(dimmer):
    # Affinized argument converted from [0:255] to [-pi/2:pi/2]
    a = pi / 255
    b = - pi / 2

    # Sinus output translated and casted to [0 - 255]
    return int((255 / 2.) * (sin (a * dimmer + b) + 1))

def barDmxRangeDeAdapter(dimmer):
    # Returns the dimmer to be passed to the adapter to get that real DMX output
    return int((255 / pi) * (asin (dimmer * (2 / 255.) - 1) + pi / 2))
