from models.Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras

    def info(self):
        return f"[Teherautó] {self._tipus} | {self._rendszam} | {self._berleti_dij} Ft/nap | {self._teherbiras} kg"
