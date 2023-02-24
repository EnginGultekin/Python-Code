# Function

# Lambda Expression


"""
**lambda ifadeleri** fonksiyonlarımızı oluşturmak için Pythonda bulunan pratik
bir yöntemdir ve gerektiği yerlerde bu ifadeleri kullanabiliriz.
Biliyorsunuz listelerimizi oluşturmak için **List Comprehension**
yöntemini kullanabiliyorduk. İsterseniz **List Comprehension**
yöntemini hatırlayalım.

"""

liste1 = [1, 2, 3, 4, 5]
liste2 = list()
for i in liste1:  # Bu klasik liste oluşturma yöntemi
    liste2.append(i * 2)
print(liste2)

liste3 = [1, 2, 3, 4, 5]
liste4 = [i * 2 for i in liste3]  # List Comprehension
print(liste4)

"""
Aynı buradaki gibi bir fonksiyonu da tek satır halinde 
**lambda ifadeleriyle** oluşturabiliriz. İlk önce yapısına bakalım 
sonra örneklerimize geçelim.

     etiket = lambda parametre1,parametre2.... :  İşlem
                    
Bu yapıdan henüz bir şey anlamamış olabiliriz. İsterseniz örneklerimizle 
***lambda ifadelerini*** anlamaya çalışalım. Bir tane iki ile çarpma 
görevini yerine getiren fonksiyon yazalım.       
"""


def multipleWithTwo1(x):  # Klasik fonksiyon tanımlama
    return x * 2


print("Normal: ", multipleWithTwo1(9))

# Şimdi de bu fonksiyonu lambda ifadelerini kullanarak tek satırda yazalım.

""" x parametre x* 2 return ifadesi ve multipleWithTwo2 değeri de bir 
etikettir(değişken gibi düşünelim) """

multipleWithTwo2 = lambda x: x * 2

# Buradaki 3 argümanı lambda ifadesindeki x'in yerine geçiyor.
print("Lambda: ", multipleWithTwo2(3))

""" ----------- Example ----------- """


def add1(a, b, c):
    return a + b + c


print("Normal: ", add1(8, 54, 62))

add2 = lambda x, y, z: x + y + z
print("Lambda: ", add2(8, 54, 62))

""" ----------- Example ----------- """


# Stringi ters çevirme
def reverseString1(s):
    return s[::-1]


print(reverseString1("Lugan Han 95"))

reverseString2 = lambda s: s[::-1]
print(reverseString2("Lugan Han 95"))
