# -*- coding: utf-8 -*-
import random
print("Dobrodošli v igri ugani skrito številko!")
def main():
    skrita_stevilka = random.randint(1, 100)
    ugibana_stevilka = int(raw_input("Prosimo vnesite število med 1 in 100: "))
    while skrita_stevilka != ugibana_stevilka:
        ugibana_stevilka = int(raw_input("Prosimo vnesite 5€ in poizkusite ponovno: "))
    else:
        print("Čestitamo, zadeli ste 1000 €!")

if __name__ == '__main__':
    main()