import json

with open ('body.json', encoding = 'utf-8') as file:
    body = json.load(file)

novy_slovnik = {}

for jmeno, hodnoceni in body.items():
    if hodnoceni > 60:
        novy_slovnik[jmeno] = 'Pass'        
    else:
        novy_slovnik[jmeno] = 'Fail'


with open('prospech.json', mode = 'w', encoding='utf-8') as file:
    json.dump(novy_slovnik, file)


#Nepovinný bonus
with open('bonusy.json', encoding = 'utf-8') as file:
    bonusy = json.load(file)

znamka = {}

from collections import Counter
slouceni = (Counter(body)) + Counter(bonusy)


for jmeno, hodnoceni in slouceni.items():
    if hodnoceni >= 90:
        znamka[jmeno] = 1
    elif hodnoceni >= 70 <= 89:
        znamka[jmeno] = 2
    elif hodnoceni >= 50 <= 69:
        znamka[jmeno] = 3
    elif hodnoceni >=30 <= 49:
        znamka[jmeno] = 4
    else:
        znamka[jmeno] = 5


with open('znamky.json', mode = 'w', encoding='utf-8') as file:
    json.dump(znamka, file)