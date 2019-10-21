#!/bin/bash
rgrep -Eo "Lightseq/Scene/Play', '(.*)'" ./ ../Controls/Mididings/scenes/ | sed "s/.*\.py//" | sed "s/\[':\//\n:/g" | rgrep Play - | sed "s/[^']*',\s'//" | sed "s/'.*//"
