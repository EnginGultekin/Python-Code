# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

# Karakter dizileri (stringler)

# String tanımlaması ve indexlemeye bakalım
deneme = '0123456789_Python_Deneme'

print('0. Eleman: ', deneme[0])

print('-1. Eleman Yani En Son: ', deneme[-1])

print('-2. Eleman Yani Sondan 2.: ', deneme[-2])

print('---------------------------------------------')

'''
 Belirli indexleri yazdırmak istersek
 [başlama indexi : bitiş indexi : atlama değeri]
 Bu arada DİKKAT !!! Belirtilen son index dahil değildir
'''

print("4'ten 10'a kadar :", deneme[4:10])

print("en baştan 10'a kadar :", deneme[:10])

print("4'ten sona kadar :", deneme[4:])

print("tüm string :", deneme[:])

print("baştan başla 2 şer 2 şer atlayarak git :", deneme[::2])

# Stringi tam tersine çevirmenin yolu
print('Stringi tersine çevir : ', deneme[::-1])

print('---------------------------------------------')

# String uzunluğu hesaplama " len() " fonksyonu ile hesaplanır
print('String uzunluğu : ', len(deneme))

'''
Stringlerde karakter karakter değişiklik yapılmasına izin verilmez
Ancak stringin tamamını değiştirmemize izin vermektedir

        Hatalıdır !!!!!!!!!
        deneme[0] = 'D'
'''

deneme = 'Python_İzin_Verdi_Değişti'
print(deneme)

print('---------------------------------------------')


# Stringleri toplayabiliriz ve çarpabiliriz

a = '1.Yazı'
b = '2.Yazı'
c = '3.Yazı'

print(a+b+c)

print(a*3)





















