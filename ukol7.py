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
       
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

user = input("Jakou značku auta si přejete (Skoda nebo Peugeot)? ")

if user == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
elif user =="Skoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
else:
    print("Daný automobil není k dispozici, můžete si půjčit pouze Peogeot a nebo Skodu")

