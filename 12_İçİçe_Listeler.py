# -*- coding: utf-8 -*-

""" Bir önceki kodtan kalan 
      - append metodu
      - pop metodu
      - sort metodu
       inceliyeceğiz 
"""           
# append metodu: verdiğimiz değeri listeye eklememizi sağlar. 

liste = [0,1,2,3,4]
liste.append(5)
liste.append("ENGİN")
print(liste,"\n")

# pop metodu: Bu metod, içine değer vermezsek listenin son indeksindeki elemanı, değer verirsek verdiğimiz değere karşılık   gelen indeksteki elemanı listeden atar ve attığı elemanı ekrana basar.

liste = [1,1,2,3,5,11]
liste.pop()
print(liste)

eleman1 = liste.pop(0)
eleman2 = liste.pop()
print(eleman1,eleman2)
print(liste,"\n")

# sort Metodu: sort metodu listenin elemanlarını sıralamamızı sağlar. Hemen kullanımına bakalım.

liste = [5,10,2,1,6,9,8,0,3,7,4]   
print(liste)
liste.sort()
print(liste)
liste.sort(reverse = True)  #Tersten sıralamayı sağlıyor
print(liste,"\n")

liste = ["Python","Java","PHP","C"]
print(liste)
liste.sort()
print(liste)
liste.sort(reverse = True)
print(liste,"\n")


""" Bu kodun konusu İç içe Listeler 
    Bir listenin içinde başka bir liste bulundurmak mümkündür. Bunlara Pythonda içiçe 
           listeler denmektedir. Bu tip bir özellik, Pythonda ağaç yapılarında 
                  veya matris yapılarında oldukça kullanışlı olmaktadır.
"""

# 4-İÇ İÇE Listeler: 

liste = [[1,2,3],[4,5,6],[7,8,9]]
print(liste[0])     # 1.listeyi yazdırır
print(liste[1][2])  # 2.listenin 3.elamanı '6'   

liste1 = [1,2]                 
liste2 = [3,4]                
liste3 = [5,6]

liste =[liste1,liste2,liste3]    #Bu şekildede yazılabilir 

print(liste[2])     #liste3 
print(liste[2][0])  #liste3'ün 1.elamanı

""" İç içe listeler bu şekildedir ayrıca bu konuyu iki boyutlu 
         arrayler gibi düşünebilrsiniz ama sadece mantıksal olarak 
"""












