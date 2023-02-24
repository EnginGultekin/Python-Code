# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

# Demetler (Tuples)


# Demet elemanları parantez içine alınarak, demet oluşturulabilir
tuple1 = (1, 2, 3, 4, 5, 6, 'tuple', 5.1)
print(tuple1)
print(type(tuple1))

# Tek elemanlı demet nasıl tanımlanır
tupleOne = (1,)

# Demet elemanlarına index ile ulaşma
print(tuple1[5])
print(tuple1[-1])
print(tuple1[2:])

# Demet Temel Methodları

# " index() "  methodu girilen elemanın indexini veriyor
tupleIndex = (1, 5, 6, 7, 8, 'tuple', 'python')
print(tupleIndex.index('tuple'))
print(tupleIndex.index(5))

# " count() " methodu içerisinde bulunma sayısını veriyor
tupleCount = (1, 23, 34, 34, 2, 1, 4, 5, 1, 1, 34)
print('Count: ', tupleCount.count(1))

''' 
!!!!!!!!! Değiştirilmeme özelliği
'''
tuple1 = ("Elma", "Armut", "Muz")
# tuple1[0] = 'other'  ---> hata verecektir
# tuple.remove('Elma')    ---> hata verecektir
