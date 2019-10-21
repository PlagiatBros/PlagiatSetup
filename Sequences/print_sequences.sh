#!/bin/bash
rgrep -Eo "Lightseq/Sequence/Enable', '(.*)'" ./ ../Controls/Mididings/scenes/ | sed "s/.*\.py//" | sed "s/\[':\//\n:/g" | rgrep Enable - | sed "s/[^']*',\s'//" | sed "s/'.*//"
