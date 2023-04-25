# Pelin arkkitehtuuri
Fleet Zeron rakenne noudattaa seuraavanlaista arkkitehtuuria:


![kuva](https://user-images.githubusercontent.com/88443840/232872179-66200a9c-a65c-40e8-9988-1019cbea8894.png)


## Pelaajan liikkuminen

Tämä kaavio kuvaa pelaajan liikkumista. Nuolinäppäimiä painattaessa peli tarkistaa, onko pelaaja ruudun laidalla ja onko pelaajan haluama suunta laitoja päin. Jos pelaaja on menossa yli ruudun laitojen, liikkumista ei suoriteta. Lisäksi turbon ollessa päällä, pelaajan pelialuksen ```speed``` on normaalia korkeampi, jolloin myös liikkuminen on nopeampaa.


![kuva](https://user-images.githubusercontent.com/88443840/234400145-7d9c691b-648b-4f4b-a5b9-cc36e4f3f08d.png)
