#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

_offres_jardin = [
    "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n\n URGENT\n contact: stagiärhee@plagiat.org",
    "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n\n URGENT\n contact: DRH-ich@plagiat.org",
    "URGENT\n Rémunération : >NON<\n\n URGENT\n contact: fiducials@plagiat.org",
    "URGENT\n coCOFFEE needed\n\n URGENT\n contact: coco@plagiat.org",
    "URGENT\n looking for interns\n\n URGENT\n contact: coloscopie@plagiat.org"
    "URGENT\n Recherche tondeur débroussailleur sexy raffiné\n\n URGENT\n contact: epilation@plagiat.org",
    "URGENT\n Aimerait : retour de l'être aimé, départ de l'être pas aimé\n\n URGENT\n contact: grandgourou@plagiat.org"
]
_offres_cour = [
    "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n\n URGENT\n contact: stagiärhee@plagiat.org",
    "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n\n URGENT\n contact: DRHaschich@plagiat.org",
    "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n\n URGENT\n contact: financier@plagiat.org",
    "URGENT\n CCoffee NEEDED\n\n URGENT\n contact: ccoffee@plagiat.org",
    "URGENT\n Looking for internstines\n\n URGENT\n contact: intestins@plagiat.org",
    "URGENT\n Recherche tondeuse débroussailleuse Briggs et Stratton\n\n URGENT\n contact: deb@plagiat.org",
    "URGENT\n Trouverait plan de carrière 100% réussite\n\n URGENT\n contact: medium@plagiat.org",
]

fifty_offre_emploi_jardin = [[rpijardinport, '/pyta/text/1/set', 'text', x] for x in _offres_jardin]
fifty_offre_emploi_cour = [[rpicourport, '/pyta/text/1/set', 'text', x] for x in _offres_cour]

fifty_coffee = [
  ['/pyta/slide/tea_1/set', 'alpha', 0], None, None, None,
  None, None, None, None,
  None, None, None, None,
  None, None, [['/pyta/slide/tea_1/set', 'gif_frame', 2], ['/pyta/slide/tea_1/set', 'alpha', 1]], None
]


fifty_twerk = [
    [['/pyta/slide/twerk_*/set', 'alpha', 0], ['/pyta/slide/twerk_1/set', 'alpha', 1]],
    [['/pyta/slide/twerk_*/set', 'alpha', 0], ['/pyta/slide/twerk_2/set', 'alpha', 1]],
    [['/pyta/slide/twerk_*/set', 'alpha', 0], ['/pyta/slide/twerk_3/set', 'alpha', 1]],
]

fifty_nymphotrap_blow = [
  ['/pyta/text/{1,2}/animate','size', 0.10, 0.11, 0.1, 'sine']
]


stagier = [
    ['/pyta/slide/twerk_*/set', 'visible', 0],
    ['/pyta/text/{1,2}/set', 'alpha', 1],
    ['/pyta/text/{1,2}/set', 'text', 'Stajiärhee', 0.2],

]

stagier_off = [
    ['/pyta/slide/twerk_*/set', 'visible', 1],
    ['/pyta/text/{1,2}/set', 'alpha', 0],
]

pascalo = [
    ['/pyta/post_process/set', 'visible', 1],
]

pascalo_off = [
    ['/pyta/post_process/set', 'visible', 0],
]


fifty_stagier = [
    stagier_off, None, None, None,
    None, None, None, stagier,
    stagier_off, None, pascalo, None,
    pascalo_off, None, None, stagier,
    stagier_off, None, None, None,
    None, None, None, stagier,
    stagier_off, None, None, None,
    None, None, None, stagier,
]


fifty_theme_synth = [
    ['/pyta/slide/johncleesedesabuse/set', 'gif_frame', 0], None, None, None
]
