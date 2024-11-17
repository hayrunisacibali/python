"""
Tahmin Etme Oyunu 
inport random
sayi=random.randint(1,12)
tahmin=int(input("tahmin et:"))
skor=5
while true
    if sayi==tahmin:
    print("kazandýnýz")
    break
    else:
    print("olmadý")
    tahmin=int(input("tahmin et:"))


Taþ Kaðýt Makas Oyunu
import random
liste=["Taþ","Kaðýt","Makas"]
pc=random.choise(liste)
player=input('[TAþ-Kaðýt-Makas]').capitalize()

print("bilgisayar",pc,"seçti")
print("sen", player,"seçtin")

if pc==player:
    print("berabere")
if pc=="Kaðýt"and player=="Taþ":
    print("Kaybettin")
if pc=="taþ"and player=="Makas":
    print("Kaybettin")
if pc=="Makas"and player=="Kaðýt":
    print("Kaybettin")

if pc=="Kaðýt"and player=="Makas":
    print("Kazandýn")
if pc=="Taþ"and player=="Kaðýt":
    print("Kaazandýn")
if pc=="Makas"and player=="Taþ":
    print("Kazandýn")





"""
