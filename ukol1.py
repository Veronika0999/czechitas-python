#Domácí úkol - 1.úkol:

jmeno = "Verca"
print(f"{jmeno}@czechitas.cz")


jmeno = input("Zadej své jméno: ")
if jmeno =="Verca":
    print(f"{jmeno}@czechitas.cz")
else:
    print("Špatně, zkus to znovu.")


#Nepovinný bonus:

jmeno_a_prijmeni = input("Jak se jmenuješ? ")

print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(jmeno_a_prijmeni.title())

#inicialy - nedá se to udělat i nějak snadněji - bez toho, aniž bych se musela ptát zvlášť na jméno a příjmení? nějak pouze s proměnnou "jmeno_a_prijmeni"? :)
jmeno = input("Vlož své křesní jméno: ")
prijmeni = input("Vlož své příjmení: ")
inicialy = (jmeno[0] +"." + prijmeni[0]+".")
print(inicialy.upper())

if len(jmeno) <= 5:
    inicialy = (jmeno[0] +"." + prijmeni[0]+".")
    print(inicialy.upper())
else:
    print(jmeno + " "+ prijmeni)
