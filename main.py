from models.SzemelyAuto import Szemelyauto
from models.TeherAuto import Teherauto
from models.AutoKolcsonzes import Autokolcsonzo


def rendszer_inditas():
    kolcsonzo = Autokolcsonzo("BestRent")

    a1 = Szemelyauto("AAA-111", "Toyota", 10000, 5)
    a2 = Szemelyauto("BBB-222", "Honda", 12000, 5)
    a3 = Teherauto("CCC-333", "Volvo", 20000, 15000)

    kolcsonzo.auto_hozzaad(a1)
    kolcsonzo.auto_hozzaad(a2)
    kolcsonzo.auto_hozzaad(a3)

    # kezdeti bérlések
    kolcsonzo.auto_berles("AAA-111", "2026-05-20", "János")
    kolcsonzo.auto_berles("BBB-222", "2026-05-21", "Dávid")
    kolcsonzo.auto_berles("CCC-333", "2026-05-22", "Ariel")
    kolcsonzo.auto_berles("AAA-111", "2026-05-23", "Jax")

    return kolcsonzo


def menu():
    kolcsonzo = rendszer_inditas()

    while True:
        print("\n1 - Bérlés")
        print("2 - Lemondás")
        print("3 - Bérlések listázása")
        print("4 - Autók listázása")
        print("0 - Kilépés")

        v = input(">> ")

        try:
            if v == "1":
                kolcsonzo.autok_listazasa()

                nev = input("Név: ")
                rendszam = input("Rendszám: ")
                datum = input("Dátum: ")

                ar = kolcsonzo.auto_berles(rendszam, datum, nev)
                print(f"Sikeres bérlés! Ár: {ar} Ft")

            elif v == "2":
                nev = input("Név: ")

                sajat = kolcsonzo.berlesek_nev_alapjan(nev)

                if not sajat:
                    print("Nincs bérlésed.")
                    continue

                print("\nSaját bérléseid:")
                for i, b in enumerate(sajat):
                    print(f"{i + 1}. {b.get_auto().get_rendszam()} - {b.get_datum()}")

                idx = int(input("Melyiket mondod le? ")) - 1

                valasztott = sajat[idx]

                kolcsonzo.berles_lemondas(
                    valasztott.get_auto().get_rendszam(),
                    valasztott.get_datum()
                )

                print("Sikeres lemondás!")

            elif v == "3":
                kolcsonzo.berlesek_listazasa()

            elif v == "4":
                kolcsonzo.autok_listazasa()

            elif v == "0":
                break

        except Exception as e:
            print("Hiba:", e)


if __name__ == "__main__":
    menu()