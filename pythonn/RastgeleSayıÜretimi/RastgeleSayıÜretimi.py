"""
Tahmin Etme Oyunu 
inport random
sayi=random.randint(1,12)
tahmin=int(input("tahmin et:"))
skor=5
while true
    if sayi==tahmin:
    print("kazand�n�z")
    break
    else:
    print("olmad�")
    tahmin=int(input("tahmin et:"))


Ta� Ka��t Makas Oyunu
import random
liste=["Ta�","Ka��t","Makas"]
pc=random.choise(liste)
player=input('[TA�-Ka��t-Makas]').capitalize()

print("bilgisayar",pc,"se�ti")
print("sen", player,"se�tin")

if pc==player:
    print("berabere")
if pc=="Ka��t"and player=="Ta�":
    print("Kaybettin")
if pc=="ta�"and player=="Makas":
    print("Kaybettin")
if pc=="Makas"and player=="Ka��t":
    print("Kaybettin")

if pc=="Ka��t"and player=="Makas":
    print("Kazand�n")
if pc=="Ta�"and player=="Ka��t":
    print("Kaazand�n")
if pc=="Makas"and player=="Ta�":
    print("Kazand�n")





"""
