#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import pprint
import time

hs_classes = [ 'druid', 'hunter', 'mage', 'paladin', 'priest', 'rogue', 'shaman', 'warlock', 'warrior' ]

card_map = {}
for hs_class in hs_classes:
  url = 'http://www.hearthpwn.com/deckbuilder/%s' % hs_class
  print("Fetching %s Deckbuilder from %s" % (hs_class, url))
  data = requests.get(url)
  doc = BeautifulSoup(data.text)
  elems = doc.find_all('tr', 'deck-card-link')
  for elem in elems:
    card_map[elem.get('data-name')] =  elem.get('data-id')
  # don't just hammer the site
  time.sleep(1)
print('Dumping card map')
with open('hearthpwn-card-map.tsv', 'w') as outfile:
  for card, id in card_map.items():
    outfile.write('%s\t%s\n' % (card, id)) 

print('Done')
