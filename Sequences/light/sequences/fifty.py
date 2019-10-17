#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *



fifty_offre_emploi = [
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche tondeur débroussailleur sexy raffiné\n URGENT\n contact: epilation@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche tondeuse débroussailleuse Briggs et Stratton\n URGENT\n contact: deb@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Aimerait : retour de l'être aimé, départ de l'être pas aimé\n URGENT\n contact: grandgourou@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Trouverait plan de carrière 100% réussite\n URGENT\n contact: medium@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text/1/set', 'text', "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpicourport, '/pyta/text/2/set', 'text', "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
]

fifty_offre_emploi_strobe = [
  [[rpijardinport, '/pyta/text/strobe', 0, 1, 5, 0.5], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 1, 5, 0.5], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 1, 5, 0.5], [rpijardinport, '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [[rpijardinport, '/pyta/text/strobe', 0, 1, 5, 0.5], [rpijardinport, '/pyta/text/strobe', 1, 1, 5, 0.5], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 1, 5, 0.5], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [[rpijardinport, '/pyta/text/strobe', 0, 1, 5, 0.5], [rpijardinport, '/pyta/text/strobe', 1, 1, 5, 0.5], [rpijardinport, '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],
  [[rpijardinport, '/pyta/text/strobe', 0, 0], [rpijardinport, '/pyta/text/strobe', 1, 0], [rpijardinport, '/pyta/text/strobe', 2, 0]],

  [[rpicourport, '/pyta/text/strobe', 0, 1, 5, 0.5], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 1, 5, 0.5], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 1, 5, 0.5], [rpicourport, '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [[rpicourport, '/pyta/text/strobe', 0, 1, 5, 0.5], [rpicourport, '/pyta/text/strobe', 1, 1, 5, 0.5], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 1, 5, 0.5], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [[rpicourport, '/pyta/text/strobe', 0, 1, 5, 0.5], [rpicourport, '/pyta/text/strobe', 1, 1, 5, 0.5], [rpicourport, '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],
  [[rpicourport, '/pyta/text/strobe', 0, 0], [rpicourport, '/pyta/text/strobe', 1, 0], [rpicourport, '/pyta/text/strobe', 2, 0]],

  [['/pyta/text/strobe', 0, 1, 5, 0.5], ['/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], ['/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [['/pyta/text/strobe', 0, 0], ['/pyta/text/strobe', 1, 1, 5, 0.5], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], ['/pyta/text/strobe', 1, 1, 5, 0.5], [ '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [['/pyta/text/strobe', 0, 1, 5, 0.5], ['/pyta/text/strobe', 1, 1, 5, 0.5], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 1, 5, 0.5], ['/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [['/pyta/text/strobe', 0, 1, 5, 0.5], ['/pyta/text/strobe', 1, 1, 5, 0.5], [ '/pyta/text/strobe', 2, 1, 5, 0.5]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],
  [['/pyta/text/strobe', 0, 0], [ '/pyta/text/strobe', 1, 0], [ '/pyta/text/strobe', 2, 0]],

]

colos = " ".join(['Colo_'+str(i) for i in range(1,47)])
twerks = " ".join(['Twerk_'+str(i) for i in range(1,33)])


# TODO: telescopage reseau ? petre utiliser posz a la place
fifty_colo_jardin = []
fifty_colo_cour = []
for i in range(1,47):
  fifty_colo_jardin.append([[rpijardinport, '/pyta/slide/visible', colos, 0], [rpijardinport, '/pyta/slide/visible', 'Colo_'+str(i), 1]])
  fifty_colo_cour.append([[rpicourport, '/pyta/slide/visible', colos, 0], [rpicourport, '/pyta/slide/visible', 'Colo_'+str(i), 1]])

fifty_coffee = [
  None, None, None, None,
  None, None, None, None,
  None, None, None, None,
  None, None, [':/Lightseq/Scene/Play', 'fifty_tea'], None
]


fifty_twerk = [
    [':/lightseq/scene/play', 'fifty_twerk_1'],
    [':/lightseq/scene/play', 'fifty_twerk_1'],
    [':/lightseq/scene/play', 'fifty_twerk_1'],
    [':/lightseq/scene/play', 'fifty_twerk_2'],
    [':/lightseq/scene/play', 'fifty_twerk_3'],
]

fifty_nymphotrap_blow = [
  [[rpijardinport, '/pyta/text/animate', 2, 'size', 0.12, 0.13, 0.1],[rpicourport, '/pyta/text/animate', 1, 'size', 0.2, 0.21, 0.1]]
]

fifty_stagier = [
  None, None, None, [['/pyta/text', 0, '??'], ['/pyta/text/visible', 0, 1], ['/pyta/slide/alpha', twerks, 0.01]],
  [['/pyta/text/visible', 0, 0], ['/pyta/slide/alpha', twerks, 1]], None, None, [['/pyta/text', 2, 'Stagière'], ['/pyta/text/visible', 2, 1], ['/pyta/slide/alpha', twerks, 0.01]],
  [['/pyta/text/visible', 2, 0],['/pyta/slide/alpha', twerks, 1]], None, None, None,
  None, None, None, [['/pyta/text', 2, 'Stajiärhee'], ['/pyta/text/visible', 2, 1], ['/pyta/slide/alpha', twerks, 0.01]],
  [['/pyta/text/visible', 2, 0],['/pyta/slide/alpha', twerks, 1]], None, None, [['/pyta/text', 0, '????'], ['/pyta/text/visible', 0, 1], ['/pyta/slide/alpha', twerks, 0.01]],
  [['/pyta/text/visible', 0, 0], ['/pyta/slide/alpha', twerks, 1]], None, None, [['/pyta/text', 2, 'Stajillère'], ['/pyta/text/visible', 2, 1], ['/pyta/slide/alpha', twerks, 0.01]],
  [['/pyta/text/visible', 2, 0],['/pyta/slide/alpha', twerks, 1]], None, None, [['/pyta/text', 0, 'Qqqq ??'], ['/pyta/text/visible', 0, 1], ['/pyta/slide/alpha', twerks, 0.01]],
  [['/pyta/text/visible', 0, 0], ['/pyta/slide/alpha', twerks, 1]], None, None, None
]
