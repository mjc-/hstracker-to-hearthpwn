# hstracker-to-hearthpwn
hack to export decks to hearthpwn from epix37's badass tracker

requires python3, requests, and beautifulsoup4

if you have python v3 already, a pip install requests and pip install beautifulsoup4 should be enough

then, run ./dump-hearthpwn-map.py once to pull down the deckbuilder pages that will give us a map from
card names to hearthpwn's wonderful ID format that is different from EVERY OTHER SITE.

then you can run ./deck-file-to-deckbuiler-url.py <class> path.to.deck.txt
to generate the url.

Example using Senfglas' awesome Grim Patron warrior deck.

Create deck.txt by using the tracker's Copy names to clipboard. 

```shell
$ cat deck.txt
Execute x 2
Whirlwind x 2
Fiery War Axe x 2
Battle Rage x 2
Commanding Shout
Slam x 2
Cruel Taskmaster x 2
Frothing Berserker x 2
Warsong Commander x 2
Death's Bite x 2
Unstable Ghoul x 2
Acolyte of Pain x 2
Dread Corsair x 2
Gnomish Inventor x 2
Grim Patron x 2
Emperor Thaurissan
$ ./deck-file-to-deckbuiler-url.py warrior deck.txt
http://www.hearthpwn.com/deckbuilder/warrior#227:2;161:2;632:2;664:2;166:1;215:2;328:2;69:2;193:2;7734:2;7757:2;428:2;261:2;246:2;14435:2;14454:1;
$
```

