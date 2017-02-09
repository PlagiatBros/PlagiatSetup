#!/bin/bash
Name=$1
FunctionID=$2
FixtureID=$3
Channel=$4
Dimmer=$5
File=$6

echo '<Function Type="Scene" Name="'$Name'" ID="'$FunctionID'">' >> $File
echo '<Speed Duration="0" FadeOut="0" FadeIn="0"/>' >> $File
echo '<FixtureVal ID="'$FixtureID'">'$Channel','$Dimmer'</FixtureVal>' >> $File
echo '</Function>' >> $File
