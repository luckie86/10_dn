# -*- coding: utf-8 -*-
import random
def main():
    drzave_v_mesta = {
        "Slovenija": "Ljubljana",
        "Avstrija": "Dunaj",
        "Italija": "Rim",
    }
    count = 0
    while True:
        nakljucna_stevilka = random.randint(0, 2)
        nakljucna_drzava = str(drzave_v_mesta.keys()[nakljucna_stevilka])
        uganjeno_mesto = raw_input("Katero je glavno mesto drzave " + nakljucna_drzava + ": ")
        preveri(nakljucna_drzava, uganjeno_mesto, drzave_v_mesta)
        count += 1
        if count == 3:
            break

def preveri(nakljucna_drzava, uganjeno_mesto, drzave_v_mesta):
    dejansko_mesto = drzave_v_mesta[nakljucna_drzava]
    if uganjeno_mesto == dejansko_mesto:
        print("Pravilno!")
    else:
        print("Napacno")

if __name__ == '__main__':
    main()