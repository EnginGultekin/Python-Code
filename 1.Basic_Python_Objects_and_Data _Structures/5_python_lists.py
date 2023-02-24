# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

# Python List

# List oluşturma
list1 = [3, 9, 6, 8, 54, 'python', 85.7]
print(list)

print('Liste uzunluğu: ', len(list1))

emptyList1 = []
print(emptyList1)

emptyList2 = list()
print(emptyList2)

# Bir string " list() " fonksyonu yardımı ile listeye dönüştürülebilir
text = 'Python Programming'
listText = list(text)
print(listText)

# Liste indexleme
listIndex = [2, 65, 8, 9, 4.5, 9, 74, 5, 'python']
print('Baştaki eleman: ', listIndex[0], '  Sondaki eleman: ',
      listIndex[len(listIndex) - 1])

print('Baştan 4 e kadar: ', listIndex[:4])
print('Listeyi tersten yazdırmak için: ', listIndex[::-1])

print('-----------------------------------')

# Temel liste metodları

list1 = [1, 2, 3, 4, 5]
list2 = ['liste2', 7, 8, 9, 10]
print(list1 + list2)

list3 = [1, 2, 3, 4]
list3 = list3 + ['Murat']
print(list3)

'''
Böyle yapınca baştan 2. elemana kadar yani 1. ve 2. elaman yerine
40 ve 50 elemanlarını üstüne yazıyoruz 
'''
list3[:2] = [40, 50]
print(list3)

list4 = [1, 2, 3, 'Son']
# list4 * 3 yaptığımızda kaydedilen bir şey olmaz  !!!!!!
print(list4 * 3)

print('-----------------------------------')

# append methodu
list1 = [78, 5, 6, 2, 17]
print(list1)
list1.append(95.7)
list1.append('python')
print(list1)

# pop methodu
print('İndex vermezsek sondaki elemanı çıkarır: ', list1.pop())
print(list1)

element = list1.pop(2)
print('Listenin 2.indexi yani 3. elamanı çıkarıldı: ', element)

print('-----------------------------------')

# Sort Methodu
list1 = [45, 3, 6, 8, 9, 12, 78, 34]
list1.sort()  # Küçükten büyüğe sıralar
print(list1)

list1.sort(reverse=True)
print(list1)  # Büyükten küçüğe sıralar

list2 = ["Elma", "Armut", "Muz", "Kiraz"]
list2.sort()  # Alfabetic olarak küçükten büyüğe
print(list2)

print('-----------------------------------')

# İç içe listeler

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

dimensionalList = [list1, list2, list3]
print(dimensionalList)

# 1. Listenin 3. elemanı
print(dimensionalList[0][2])




