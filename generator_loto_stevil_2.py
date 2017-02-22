# -*- coding: utf-8 -*-
from random import randint as nakljucna_stevilka
print("Dobrodošli v programu za generiranje Loto številk!")

lotto_stevilke = []
def ustvari_lotto_stevilke(stevilo_stevilk):
    return [nakljucna_stevilka(1,39) for i in range(stevilo_stevilk) if i not in lotto_stevilke]

def stevilo_listkov():
    return int(raw_input("Koliko listkov bi imeli?: "))

stevilo_stevilk = int(raw_input("Koliko številk bi imeli?: "))
for i in range(stevilo_listkov()):
    lotto_list = ustvari_lotto_stevilke(stevilo_stevilk)
    lotto_stevilke.append(lotto_list)

for i in lotto_stevilke:
    i.sort()
    print i

# Zakaj pri večjem številu številk, spusti skozi enaka števila (navkljub if izjavi)?