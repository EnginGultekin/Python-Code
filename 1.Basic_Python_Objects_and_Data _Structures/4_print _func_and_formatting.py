# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları


# Print Fonksyonu ve Formatlama  " https://pyformat.info "

# type() fonksyonu
number = 5
field = 25.9
text = 'Python'
print(type(number), '\t', type(field), '\t', type(text))

#
# Print fonksyonunun özellikleri
#

''' 
1.si " sep " parametresi
print içinde yazdırılacak olan elemanlar arasında
istediğimiz şeyi yazdırmamıza yardımcı olmaktadır.   
'''

print(1, 2, 3, 4, 5, 'text', 3.8, sep=" - ")
print("06", "04", "2015", sep="/")

'''
2.si " * " 
eğer bir stringin başına bu işareti koyarsak her bir karakteri ayırır
ve hepsine bir string gibi davranmaya yarıyor
'''

print(*"Python")
print(*"Python", sep="-")
print(*"TBMM", sep=".")

#
# Formatlama " format() " fonksyonu
#

'''
örnek üzerinden anlatmak gerekirse 
süslü parantezler ve fromat fonksyonu kullanarak 
aşağıdaki gibi sırayla ya da index belirterek istenilen
değişkeni süslü paranteze atar gibi işlem yapabiliriz 
'''
print('{} {} {}'.format(3.8787, 5.8754, 9.4545))

num1 = 74
num2 = 87
print("{} + {} 'nın toplamı {}'dır".format(num1, num2, num1 + num2))

'''
Süslü parantezlerin içindeki kullanım ondalıklı kısmın 
 sadece 2 basamağına kadar almak istediğimiz söylüyor.
'''

# 645.8 98 python çıktısını almalıyız
print("{2} {0} {1}".format(98, 'Python', 645.8))

# ondalıklı kısmın sadece 2 basamağına kadar almakta
print("{:.2f} - {:.1f} - {:.3f}".format(3.1463, 5.324, 7.324324))
