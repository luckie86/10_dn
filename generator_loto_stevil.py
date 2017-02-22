# -*- coding: utf-8 -*-
import random
print("Dobrodošli v programu za generiranje Loto številk!")
def main():
    stevilo_stevilk = int(raw_input("Prosimo vnesite koliko naključnih števil bi želei imeti: "))
    stevilke = []
    while True:
        if len(stevilke) == stevilo_stevilk:
            break
        nakljucna_stevilka = random.randint(1, 39)
        if nakljucna_stevilka not in stevilke:
            stevilke.append(nakljucna_stevilka)
            stevilke.sort()
    print stevilke
    print("Lep pozdrav!")

if __name__ == '__main__':
    main()