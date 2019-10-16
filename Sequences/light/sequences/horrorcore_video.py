#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *
import random

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

def _text(word):
    return [rpijardinport, '/pyta/text/0/set', 'text', word, 0.1]

def _text_rand():
    words = ['guys', 'buys', 'buicks', 'yacks', 'shagz', 'gruïck', 'jeez', 'bulls', 'eyes']
    return [rpijardinport, '/pyta/text/0/set', 'text', words[random.randint(0, len(words) - 1)], 0.1]


horrorcore_refrain_jardin = [
    _text('no'), None, None, None,
    (_text('dis'), None, _text('ain\'t')), (None, _text('no'), None), _text('lov'), _text('song'),
    None, None, None, None,
    (_text('dis'), None, _text('ain\'t')), (None, _text('no'), None), _text('fu'), _text('king'),
    _text('sad'), _text('song'), None, None,
    (_text('U'), None, _text('ain\'t')), (None, _text('me'), None), _text('kind'), _text('ov'),
    _text('galls'), None, None, None,
    (_text('you'), None, _text('ain\'t')), (None, _text('my'), None), _text('kind'), _text('of'),
    _text_rand(), _text_rand(), _text_rand(), _text_rand(),
    _text_rand(), _text_rand(), _text_rand(), _text_rand()
]


def _text_rand_lalala():
    words = ['laaa', 'bââ', 'lala', 'lalala', 'blah', 'blâââ', 'blabla']
    return [
        [rpicourport, '/pyta/text/2/set', 'text', words[random.randint(0, len(words) - 1)], 0.2],
        [rpicourport, '/pyta/text/2/animate', 'rotate_z', '+0', random.randint(-60, 60), 0.1],
        [rpicourport, '/pyta/text/2/animate', 'position', '+0', '+0', '+0', random.random() / 2. - 0.25, random.random() / 2. - 0.25, -2, 0.1],
    ]

horrorcore_refrain_cour = [
    _text_rand_lalala(), None, None, None,
    (_text_rand_lalala(), None, _text_rand_lalala()), (None, _text_rand_lalala(), None), _text_rand_lalala(), _text_rand_lalala(),
    None, None, None, None,
    (_text_rand_lalala(), None, _text_rand_lalala()), (None, _text_rand_lalala(), None), _text_rand_lalala(), _text_rand_lalala(),
    _text_rand_lalala(), _text_rand_lalala(), None, None,
    (_text_rand_lalala(), None, _text_rand_lalala()), (None, _text_rand_lalala(), None), _text_rand_lalala(), _text_rand_lalala(),
    _text_rand_lalala(), None, None, None,
    (_text_rand_lalala(), None, _text_rand_lalala()), (None, _text_rand_lalala(), None), _text_rand_lalala(), _text_rand_lalala(),
    _text_rand_lalala(), _text_rand_lalala(), _text_rand_lalala(), _text_rand_lalala(),
    _text_rand_lalala(), _text_rand_lalala(), _text_rand_lalala(), _text_rand_lalala()
]

horrorcore_couplet_2_screenswitch_strobe = [
    [rpicourport, '/pyta/slide/talkingheads_3/strobe', 'alpha', 0, 1, 0.08, 0.5],
    [rpijardinport, '/pyta/slide/talkingheads_3/strobe', 'alpha', 1, 0, 0.08, 0.5],
]

horrorcore_couplet_2_screenswitch_strobe_stop = [
    [rpicourport, '/pyta/slide/talkingheads_3/strobe_stop', 'alpha'],
    [rpijardinport, '/pyta/slide/talkingheads_3/strobe_stop', 'alpha']
]


horrorcore_couplet_2_screenswitch = [
    horrorcore_couplet_2_screenswitch_strobe_stop+ [[rpijardinport, '/pyta/slide/talkingheads_3/set', 'gif_frame', 1], [rpijardinport, '/pyta/slide/talkingheads_3/set', 'alpha', 1], [rpicourport, '/pyta/slide/talkingheads_3/set', 'alpha', 0]],
    None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, horrorcore_couplet_2_screenswitch_strobe + [[rpicourport, '/pyta/slide/talkingheads_3/set', 'gif_frame', 1]],
    horrorcore_couplet_2_screenswitch_strobe_stop + [[rpicourport, '/pyta/slide/talkingheads_3/set', 'alpha', 1], [rpijardinport, '/pyta/slide/talkingheads_3/set', 'alpha', 0]],
    None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, None,
    None, None, None, horrorcore_couplet_2_screenswitch_strobe,
]
