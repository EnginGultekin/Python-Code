# -*- coding: utf-8 -*-
# String Parçalama

s1="Python Programlama Dili"
s2="0123456789_123456789"

""" String parçalama konusu şu şekildedir

         ' [başlama indeksi : bitiş indeksi : atlama değeri] '
"""

         
print(s2[4:10]) # 4'ten başla 10.indexe kadar ama 10.indexi alma demek yani ' 456789 '
print(s2[:10])  #Başlama indexi verilmediği için baştan başla 10.index kadar ' 0123456789 '   
print(s2[7:])   #Başlama  değerini vermiş ama son değğer yok bu yüzden sona kadar gidecek ' 789_123456789 '   

print(s2[:])   # başlama ve bitiş değerleri olmadığı için baştan sona kadar hepsini yazdırır ' 0123456789_123456789 '
print(s2[:-1])  #-1. indexe kadar yaz s2[-1]=9=s2[19]  DİKKAT _ işaretinden sonraki dokuz  ' 0123456789_12345678 '

#[başlama indeksi : bitiş indeksi : atlama değeri] = [::2] baş ve son yok atlama değeri 2 

print(s2[::2])   # ikişer ikişer farkla yazar ' 02468_2468 '
print(s2[::3])   # üçer üçer farkla yazar  ' 0369258 ' 

print(s2[4:-3:2]) # 4'ten başla -3.(17.)indexe kadar ikişerli farkla yazdır ' 468_246' 

# Stringi tersten atlatarak yazdırma 

print(s2[::-1]) #Stringi sodan başa doğru bir bir arttırarak yazma ' 987654321_9876543210'
print(s2[18:6:-1])   #   ' 87654321_987 '
# print(s2[4:8:-1])  """ Bu satır çalışmaz çünkü mantıksal açıdan yanlış Python bunun yerine boş satır bırakıyor """
