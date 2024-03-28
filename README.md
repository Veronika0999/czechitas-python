Kurz programování v Pythonu

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

