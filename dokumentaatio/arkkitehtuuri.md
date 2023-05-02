# Pelin arkkitehtuuri

## Rakenne
Fleet Zeron rakenne noudattaa seuraavanlaista rakennetta:


![kuva](https://user-images.githubusercontent.com/88443840/235754414-6af0ddec-279d-40f3-983c-fb169b1f5ace.png)

## Sovelluslogiikka

Pelin rakenne perustuu päätiedoston, fleet_zero.py:n ympärille. Pelin pääsilmukka käynnistyy, kun päätiedosto suoritetaan ja päättyy, kun pelaaja painaa ESC näppäintä tai häviää.



### Pelaajan aluksen ja vihollisalusten luominen

Pelaajan alus ja vihollisalukset perivät tietoja luokalta ```Spaceship```. 
Luokka ```Spaceship``` asettaa kaikille aluksille seuraavat tiedot: ```(x_coord, y_coord, speed, health)```.
```x_coord``` ja ```y_coord``` asettavat aluksen sijainnin, ```speed``` nopeuden ja ```health``` elämäpisteet.



### Pelaajan liikkuminen

Tämä kaavio kuvaa pelaajan liikkumista ylöspäin: 

![kuva](https://user-images.githubusercontent.com/88443840/235771884-cc267f1f-84b1-4d77-b2a7-53e0754c131f.png)
Pelaajan painaessa ylöspäin ```fleet_zero``` kutsuu ```player_actions``` funktiota, joka vastaa pelaajan antamista painalluksista. ```player_actions``` tarkista, jos pelaaja on menossa yli ruudun ylälaidan. Kun pelaaja painaa nuolta ylöspäin ja ei ole ruudun ylälaidassa, ```player_actions``` vähentää pelaajan aluksen sijaintia y-akselilla, joka taas saa pelaajan aluksen liikkumaan ylöspäin.


Tämä kuvaa pelaajan liikkumista, kun turbo on päällä:

![kuva](https://user-images.githubusercontent.com/88443840/235771566-b0820dbc-e23c-4d27-89fe-d114b6604bd1.png)
Pelaaja painaa yhtäaikaisesti nuolta ylöspäin ja vasenta shiftiä. Edelleen ```fleet_zero``` kutsuu ```player_actions``` funktiota. Shiftin ollessa painettuna, se asettaa pelaajan aluksen nopeuden kahdeksaan ja turbon päälle. Sen jälkeen ```player_actions``` tarkistaa jos ehdot täyttyvät ja niiden täyttyessä se liikuttaa pelaajaa nyt korkeammalla nopeudella.

### Pelaajan ampuminen

Tämä kaavio kuvaa pelaajan ampumista: 
![kuva](https://user-images.githubusercontent.com/88443840/235775416-12ff788f-99c6-4558-aedc-f46dfba52d0d.png)
Pelaaja painaa ampumisnäppäintä, joka kutsuu ```player_actions``` funktiota. Koska pelaaja ei paina shift näppäintä, ja turbo on oletuksena pois päältä, ```player_actions``` kutsuu ```PlayerShip``` funktiota ```shoot```. Funktio ```shoot``` tarkistaa, onko viimeisimmästä onnistuneesta ampumisesta tarpeeksi aikaa, että voidaan suorittaa ampuminen. Jos on, se lisää uuden luodin pelaajan luotilistaan.

