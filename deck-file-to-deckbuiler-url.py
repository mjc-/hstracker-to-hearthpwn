#!/usr/bin/env python

import sys

card_map = 'hearthpwn-card-map.tsv'
deck_class = sys.argv[1]
deck_path = sys.argv[2]

with open (card_map, "r") as mapfile:
        lines=mapfile.readlines()

card_map = {}
for line in lines:
        cols = line.rstrip().split('\t')
        card_map[cols[0]] = cols[1]

deck_url = 'http://www.hearthpwn.com/deckbuilder/%s#' % deck_class
with open (deck_path, "r") as deckfile:
        lines=deckfile.readlines()

for line in lines:
  r = line.rstrip().split(' x 2')
  if len(r) > 1:
   count = '2'
  else:
   count = '1'
  card_id = card_map[r[0]]
  deck_url = deck_url + card_id + ':' + count + ';'

print(deck_url)

