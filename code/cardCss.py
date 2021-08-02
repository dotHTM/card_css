#!/usr/bin/env python3
# cardCss.py
#   Description
#
#   Written by Mike Cramer
#   Started on DATE

#body

import os, os.path, sys

sizes = {
    'small': {
        'w': 60,
        'h': 80
    },
    'medium': {
        'w': 120,
        'h': 160
    },
    'large': {
        'w': 318,
        'h': 412
    }
}

styles = [
    ', '.join(map(lambda x: f".{x}>i", sizes)) + """{
  color: #0000;
  background-size: contain;
  background-repeat: no-repeat;
  display: inline-block;
}""", '.hand>i{ transform: rotate(5deg); }',
'.hand{color: #0000;}'
]

suitsNyms = {
    'hearts': ['heart', 'h'],
    'spades': ['spade', 's'],
    'diamonds': ['diamond', 'd'],
    'clubs': ['club', 'c'],
}

atlasIndex = 0

cardNyms = {
    1: ["one", "ace", "a"],
    2: ["two"],
    3: ["three"],
    4: ["four"],
    5: ["five"],
    6: ["six"],
    7: ["seven"],
    8: ["eight"],
    9: ["nine"],
    10: ["ten", "x"],
    11: ["jack", "j"],
    12: ["queen", "q"],
    13: ["king", "k"],
}

allNymsList = []


def padl(inputString, strlen, padding="0"):
    if len(str(inputString)) < strlen:
        return padl(str(padding) + str(inputString), strlen, padding)
    return inputString


def wrap(inputString, l, r):
    return f'{l}{inputString}{r}'


wrapBrackets = lambda x: wrap(x, '{', '}')

hyphenation = '-'.join

imgSplitNumber = 0

for s in suitsNyms:
    for c in cardNyms:
        selector = []
        selector.extend([
            f".{s}-{c}", 
            f".{s}-0{c}", 
            f".{s}{c}", 
            f".{s}0{c}", 
            f"._{c}{s}",
            f"._0{c}{s}", 
            f"._{c}-of-{s}", 
            f"._0{c}-of-{s}"
        ])
        for sn in suitsNyms[s]:
            selector.extend([
                f".{sn}-{c}", 
                f".{sn}-0{c}", 
                f".{sn}{c}", 
                f".{sn}0{c}",
                f"._{c}-of-{sn}", 
                f"._0{c}-of-{sn}"
            ])
        for cn in cardNyms[c]:
            selector.extend([
                f".{s}{cn}", 
                f".{cn}{s}", 
                f".{s}-{cn}", 
                f".{cn}-of-{s}"])
            for sn in suitsNyms[s]:
                selector.extend([
                    f".{sn}{cn}", 
                    f".{cn}{sn}", 
                    f".{sn}-{cn}", 
                    f".{cn}-of-{sn}"])
        for size in sizes:
            styles.append(
                ', '.join(map(lambda x: f".{size}>" + x, selector)) +
                wrapBrackets(
                    f"background-image: url('cards/{imgSplitNumber}.png')"))
        imgSplitNumber += 1

for size in sizes:
    overlap = str(int(sizes[size]['w'] * 0.4))
    styles.append(f""".hand.{size}>i""" +
                  wrapBrackets(f""" margin-right: -{overlap}px; """))
    styles.append(f""".{size}>i""" +
                  wrapBrackets(f""" width: {str(sizes[size]['w'])}px; 
        height: {str(sizes[size]['h'])}px; """))

nlw = "\n".join

f = open("../cards.css", "w")
f.write(nlw(styles))
f.close()
"""
body > div > i.h01
"""
