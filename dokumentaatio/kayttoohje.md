# Käyttöohje

Lataa ohjelman viimeisin release täältä: [release 2](https://github.com/MegafoS/ot-harjoitustyo/releases/tag/viikko6

## Pelin käynnistäminen

Jos sinulla on jo poetry asennettuna, voit ohittaa alla olevat vaiheet ja siirtyä pelin käynnistämiseen.

Asenna pelin riippuvuudet komennoilla:

```bash
poetry install
```
```bash
poetry run invoke build
```

Käynnistä peli komennolla:

```
poetry run invoke start
```
Peli alkaa suoraan kun se on käynnistetty.

## Näppäinasetukset

Tässä ovat kaikki näppäimet joita voit pelatessa käyttää:

Liikkuminen: Nuolinäppäimet

Ampuminen: X / Välilyönti

Turbo: Vasen shift

Osuminen vihollisaluksiin vahingoittaa sinua. Jos vihollisalus pääsee ohitsesi, menetät lisäelämän.
Kerää mahdollisimman paljon pisteitä tuhoamalla vihollisaluksia ennen kuin menetät kaikki lisäelämät!
