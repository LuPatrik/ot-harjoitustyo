# Fleet Zero

Fleet Zero on Space Invadersin tyylinen videopeli. Peli on vielä työn alla, mutta pelin runko on suurimmaksi osaksi toteutettu ja on valmis pelattavaksi.

**HUOM:** Fleet Zero vaatii vähintään Python version `3.8`. Peliä ei ole testattu vanhemmilla versioilla. 

Ohjeet käynnistykseen:
1. Lataa julkaisu
2. Pura tiedosto
3. Asenna poetry (ohjeet käyttohjeessa)
4. Suorita terminaalissa komento:
```bash
poetry run invoke start
```
Käynnistäminen terminaalin kauttaa vaatii myös poetryn. Vaihtoehtoisesti voit purkaa tiedoston, avata src kansion ja käynnistää pelin fleet_zero.py tiedoston kautta.

## Näppäimet:
Nuolinäppäimet: Liikkuminen

X tai välilyönti: Ampuminen

LShift: Turbo

## Dokumentaatio

[kayttoohje.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[vaatimusmaarittely.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[changelog.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[release 2](https://github.com/MegafoS/ot-harjoitustyo/releases/tag/viikko6)

[release 1](https://github.com/MegafoS/ot-harjoitustyo/releases/tag/viikko5)

## Komennot
Lista komennoista, joita voidaan suorittaa

Käynnistää pelin:
```bash
poetry run invoke start
```

Suorittaa pelin testit:
```bash
poetry run invoke test
```

Muodostaa testikattavuusraportin pelistä:
```bash
poetry run invoke coverage-report
```

Testaa ohjelman koodin pylintin mukaan:
```bash
poetry run invoke lint
```

