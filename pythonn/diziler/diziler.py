"""
liste=['ali',5,'a']  diziden farkl� oalrak ayn� t�rde olmak zorunda de�il

liste=['talat','�etin',2332,'baba']
liste[2]
2332
 liste[-1]
 baba

 l.index(2332) -2

 l=[1,2,3,4,5,6,7,8,9]
 l[2:] -3456789
 l[:3] -123
 l[::-1] -987654321
 l[::2]  -13579

 l.append(10) -12345678910
 l.append('a') -12345678910a
 l.insert (2,9) -2. indise 9 ekle der ekler sonra kayd�r�r-129345678910a

 len(l) -12
 l.count(9) -2 - listede ka� kere bulunur

 l1.extend(l2) l1 in �zerine l2 eklenir l1 de�isir.

 l.reverse() -l yi ders �evirir ve l nin i�ine atar

 l=[]
 topla= 0
 for i in range(0,5)
    say�=int(input('say� gir'))
    l.append(say�)
    topla+=say�
print('en k���k ve en b�y�k say�lar�n tplam�',max(l)+min(l))
print('aritmetik ortalama',topla/len(l))

kelime='ali'
l=list(kelime)
l.remove('a') -li, ilk a y� siler
l.pop(1) -1.indisi siler

l.sort() -listeyi s�ralar

l.pop(0) -kuyruk olusturmak i�in ilk indis ��kar�l�r






"""
