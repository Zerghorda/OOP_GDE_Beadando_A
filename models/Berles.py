class Berles:
    def __init__(self, auto, datum, nev):
        self._auto = auto
        self._datum = datum
        self._nev = nev

    def get_auto(self):
        return self._auto

    def get_datum(self):
        return self._datum

    def get_nev(self):
        return self._nev

    def __str__(self):
        return f"{self._nev} | {self._auto.get_rendszam()} | {self._datum}"