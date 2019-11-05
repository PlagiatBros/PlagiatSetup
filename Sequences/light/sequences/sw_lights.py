#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

# Vérifier façon de gérer les arguments de scène
sw_moroness_segments = [
    [':/Lightseq/Scene/Play', 'sw_randomized_segment', 180], None,
    [':/Lightseq/Scene/Play', 'sw_randomized_segment', 90], None,
    [':/Lightseq/Scene/Play', 'sw_randomized_segment', 45], None,
    [':/Lightseq/Scene/Play', 'sw_randomized_segment', 22], None,
    [':/Lightseq/Scene/Play', 'sw_randomized_segment', 11], None,
    None, None, None, None
]

sw_refrain_red_flashes = [
    ([[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 255], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 70]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 242], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 82]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 230], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 94]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 218], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 106]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 206], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 118]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 194], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 130]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 182], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 142]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 170], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 154]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 158], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 166]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 146], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 178]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 134], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 190]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 122], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 202]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 110], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 214]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 98], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 226]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 86], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 238]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 70], [qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 255]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 255], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 70]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 242], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 82]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 230], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 94]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 218], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 106]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 206], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 118]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 194], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 130]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 182], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 142]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 170], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 154]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 158], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 166]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 146], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 178]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 134], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 190]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 122], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 202]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 110], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 214]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 98], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 226]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ([[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 86], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 238]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0],
    [[qlcport, '/TuttiCour/Red/Segment/{1,3,6,8}', 70], [qlcport, '/TuttiJardin/Red/Segment/{1,3,6,8}', 255]],
    [qlcport, '/Tutti/Red/Segment/{1,3,6,8}', 0]),

    ]

whiteflashon = [qlcport, '/Tutti/White/Segment/{2,4,5,7}', 255]
whiteflashoff = [[qlcport, '/Tutti/White/Segment/{2,7}', 0], [qlcport, '/TuttiLointain/White/Segment/{4,5}', 200]]
sw_refrain_white_flash = [
    (None, whiteflashon), whiteflashoff, (None, whiteflashon), whiteflashoff,
    (None, whiteflashon), whiteflashoff, (whiteflashon, whiteflashoff), (None, whiteflashon),
    (whiteflashoff, whiteflashon), whiteflashoff, (None, whiteflashon), whiteflashoff,
    (None, whiteflashon), whiteflashoff, (whiteflashon, whiteflashoff), (None, whiteflashon),
    (whiteflashoff, whiteflashon), whiteflashoff, (None, whiteflashon), whiteflashoff,
    (None, whiteflashon), whiteflashoff, (whiteflashon, whiteflashoff), None,
    [':/Lightseq/Scene/Play', 'sw_refrain_strobe'], None, None, [[':/Lightseq/Scene/Stop', 'sw_refrain_strobe']] + whiteflashoff
    ]
