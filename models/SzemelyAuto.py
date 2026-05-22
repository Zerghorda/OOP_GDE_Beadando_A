from models.Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ferohelyek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ferohelyek_szama = ferohelyek_szama

    def info(self):
        return f"[Személyautó] {self._tipus} | {self._rendszam} | {self._berleti_dij} Ft/nap | {self._ferohelyek_szama} fő"