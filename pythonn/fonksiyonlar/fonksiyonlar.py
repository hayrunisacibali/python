"""
fonksiyon= program�n islevini yerine getiren k���k kod bloklar�d�r.

def topla():
    print("iki say�n�n toplam�d�r.")
    print(5,"+",7,"=",13)

topla() -bu fonksiyonu �a��r�r�m.
toplama (5) - parametreli fonksiyon
def selamlama(isim="talat") -eger isim yaz�lmazsa default olark talat kullan�r.

def alan (u,g):
    A=u*g
    return A  - geriye deger d�ner.

def topla():
    global a   -de�i�keni global tan�mlar�z fonksiyonun d���nda da kullanbiliriz b�ylece ama ilk de�er burada verilemez.
    a = 5

def d�lar(TL):
    return(TL/18)

dolar=lambda TL: TL/18  - daha k�sa fonk yazmam�z� sa�lar.
TL=int(input("tl gir")
print(TL, "T�rk Liras�=",dolar(TL),"dolar")

"""
