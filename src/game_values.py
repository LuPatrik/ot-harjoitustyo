class GameValues:
    """Yksinkertainen luokka, jossa määritellään joukko pelille tärkeitä tietoja."""
    def __init__(self):
        """Luokan konstruktori.
            self.screen_size määrittää peliruuduun koon.
            self.fps määrittää kuinka moneen kertaan peliruutu päivitetään sekunnissa.
            samalla määrittää pelin nopeuden.
            self.name määrittää pelin nimen.
            self.level määrittää pelin tason."""
        self.screen_size = (800,800)
        self.fps = 60
        self.name = "Fleet Zero"
        self.level = 1
