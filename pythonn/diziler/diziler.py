"""
liste=['ali',5,'a']  diziden farklı oalrak aynı türde olmak zorunda değil

liste=['talat','çetin',2332,'baba']
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
 l.insert (2,9) -2. indise 9 ekle der ekler sonra kaydırır-129345678910a

 len(l) -12
 l.count(9) -2 - listede kaç kere bulunur

 l1.extend(l2) l1 in üzerine l2 eklenir l1 değisir.

 l.reverse() -l yi ders çevirir ve l nin içine atar

 l=[]
 topla= 0
 for i in range(0,5)
    sayı=int(input('sayı gir'))
    l.append(sayı)
    topla+=sayı
print('en küçük ve en büyük sayıların tplamı',max(l)+min(l))
print('aritmetik ortalama',topla/len(l))

kelime='ali'
l=list(kelime)
l.remove('a') -li, ilk a yı siler
l.pop(1) -1.indisi siler

l.sort() -listeyi sıralar

l.pop(0) -kuyruk olusturmak için ilk indis çıkarılır






"""
