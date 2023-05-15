# Käyttöohje

Lataa ohjelman viimeisin release täältä: [release 2](https://github.com/MegafoS/ot-harjoitustyo/releases/tag/viikko6)

## Pelin käynnistäminen

Ennen ensimmäistä käynnistämistä, asenna pelin riippuvuudet komennoilla:

```bash
poetry install
```

Käynnistä peli komennolla:

```
poetry run invoke start
```
Peli alkaa kun pelaaja painaa alkuvalikossa ```Start game```

## Näppäinasetukset

Tässä ovat kaikki näppäimet joita voit pelatessa käyttää:

Pelin keskeytys: ESC

Liikkuminen: Nuolinäppäimet

Turbo: Vasen shift

Ampuminen: X / Välilyönti (Turbon täytyy olla pois päältä, jotta ampuminen on mahdollista!)

Osuminen vihollisaluksiin vahingoittaa sinua. Jos vihollisalus pääsee ohitsesi tai menetät kaikki elämäpisteesi, menetät lisäelämän. Peli vaikeutuu jatkuvasti, ja vihollisten määrä kasvaa tasojen edetessä.
Kerää mahdollisimman paljon pisteitä tuhoamalla vihollisaluksia ennen kuin menetät kaikki lisäelämät!

## Keskeytysvalikko

Pelin voi keskeyttää pelisession aikana painamalla ESC näppäintä. Tällöin peli siirtyy keskeytysvalikkoon, josta voi valita ```Resume``` jatkaakseen peliään siitä mihin peli jäi tai ```Quit``` poistuakseen pelistä.
