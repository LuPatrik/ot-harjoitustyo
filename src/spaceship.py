class Spaceship:
    """Luokka joka määrittää alusten perustiedot. Pelaajan aluksen ja vihollisalusten 
    luokat perivät tiedot tältä luokalta.
        Attributes:
                x_coord: Määrittää aluksen sijainnin x akselilla.
                y_coord: Määrittää aluksen sijainnin y akselilla.
                speed: Määrittää aluksen nopeuden
                health: Määrittää aluksen elämäpisteet"""
    def __init__(self, x_coord, y_coord, speed, health):
        """Luokan konstruktori.
            Args:
                x_coord: Määrittää aluksen sijainnin x akselilla.
                y_coord: Määrittää aluksen sijainnin y akselilla.
                speed: Määrittää aluksen nopeuden
                health: Määrittää aluksen elämäpisteet

            Näiden lisäksi konstruktori asettaa aluksen ampumisnopeuden,
            tämän hetkisen vahinkoimmuniteetin.
            """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.base_speed = speed
        self.health = health
        self.speed = speed
        self.current_shot_cooldown = 0
        self.shot_cooldown = 200
        self.damage_immunity = 0
    def hit(self, damage):
        """Alus ottaa vahinkoa hit funktiolla.
            Args:
                damage: Määrittää kuinka paljon vahinkoa alus ottaa.
            
            Heti, kun alus on ottanut vahinkoa, se ei voi ottaa hetkeen 
            uudestaan vahinkoa, koska hit funktio asettaa vahinkoimmuniteetin
            20:een
            """
        self.health -= damage
        self.damage_immunity = 20
    def damage_immunity_update(self):
        """Funtkio, joka päivittää tämän hetkisen vahinkoimmuniteetin ajan.
            Jos vahinkoimmuniteetti on enemmän kuin 0, se vähentää sen kestoa."""
        if self.damage_immunity > 0:
            self.damage_immunity -= 1
            