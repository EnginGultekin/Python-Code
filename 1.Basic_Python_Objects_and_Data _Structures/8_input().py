# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

# input() fonksyonu

"""
input()  # Çalıtırdığımız zaman input fonksiyonu bizden bir girdi bekler.
"""

number = input('Lütfen bir sayı giriniz: ')
print('Girmiş olduğunuz sayı: ', number)

# Kullanıcının girdiği değer bize string olarak döner
typeStr = input('Lütfen bir sayı giriniz: ')
print('Girmiş olduğunuz inputun tipi: ', type(typeStr))

"""
Girien değerler string olarak dönmektedir ancak bir başka 
bir tipte kullanmak istersek örnekteki gibi yapabiliriz 
"""

convert = int(input('Lütfen bir sayı giriniz: '))
print('girilen sayının 5 katı = ', convert * 5)

# Eğer kullanıcılar sayı değilde karakter girerse ne olacak ?

# onu daha ilerde görecez














