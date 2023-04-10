#Povinný domácí úkol č.2:

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadej kód součástky: ")
mnozstvi = int(input("Zadej požadované množství: "))

if kod_soucastky not in sklad:
    print(f"Požadovaná součástka {kod_soucastky} není skladem")
elif kod_soucastky in sklad:
    if sklad[kod_soucastky] < mnozstvi:
        print(f"Požadovaná součástka {kod_soucastky} je skladem, ale v omezeném množství {mnozstvi} kusů.")
        sklad.pop(kod_soucastky)
    else:
        print(f"Požadovaná součástka {kod_soucastky} je dostupná v požadovaném množství.")
        sklad[kod_soucastky] -= mnozstvi
        print(sklad)

#Nepovinný bonus 1 (pouze kód)
user = input("Jaký kod  chceš převest? ")
for kod in user:
    print(morse_code[kod], end=" ")

#Nepovinný bonus 2 (pouze kód)
user = input("Zadej region, který tě zajímá: ")

for stat in staty:
    if stat["region"] == user:
        print(stat["name"])

if stat["region"] != user:
    print("Neznámý region")