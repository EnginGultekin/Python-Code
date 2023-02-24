# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları


# değişkenler tanımlanırken herhangi bir tip belirtmeye gerek yoktur
count = 5
result = 10

''' 
iki değişken tanımladık ve bunlar arasındaki değerleri kısa bir yolla
karşılıklı değiştirebiliriz .
'''

print('Count :', count)
print('Result :', result)

count, result = result, count

print('Count :', count)
print('Result :', result)

'''
Python da "4/2" işlemi yaptığımızda sonuç "2" değilde "2.0" 
float bir değer dönüyorancak biz bunu istemiyoruz ve tam sayı sonucu 
vermesi için " // " bölme işlemi için bu operotörü kullanmaktayız .
'''

print('Float: ', 4 / 2)
print('Tam Sayı: ', 4 // 2)

# Üst bulma  " 4 ** 3 " şeklindedir
print(4 ** 3)

# Kök bulma " 64 ** 0.5 " şeklindedir
print(64 ** 0.5)
print(64 ** (1/6))

