# Kurz programování v Pythonu

# ukol-01

Hlavním cílem úkolu z první lekce je vyzkoušet si systém odevzdávání (viz [návod](../ODEVZDAVANI-UKOLU.md)). Pokud do příští lekce
nevyřešíš úlohu, odevzdej alespoň testovací soubor, abychom věděli, že víš jak na to.

V případě dotazů vždy můžeš kontaktovat kouče ve Slackovém kanálu tvé skupinky.

---

## Zadání:

Napiš program, který bude obsahovat jednu proměnnou `jmeno`. Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje).
Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou `czechitas.cz` a tuto e-mailovou adresu vypíše.

Tedy pokud bude hodnota proměnné `jmeno` například `Jindřiška`, pak program vypíše `Jindřiška@czechitas.cz`.

--- 

## Nepovinný bonus:

*Tuto část můžeš řešit, pokud už máš první část úkolu hotovou a chceš si ještě něco procvičit.*

Napiš program, který bude obsahovat proměnnou `jmeno_a_prijmeni`. Obsah proměnné načti od uživatele pomocí funkce `input`. 
Tvůj program postupně vypíše několik způsobů formátování jména:
* všechna písmena velká (vypíše např. `JANA MALÁ`)
* všechna písmena malá (vypíše např. `jana malá`)
* standardní varianta - první písmeno velké, další malá (vypíše např. `Jana Malá`)
* iniciály (vypíše např. `J. M.`)
* křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá
(u vstupu `Jarmila Malá` by došlo ke zkrácení křestního jména, zatímco u vstupu `Jana Malá` nikoliv)

Zaexperimentuj s různými vstupy od uživatele (co třeba `JaNA maLá`?).

# ukol-02

## Zadání

Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace
o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je
počet součástek na skladě.

```python
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
```

Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník.
Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník
chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:

* Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
* Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
* Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

---

## Nepovinný bonus 1
Ve slovníku [zde](./morseovka.py) najdeš Morseovu abecedu, kde jako klíč slouží znak v klasické abecedě a jako hodnota zápis znaku v Morseově abecedě.

1. Napiš program, který se uživatele zeptá na text, který chce zapsat v Morseově abecedě. Uvažuj disciplinovaného uživatele, který zadává pouze znaky bez diakritiky, malá písmena atd. Na začátku uvažuj i to, že uživatel nezadává mezery.
1. Projdi řetězec zadaný uživatelem. Najdi každý znak ve slovníku a vypiš ho na obrazovku v Morseově abecedě.
1. Abychom měli celý kód vypsaný na jedné řádce, požádáme funkci `print()`, aby na konci výpisu nevkládala znak pro konec řádku, ale mezeru. To uděláme tak, že jako druhý argument funkce dáme argument `end=" "`.
1. Nyní přidáme mezery. Uvažuj, že uživatel může zadat mezeru. Před tím, než budeš hledat znak ve slovníku, zkontroluj, zda znak není mezera. Pokud ano, vypiš znak lomítka `/`.

---

## Nepovinný bonus 2
Ve slovníku [zde](./staty.py) najdeš seznam slovníků s informacemi o státech světa. O každém státu tam vidíš následující
informace:

* název státu (`name`),
* hlavní město (`capital`),
* region (`region`),
* subregion (`subregion`),
* populace (`population`),
* rozloha (`area`),
* Giniho koeficient (`gini`).

Vytvoř program, který se uživatele zeptá na region, který ho zajímá. Následně projdi seznam a vypiš všechny státy, které leží v regionu. Pokud program žádný stát pro daný region nenajde, vypiš text `"Neznámý region"`.

