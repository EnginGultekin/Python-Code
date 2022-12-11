# -*- coding: utf-8 -*-

# 2-Listeleri Indeksleme ve Parçalama
""" Listeleri indeksleme ve parçalama stringlerle birebir olarak aynıdır.
"""
liste = [0,1,2,3,4,5,6,7,8,9,10]
print(len(liste),"\n")
print(liste[4])
print(liste[-1])
print(liste[len(liste)-1],"\n")

# <<Parçalama>>
liste = [0,1,2,3,4,5,6,7,8,9,10]
print(liste)
print(liste[4:])   # [4,5,6,7,8,9,10]
print(liste[:8])   # [0,1,2,3,4,5,6,7]
print(liste[4:8])  # [4,5,6,7]
print(liste[::2])  #Baştan sona kadar ikişer ikişer yazdırıyor. [0,2,4,6,8,10]
print(liste[::-1]) #Tersten yazdırma.                        [10,9,8,7,6,5,4,3,2,1]   
print(liste[::-3]) #Tersten üçer üçer yazdırma.   [10,7,4,1] 
