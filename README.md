# Fleet Zero

Fleet Zero on Space Invadersin tyylinen videopeli. Tällä hetkellä peli on vielä työn alla, mutta pelaajan aluksen liikkuminen, turbo, ampuminen ja törmäyshavainto toimivat.

**HUOM:** Fleet Zero vaatii vähintään Python version `3.8`. Peliä ei ole testattu vanhemmilla versioilla.

## Dokumentaatio

[vaatimusmaarittely.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[changelog.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/MegafoS/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

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