_V tomto bonusu využiješ znalosti z bonusové kapitoly [Slovníky a cykly: dvourozměrné tabulky v Pythonu](https://kodim.cz/kurzy/uvod-do-progr-2/uvod-do-programovani-2/slovniky/dvourozmerne-tabulky)_

# ukol-03

_V tomto úkolu využiješ znalosti z kapitoly [Slovníky a cykly](https://kodim.cz/kurzy/uvod-do-progr-2/uvod-do-programovani-2/slovniky/slovniky-a-cykly)_

---

## Zadání

Soubor [body.json](./body.json) je JSON, který obsahuje informace o získaných bodech z písemky.

* Soubor si ulož a načti do slovníku.

* Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec `"Pass"`, pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude `"Fail"`.

* Výsledný slovník ulož jako JSON do souboru `prospech.json`.

---

## Nepovinný bonus

Krom souboru s body si ulož a načti do druhého slovníku ještě soubor [bonusy.json](./bonusy.json). Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.

Tvým úkolem je žákům přiřadit známky na základě *součtu* bodů z písemky a bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:

```
1: 90 a více
2: 70-89
3: 50-69
4: 30-49
5: 29 a méně
```

* Výsledný slovník ulož jako JSON do souboru `znamky.json`.

# ukol-04

## Zadání

Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

1. Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
1. Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

Tvůj program bude obsahovat dvě funkce:
1. První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu `True`, jinak vrátí hodnotu `False`.
1. Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné,
vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou
vypíše uživateli.

Tipy: 
* Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme
v kurzu zatím neřešili.
* Pro kontrolu předvolby použijte _slicing_ (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem `"+420"`.

---

## Nepovinný bonus 1

Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš například tak, že použiješ metodu `.replace()`.
První parametr metody `replace` je znak, který chceš nahradit, a druhý parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem `""`.

* Odkaz na dokumentaci metody `replace`: https://docs.python.org/3/library/stdtypes.html#str.replace

---

## Nepovinný bonus 2
Přidej svým funkcím _typování_, aby bylo jasné, jaký typy mají parametry tvých funkcí a jaká je návratová hodnota tvých funkcí.

_K typování se dostaneme až v 5. lekci. Pokud chceš, můžeš úlohu řešit předem pomocí [Čtení na doma](https://kodim.cz/kurzy/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/cteni-na-doma)_

# ukol-05

## Zadání

Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

```py
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
```

1. Vytvoř seznam průměrných teplot pro každý den.
1. Vytvoř seznam ranních teplot.
1. Vytvoř seznam nočních teplot.
1. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

---

## Nepovinný bonus

Krom teplot máme k dispozici i informaci o dnu v týdnu:

```py
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]
```

Pomocí _dict comprehension_ vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.

```
{den: průměrná teplota}
```

_Dict comprehension_ si ukážeme až v 6. lekci, ale princip je velice podobný _list comprehension_. Tady je příklad využit - vytvoříme nový slovník, který nebude body znázorňovat jako celá čísla, ale jako procenta:

```py
hodnoceni = {"Marie": 62, "Magdalena": 74, "Monika": 93, "Marek": 80}

procenta = {zak: f"{body}%" for zak, body in hodnoceni.items()}
# procenta = {zak: str(body) + "%" for zak, body in hodnoceni.items()}

# nebo

procenta = {zak: f"{hodnoceni[zak]}%" for zak in hodnoceni}
# procenta = {zak: str(hodnoceni[zak]) + "%" for zak in hodnoceni}

print(procenta)  # {'Marie': '62%', 'Magdalena': '74%', 'Monika': '93%', 'Marek': '80%'}
```

# ukol-06

## Zadání

1. Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:

* platná data:
```
2.2.2022
13. 8. 1999
4/5/2001
```

* neplatná data:
```
5.123.458.91
21.4
8./9
```

2. Zkopíruj si obsah souboru [posta.txt](posta.txt) do regex101 jako testovací řetězec. Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu. Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například `190 16 PRAHA 916` nebo `742 45 FULNEK`. Celkem by jich mělo být 18.

---

## Nepovinný bonus

Napiš program, který se zeptá uživatele na jeho přihlašovací jméno, e-mailovou adresu a heslo. Po každém zadaném údaji program ověří jeho správnost podle následujících pravidel:

* uživatelské jméno smí obsahovat malá a velká písmena (nesmí obsahovat žádné jiné znaky), jeho minimálná délka je 6 znaků a jeho maximální délka je 10 znaků.
* heslo smí obsahovat malá a velká písmena, číslice, a následující speciální znaky: `_`, `-`, `.`, `+`, `=`. Jeho minimálná délka je 12 znaků a jeho maximální délka je 30 znaků.
* e-mail by měl být validním e-mailem :slightly_smiling_face: Tady jsou nějaké testovací příklady (viz [zdroj](https://gist.github.com/cjaoude/fd9910626629b53c4d25))
  * příklady platných e-mailových adres:
    ```
    email@example.com
    firstname.lastname@example.com
    email@subdomain.example.com
    firstname+lastname@example.com
    email@123.123.123.123
    email@[123.123.123.123]
    "email"@example.com
    1234567890@example.com
    email@example-one.com
    _______@example.com
    email@example.name
    email@example.museum
    email@example.co.jp
    firstname-lastname@example.com
    ```
  * příklady neplatných e-mailových adres:
    ```
    plainaddress
    #@%^%#$@#$@#.com
    @example.com
    Joe Smith <email@example.com>
    email.example.com
    email@example@example.com
    .email@example.com
    email.@example.com
    email..email@example.com
    あいうえお@example.com
    email@example.com (Joe Smith)
    email@example
    email@-example.com
    email@example.web
    email@111.222.333.44444
    email@example..com
    Abc..123@example.com
    ```

  *Zkuste se zaměřit na to, aby program pokryl co nejvíce platných e-mailových adres. Cílem není pokrýt všechny platné, a vyloučit všechny neplatné, ale zkusit si napsat regex, který to zvládne co nejlépe, i když třeba ne perfektně! Bonus odevzdej, i když nebude dokonalý.*


  # ukol-07: Evidence aut

Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

| Registrační značka | Značka a typ vozidla | Počet najetých kilometrů |
| ------------------ | -------------------- | ------------------------ |
| 4A2 3020           | Peugeot 403 Cabrio   | 47534                    |
| 1P3 4747           | Škoda Octavia        | 41253                    |

Vytvoř třídu `Auto`, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

- registrační značka automobilu `registracni_znacka`,
- značka a typ vozidla `typ_vozidla`,
- počet najetých kilometrů `najete_km`,
- informaci o tom, jestli je vozidlo aktuálně volné `dostupne` (pravdivostní hodnota -- `True` pokud je volné a `False` pokud je vypůjčené).

Vytvoř metodu `__init__()` pro třídu `Auto`. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce `__init__` a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako `True`, tj. na začátku je vozidlo vždy volné.

Vytvoř objekty, které reprezentují oba automobily půjčovny.

Třídě `Auto` přidej metodu `pujc_auto()`, která nebude mít (kromě obligátního `self`) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu `dostupne`, který určuje, zda je vozidlo půjčené, a vrátí text `"Potvrzuji zapůjčení vozidla"`. Pokud je vozidlo již půjčené, vrátí text `"Vozidlo není k dispozici"`.

Dále tříde `Auto` přidej funkci `get_info()`, která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty `Peugeot` nebo `Škoda`. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce `get_info()` a následně použij funkci `pujc_auto()`.

Otestuj, že program nedovolí půjčit stejné auto dvakrát.

---

## Nepovinný bonus

Přidej třídě `Auto` metodu `vrat_auto()`, která bude mít (krom obligátního `self`) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova `return`.

# ukol-08: Adopce zvířat

_Úkol můžeš odevzdat buďto jako Jupyter Notebook `.ipynb`, nebo jako klasický program `.py`._

Stáhni si [dataset](https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/adopce-zvirat.csv), který obsahuje seznam zvířat k adopci v ZOO Praha. Zdroj dat je [Národní katalog otevřených dat](https://data.gov.cz/).

* Data si načti pomocí metody `pandas.read_csv()`. Pozor, nastav oddělovač na znak středníku. Využij parametr `sep`.

* Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?

* Které zvíře se nachází na záznamu s indexem 34? Vypiš název tohoto zvířete v češtině a v angličtině.

---

## Nepovinný bonus

Využij metody [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html) (a libovolných dalších metod), ke zjištění následujících informací:
* Adopce kterých zvířat je nejdražší?
* Které zvíře je alfabeticky poslední v češtině? Které v angličtině?

Bonus můžeš doplnit o nějaké vlastní pozorování.


# ukol-09: Teplota ve městech

_Úkol můžeš odevzdat buďto jako Jupyter Notebook `.ipynb`, nebo jako klasický program `.py`._

Stáhni si soubor [temperature.csv](./temperature.csv), který obsahuje informace o průměrné teplotě v různých městech v **listopadu 2017**.


Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. 

Dále napiš následující dotazy:
* Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? [Zde](https://cs.wikipedia.org/wiki/Stupe%C5%88_Fahrenheita) je nápověda.
* Dotaz na měření, ve kterých je teplota (sloupec `AvgTemperature`) vyšší než 80 stupňů.
* Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec `Region`) Evropa (Europe).
* Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než -20 stupňů.

---

## Nepovinný bonus 1

Nainstaluj si modul `pytemperature` a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia.

Ve svém programu nejprve proveď import modulu `pytemperature`. Nový sloupec pak přidáš do tabulky tak, že nalevo od `=` vložíš tabulku a název nového sloupce do hranatých závorek. Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci `f2c` z modulu `pytemperature`, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.

```python
import pytemperature

df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
```

Nyní můžeš zpracovat následující příklady:

* Dotaz na měření, ve kterých je teplota (sloupec `AvgTemperatureCelsia`) vyšší než 30 stupňů Celsia.
* Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec `Region`) Evropa (Europe).
* Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé?

---

## Nepovinný bonus 2

Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracoval/a první bonus, můžeš pracovat s teplotami ve stupních Celsia.

Napiš následující dotazy:

* Dotaz na řádky z 13. listopadu 2017 (sloupec `Day` musí mít hodnotu 13).
* Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec `Day` musí mít hodnotu 13 a sloupec `Country` hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
* Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec `City`) Washington a Philadelphia.


# ukol-10: Zaměstnanci a Projekty

_Úkol můžeš odevzdat buďto jako Jupyter Notebook `.ipynb`, nebo jako klasický program `.py`._

## Zadání 1

Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci. Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech [zam_praha.csv](https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv), [zam_plzeň.csv](https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv) a [zam_liberec.csv](https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv).

* Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec `mesto`, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
* Vytvoř novou tabulku `zamestnanci` a ulož do ní informace o všech zaměstnancích (operace `concat`).
* Ze souboru [platy_2021_02.csv](https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv) načti platy zaměstnanců za únor 2021. Propoj tabulku (operace `join`) s platy a tabulku se zaměstnanci pomocí sloupce `cislo_zamestnance`.
* Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
* Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.

## Zadání 2
Pokračuj ve své práci pro softwarovou firmu. Ze souboru [vykazy.csv](https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/vykazy.csv) načti informace o výkazech na projekty pro jednoho vybraného zákazníka.

* Načti data ze souboru a ulož je do tabulky.
* Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.

---

## Nepovinný bonus 1

* Ulož do proměnné počet zaměstnanců, kteří v naší firmě již nepracují.
* V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.

---

## Nepovinný bonus 2

Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení. 

Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.


# ukol-11

_Úkol můžeš odevzdat buďto jako Jupyter Notebook `.ipynb`, nebo jako klasický program `.py`._

## Zadání

Stáhni si soubor [platy_2021_02.csv](https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv) s informacemi o platech v softwarové firmě (stejný soubor, jako v předchozím úkolu).

Načti si tato data do tabulky a vytvoř histogram. Nastav vhodně hranice skupin histogramu (parametr `bins`), aby byl graf přehledný a snadno interpretovatelný.

---

## Nepovinný bonus 1

Vrať se k práci se souborem [temperature.csv](./temperature.csv), který obsahuje informace o průměrné teplotě v různých městech v **listopadu 2017**.

* Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
* Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.




