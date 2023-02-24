# -*- coding: utf-8 -*-

""" Bu kod içerisinde aşağıdaki maddeleri göreceğiz
   - Liste Oluşturma
   - Indeksleme ve Parçalama
   - Temel Liste Metodları
   - İç içe listeler
"""
# 1-Liste Oluşturma:  Listeler bir [] köşeli parantez içine veriler veya değerler konarak oluşturulabilir.

liste = ["Elma",5,"Muz",5.8,123]  #Listelerin içine istediğimiz type ta veri yazabiliriz
print(liste,"\n") 

boş_liste = list()      #list fonksyonu liste oluşturmamızı sağlıyor
print(boş_liste,"\n")

liste2 = [1,2,3,4,5,6,7,8,9]
print(len(liste2),"\n")            #len() fonksyonunu listeler içinde kullanabiliriz : 'Uzunluk'


s= "ENGİN_GÜLTEKİN"
liste = list(s)
print(liste,"\n")


""" Buraya kadar sadece Liste oluşturmayı ve list() fonksyonunu kullanmayı
      öğrendik bu konunun devamı 10,11 ve 12.kodun içinde olacak iyi çalışmalar
"""        
