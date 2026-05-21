from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: float,
                 teherbiras: float, tengelyek_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras
        self.tengelyek_szama = tengelyek_szama

    def info(self):
        return (
            f"Teherautó - {self.tipus}\n"
            f"Rendszám: {self.rendszam}\n"
            f"Bérleti díj: {self.berleti_dij} Ft/nap\n"
            f"Teherbírás: {self.teherbiras} kg\n"
            f"Tengelyek száma: {self.tengelyek_szama}"
        )