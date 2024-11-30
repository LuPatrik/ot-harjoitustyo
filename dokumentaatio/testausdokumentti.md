# Testausdokumentti

Fleet Zeroa on testattu manuaalisesti kokeilemalla, sekä pylintissä luotujen testien avulla.

## Fleet Zeron testit

Fleet Zeron testit ollaan luotu tiedostoon ```fleet_zero_test.py```. Testitiedosto sisältää luokan ```TestFleetZero```, jossa sisältää kaikki Fleet Zerolle muodostetut pylint testit. 
```TestFleetZero```:lle on importtattu kaikki tarvittavat luokat ja funktiot, joita testit tarvitsevat.

## Testauskattavuus

Tämä kuva on ```poetry run invoke coverage-report``` komennolla luotu testauskattavuus. Testauksen haarautumakattavuus on tällä hetkellä 59%.

![kuva](https://github.com/MegafoS/ot-harjoitustyo/assets/88443840/f8100f1d-7616-4e0b-98da-2874883d8fb8)


## Järjestelmätestaus

Fleet Zeron kaikki järjestelmätestaukset ollaan suoritettu manuaalisesti.

Fleet Zeron pelaamista ollaan testattu Windows ja Linux ympäristössä. Toiminnallisuutta ei olla testattu macOS ympäristössä.

Fleet Zeron toiminnallisuutta ollaan testattu tietokoneilla, joilla on sekä matala että korkea suorituskyky positiivisin tuloksin.
