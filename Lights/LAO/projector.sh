#!/bin/bash
ProjectorName=$1
FunctionBaseID=$2
BaseChannel=$3
FixtureID=$4
Dimmer=$5



for i in 1 2 3 4 5 6 7 8
do
Name="$ProjectorName Segment $i"
FunctionID=$(echo "$FunctionBaseID+$i-1"|bc)
Channel=$(echo "$BaseChannel+($i-1)*3" |bc)
./scene_create.sh "$Name" $FunctionID $FixtureID $Channel $Dimmer moncul

done

