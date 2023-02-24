# Loops


"""
--- in ---  operatörü, bir elamanın başka bir listede, demette  veya stringte
bulunup bulunmadığını kontrol eder.
"""

# a karakteri Hallo içinde var o yüzden true
print("a" in "Hallo")
print("t" in "Hallo")  # Karakter

print('List: ', 4 in [1, 2, 3, 4])  # liste
print('Tuple: ', 4 in (1, 2, 3))  # tuple (demet)

# for-loop

'''
For döngüsü, listelerin, demetlerin ve hatta sözlüklerin üzerinde
dolaşmamızı sağlar

    for item in veri_yapısı(liste,demet vs)
'''

# Listede gezinmek

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
result = 0

for item in list1:
    print("item: ", item)
    result += item
print('İtem Result: ', result)
print("\n-----------------------")

# Karakter dizileri üzerinde gezinmek
s = "Python"
for character in s:
    print(character)
print("\n-----------------------")

# Demetler üzerinde gezinmek
tuple1 = (1, 2, 3, 4, 5, 6)
for tup in tuple1:
    print(tup)
print("\n-----------------------")

# Listelerin için 2 boyutlu demetler
liste = [(1, 2), (3, 4), (5, 6), (7, 8)]

for eleman in liste:
    print(eleman)  # Herbir elemanın  demet olduğu görebiliyoruz.

# Demet içindeki herbir elemanı almak için pratik yöntem
for (i, j) in liste:
    print(i, ' - ', j)

# Demet içindeki elemanları çarpalım.
liste = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for (i, j, k) in liste:
    print(i * j * k)

print("\n-----------------------")

# Sözlükler üzerinde gezinmek (Dictionary)

dict1 = {"one": 1, "two": 2, "three": 3}

print(dict1.keys())
print(dict1.values())
print(dict1.items())
print("\n-----------------------")

# Metodları kullanmadan sözlük üzerinde gezinmek Sadece keyleri alabiliyoruz.
for item in dict1:
    print(item)

for item in dict1.keys():
    print("Key: ", item)

for item in dict1.values():
    print("Value: ", item)

for (i, j) in dict1.items():
    print("key: ", i, "- value: ", j)
