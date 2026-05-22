from models.Berles import Berles
from datetime import datetime


class Autokolcsonzo:
    def __init__(self, nev):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    # --- AUTÓK ---
    def auto_hozzaad(self, auto):
        self._autok.append(auto)

    def auto_keres(self, rendszam):
        for auto in self._autok:
            if auto.get_rendszam() == rendszam:
                return auto
        return None

    # --- ELÉRHETŐSÉG ---
    def auto_elerheto(self, rendszam, datum):
        for b in self._berlesek:
            if b.get_auto().get_rendszam() == rendszam and b.get_datum() == datum:
                return False
        return True

    # --- BÉRLÉS (🔥 + NÉV) ---
    def auto_berles(self, rendszam, datum, nev):
        auto = self.auto_keres(rendszam)

        if not auto:
            raise Exception("Nincs ilyen autó!")

        if not self.auto_elerheto(rendszam, datum):
            raise Exception("Az autó nem elérhető!")

        uj = Berles(auto, datum, nev)
        self._berlesek.append(uj)

        return auto.get_berleti_dij()

    # --- NÉV SZŰRÉS ---
    def berlesek_nev_alapjan(self, nev):
        return [b for b in self._berlesek if b.get_nev() == nev]

    # --- LEMONDÁS ---
    def berles_lemondas(self, rendszam, datum):
        for b in self._berlesek:
            if b.get_auto().get_rendszam() == rendszam and b.get_datum() == datum:
                self._berlesek.remove(b)
                return

        raise Exception("Nincs ilyen bérlés!")

    # --- LISTÁZÁS ---
    def berlesek_listazasa(self):
        if not self._berlesek:
            print("Nincsenek bérlések.")
            return

        for b in self._berlesek:
            print(f"{b.get_nev()} | {b.get_auto().get_rendszam()} | {b.get_datum()}")

    # --- AUTÓK LISTÁZÁSA ---
    def autok_listazasa(self):
        for auto in self._autok:
            print(auto.info())