#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

fifty_offre_emploi = [
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n Recherche tondeur débroussailleur sexy raffiné\n URGENT\n contact: epilation@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche tondeuse débroussailleuse Briggs et Stratton\n URGENT\n contact: deb@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Aimerait : retour de l'être aimé, départ de l'être pas aimé\n URGENT\n contact: grandgourou@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Trouverait plan de carrière 100% réussite\n URGENT\n contact: medium@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Rémunération : >NON<\n URGENT\n contact: fiducials@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Pas de ça entre nous, on est avant tout une équipe\n URGENT\n contact: financier@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n coCOFFEE needed\n URGENT\n contact: coco@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n CCoffee NEEDED\n URGENT\n contact: ccoffee@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n looking for interns\n URGENT\n contact: coloscopie@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Looking for internstines\n URGENT\n contact: intestins@plagiat.org"]],
  [[rpijardinport, '/pyta/text', 1, "URGENT\n Recherche jeune femme (h/f) pour stage-CDI 48 heures\n URGENT\n contact: stagiärhee@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune homme (h/f) pour stage-CDI 48 heures.\n URGENT\n contact: stagiärhee@plagiat.org"]],
  [[rpicourport, '/pyta/text', 2, "URGENT\n Recherche jeune (engagement total) pour convention benevolat 66 heures\n URGENT\n contact: DRH-ich@plagiat.org"],[rpijardinport, '/pyta/text', 2, "URGENT\n Recherche jeune (35 ans exp. mini) pour service cinique 66 h.\n URGENT\n contact: DRHaschich@plagiat.org"]],

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

colos=""
for i in range(1,47):
  colos.append('Colo_'+str(i)+' ')

fifty_colo_jardin = []
fifty_colo_cour = []
for i in range(0,46):
  fifty_colo_jardin.append([[rpijardinport, '/pyta/slide/visible', colos, 0], [rpijardinport, '/pyta/slide/visible'], 'Colo_'+str(i), 1])
  fifty_colo_cour.append([[rpicourport, '/pyta/slide/visible', colos, 0], [rpicourport, '/pyta/slide/visible'], 'Colo_'+str(i), 1])
  
fifty_coffee = [
  None, None, None, None,
  None, None, None, None,
  None, None, None, None,
  None, None, [':/Lightseq/Scene/Play', 'fifty_tea'], None
]

twerks=""
for i in range(1,100):
  twerks.append("Twerk_"+str(i)+" ")

fifty_twerk_jardin=[]
fifty_twerk_cour=[]             
for i in range(0,5):
    fifty_twerk_jardin.append([[rpijardinport, '/pyta/slide/visible', twerks, 0],[rpijardinport, '/pyta/slide/visible', 'Twerk_1.gif']])
    fifty_twerk_cour.append([[rpicourport, '/pyta/slide/visible', twerks, 0],[rpicourport, '/pyta/slide/visible', 'Twerk_1.gif']])
for i in range(0,2):
    fifty_twerk_jardin.append([[rpijardinport, '/pyta/slide/visible', twerks, 0],[rpijardinport, '/pyta/slide/visible', 'Twerk_2.gif']])
    fifty_twerk_cour.append([[rpicourport, '/pyta/slide/visible', twerks, 0],[rpicourport, '/pyta/slide/visible', 'Twerk_2.gif']])

fifty_twerk_jardin.append([[rpijardinport, '/pyta/slide/visible', twerks, 0],[rpijardinport, '/pyta/slide/visible', 'Twerk_3.gif']])
fifty_twerk_cour.append([[rpicourport, '/pyta/slide/visible', twerks, 0],[rpicourport, '/pyta/slide/visible', 'Twerk_3.gif']])

fifty_nymphotrap_blow = [
  [[rpijardinport, '/pyta/text/animate', 2, 'scale_x', 780, 800, 0.1],[rpicourport, '/pyta/text/animate', 1, 'scale_x', 780, 800, 0.1]]
]
