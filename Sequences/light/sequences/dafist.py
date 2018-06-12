import sys
sys.path.append("../Controls/Mididings/")

from ports import *

dafist_clignotage = [
    [':/Lightseq/Scene/Play', 'dafist_clignotageA'],[':/Lightseq/Scene/Play', 'dafist_clignotageB']
]

dafist_entreeinstru_leslie = [
    [[':/Lightseq/Scene/Play', 'dafist_leslie_o'],[':/Lightseq/Scene/Play', 'dafist_leslie_j']], None, None, None,
    None, None, None, None
]

dafist_roulettearabesques = [
    [[':/Lightseq/Scene/Play', 'dafist_roulettearabesques'],[4444,'/oui']],
    [4444,'/ouioui']
]


dafist_themerefrain_clignotagestrob = [

    [[':/Lightseq/Sequence/Enable', 'dafist_clignotage'],[':/Lightseq/Scene/Play', 'dafist_patatetemps']], [':/Lightseq/Scene/Play', 'dafist_patatetemps'], None, None,
    [':/Lightseq/Scene/Play', 'dafist_patatesyncope'], None, None, [':/Lightseq/Scene/Play', 'dafist_patatesyncope'],
    None, None, None, None,
    [':/Lightseq/Scene/Play', 'dafist_patatesyncope'], None, None, [[':/Lightseq/Sequence/Disable', 'dafist_clignotage'], [':/Lightseq/Scene/Play', 'dafist_blinderstrob'], [':/Lightseq/Scene/Play', 'dafist_vpoff']],

    [[':/Lightseq/Sequence/Enable', 'dafist_clignotage'],[':/Lightseq/Scene/Play', 'dafist_patatetemps']], [':/Lightseq/Scene/Play', 'dafist_patatetemps'], None, None,
    [':/Lightseq/Scene/Play', 'dafist_patatesyncope'], None, None, [':/Lightseq/Scene/Play', 'dafist_patatesyncope'],
    None, None, None, None,
    None, None, None, [[':/Lightseq/Sequence/Disable', 'dafist_clignotage'], [':/Lightseq/Scene/Play', 'dafist_blinderstrob'], [':/Lightseq/Scene/Play', 'dafist_vpoff']]

]

dafist_refrain = [

    [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1],[rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0, 0, 0]], [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]], [rpijardinport, '/pyta/slide/visible', -1, 0], None,
    [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]], [rpijardinport, '/pyta/slide/visible', -1, 0], None, [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]],
    [rpijardinport, '/pyta/slide/visible', -1, 0], None, None, None,
    [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]], [rpijardinport, '/pyta/slide/visible', -1, 0], None, [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]],

    [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1],[rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0, 0, 0]], [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]], [rpijardinport, '/pyta/slide/visible', -1, 0], None,
    [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]], [rpijardinport, '/pyta/slide/visible', -1, 0], None, [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]],
    [rpijardinport, '/pyta/slide/visible', -1, 0], None, None, None,
    None, None, None, [[rpijardinport, '/pyta/slide/animate', 'GoatEye_10', 'scale_x', 350, 800, 0.1 ],[rpijardinport, '/pyta/slide/visible', 'GoatEye_10', 1], [rpijardinport, '/pyta/slide/rgb', 'GoatEye_10', 0.9, 0, 0]]

]
