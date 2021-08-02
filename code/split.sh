#!/usr/bin/env bash
# split.sh

srcDir='../art files/exports'
cardDir='../cards'

mkdir -p "$cardDir"
convert "$srcDir/card corners atlas.png" -crop 8x8@ +repage +adjoin "$cardDir/%d.png"

