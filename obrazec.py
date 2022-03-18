"""
Úloha 3 - obrazec
Úkolem je pomocí jednoho příkazu print vytisknout obrazec, který je danný vstupem uživatele. Obrazec se skládá z textu, který je
tvořen znakem * a #
Načti od uživatele 3 čísla: 
    - 1. číslo je počet řádek obrazce
    - 2. číslo je šířka obrazce
    - 3. číslo je počet hvězdiček na řádku (a zbytek jsou #), nejdřív jsou vždy * pak až #
(Pozor, počet hvězdiček logicky nesmí být větší, než šířka řádku... tak pozor až budete zadávat čísla)

Např: pro čísla 5 (počet řádků), 10 (šířka) a 2 (počet hvězd) by se mělo ukázat toto:

**########
**########
**########
**########
**########
"""

radku = int(input())
sirka = int(input())
hvezdicek = int(input())

print(radku * (hvezdicek*"*"+(sirka-hvezdicek)*"#"+"\n"))
