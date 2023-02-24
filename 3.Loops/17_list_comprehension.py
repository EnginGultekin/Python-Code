# Loops

# List Comprehension

# Listelerdeki " append " metodunu hatırlayalım.
list1 = [1, 2, 3, 4]
print(list1)
list1.append(5)
print(list1)
print("-------------------")

# list1'den list2'yi oluşturalım.
list1 = [1, 2, 3, 4, 5]
list2 = list()  # veya list2 = [] ikisi de boş liste oluşturur.
for i in list1:
    # list2 'ye liste1 in elemanları for döngüsü yardımıyla atıyoruz.
    list2.append(i)
print("1. ", list2)

"""Acaba bu kodumuzu list comprehension ile daha kısa yazabilir miyiz ?"""

list1 = [1, 2, 3, 4, 5]
""" List Comprehension """
list2 = [i for i in list1]
print("2. ", list2)

""" List Comprehension """
list2 = [i * 2 for i in list1]
print("3. ", list2)

""" List Comprehension """
list1 = [(1, 2), (3, 4), (5, 6)]
list2 = [i * j for (i, j) in list1]
print("4. ", list2)

list1 = list(range(1, 11))
""" List Comprehension """
list2 = [i for i in list1 if not (i == 2 or i == 4 or i == 9)]
print("5. ", list2)

s = "Python"
# List Comprehension
list1 = [i * 3 for i in s]
print(list1)
print("\n---*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*---\n")

#
#
#
#    !!!!!! Complex example
#
#
#

"""
Peki iç içe listeleri tek bir liste haline list comprehension ile nasıl 
getirebiliriz ? 
İlk önce normal yolumuzu görelim.
"""

list1 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
# yeni_liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

list2 = list()
for i in list1:
    # Buradaki i değeri de aslında bir liste.
    print(i)

for i in list1:
    for x in i:
        # print("x:", x)
        list2.append(x)
print(list2)

print("\n---*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*---\n")

# List Comprehension
liste2 = [c for i in list1 for c in i]
print(list2)

liste2 = [c for i in list1 for c in i]
