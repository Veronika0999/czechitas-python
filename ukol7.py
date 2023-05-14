class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
   
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."
       
    def get_info(self):
        return f"Vozidlo {self.typ_vozidla} má registrační značku {self.registracni_znacka} "
    
    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.stav_tachometru = stav_tachometru
        self.dostupnost = True
        
        if pocet_dni < 7:
            cena = pocet_dni * 300
            return f"Cena za půjceni auta je {cena}."
        else:
            cena = pocet_dni * 400
            return f"Cena za půjčení auta je {cena}."
       
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

user = input("Jakou značku auta si přejete (Skoda nebo Peugeot)? ")
stav_tachometru = int(input("Zadej stav tachometru: "))
doba_pujceni = int(input("Na kolik dní si chcete auto půjčit? "))

if user == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
    print(peugeot.vrat_auto(stav_tachometru, doba_pujceni))
elif user =="Skoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
    print(skoda.vrat_auto(stav_tachometru, doba_pujceni))
else:
    print("Daný automobil není k dispozici, můžete si půjčit pouze Peogeot a nebo Skodu")

