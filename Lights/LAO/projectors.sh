#!/bin/bash

bcj_name="CJ"
bcc_name="CC"
bbj_name="BJ"
bbc_name="BC"

bcj_basechannel=0
bcc_basechannel=0
bbj_basechannel=0
bbc_basechannel=0

bcj_fixtureID=0
bcc_fixtureID=4
bbj_fixtureID=1
bbc_fixtureID=3


rouge="Red"
bleu="Blue"
vert="Green"

baseId=0

./projector.sh "$bcj_name $rouge" $baseId $bcj_basechannel $bcj_fixtureID 255
./projector.sh "$bcj_name $vert" $(echo "$baseId+8"|bc) $(echo "$bcj_basechannel+1"|bc) $bcj_fixtureID 255
./projector.sh "$bcj_name $bleu" $(echo "$baseId+16"|bc) $(echo "$bcj_basechannel+2"|bc) $bcj_fixtureID 255

./projector.sh "$bcc_name $rouge" $(echo "$baseId+24"|bc) $bcc_basechannel $bcc_fixtureID 255
./projector.sh "$bcc_name $vert" $(echo "$baseId+32"|bc) $(echo "$bcc_basechannel+1"|bc) $bcc_fixtureID 255
./projector.sh "$bcc_name $bleu" $(echo "$baseId+40"|bc) $(echo "$bcc_basechannel+2"|bc) $bcc_fixtureID 255

./projector.sh "$bbj_name $rouge" $(echo "$baseId+48"|bc) $bbj_basechannel $bbj_fixtureID 255
./projector.sh "$bbj_name $vert" $(echo "$baseId+56"|bc) $(echo "$bbj_basechannel+1"|bc) $bbj_fixtureID 255
./projector.sh "$bbj_name $bleu" $(echo "$baseId+64"|bc) $(echo "$bbj_basechannel+2"|bc) $bbj_fixtureID 255

./projector.sh "$bbc_name $rouge" $(echo "$baseId+72"|bc) $bbc_basechannel $bbc_fixtureID 255
./projector.sh "$bbc_name $vert" $(echo "$baseId+80"|bc) $(echo "$bbc_basechannel+1"|bc) $bbc_fixtureID 255
./projector.sh "$bbc_name $bleu" $(echo "$baseId+88"|bc) $(echo "$bbc_basechannel+2"|bc) $bbc_fixtureID 255
