#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

upsideD = [[rpijardinport, '/pyta/slide/mooncup_1/set', 'rotate_z', 180], [rpijardinport, '/pyta/slide/mooncup_1/set', 'align_v', 't'], [rpicourport, '/pyta/slide/mooncup_1/set', 'rotate_z', 180], [rpicourport, '/pyta/slide/mooncup_1/set', 'align_v', 't']]
upsideD_off = [[rpijardinport, '/pyta/slide/mooncup_1/set', 'rotate_z', 0], [rpijardinport, '/pyta/slide/mooncup_1/set', 'align_v', 'b'], [rpicourport, '/pyta/slide/mooncup_1/set', 'rotate_z', 0], [rpicourport, '/pyta/slide/mooncup_1/set', 'align_v', 'b']]

horrorcore_couplet_mooncup = [
    None, None, None, upsideD,
    None, (None, upsideD_off), (None, None, upsideD), upsideD_off,
    None, None, None, upsideD,
    None, (None, upsideD_off), None, None,

    None, None, None, upsideD,
    None, (None, upsideD_off), (None, None, upsideD), upsideD_off,
    None, None, None, upsideD,
    None, (None, upsideD_off), None, None
]

stu = [[rpijardinport, '/pyta/text/1/set', 'text', "STew    "], [rpijardinport, '/pyta/text/1/set', 'visible', 1]]
pid = [[rpijardinport, '/pyta/text/2/set', 'text', "     pId"], [rpijardinport, '/pyta/text/2/set', 'visible', 1]]
don = [[rpicourport, '/pyta/text/1/set', 'text', "DON    "], [rpicourport, '/pyta/text/1/set', 'visible', 1]]
keys = [[rpicourport, '/pyta/text/2/set', 'text', "    key"], [rpicourport, '/pyta/text/2/set', 'visible', 1]]

glitch_and_down = [[rpijardinport, '/pyta/text/[1-2]/animate', 'position_y', 0, -1, 1], [rpijardinport, '/pyta/text/[1-2]/set', 'rgbwave', 0.3], [rpicourport, '/pyta/text/[1-2]/animate', 'position_y', 0, -1, 1], [rpicourport, '/pyta/text/[1-2]/set', 'rgbwave', 0.3]]
horrorcore_stupidDonkeys = [
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,

    None, None, None, None,
    None, None, (stu, None, pid), (None, don, None),
    keys, None, glitch_and_down, None,
    None, None, None, None
]
