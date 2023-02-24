# Loops

"""
--- Problem 1 ---
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya
"mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

"""

num = int(input("Lütfen bir sayı giriniz: "))
perfectNum = 0

for m in range(1, num):
    if num % m == 0:
        perfectNum += m

if perfectNum == num:
    print("{} sayısı mükemmel sayıdır".format(num))
else:
    print("{} sayısı mükemmel sayı değildir".format(num))

"""
--- Problem 2 ---
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı 
olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 
4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya 
eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4 

"""

num = input("Lütfen bir sayı giriniz: ")
digitLength = len(num)
num = int(num)
tempNum = num
digit = 0
armstrongNum = 0

while tempNum > 0:
    digit = tempNum % 10
    armstrongNum += digit ** digitLength
    # float olmasın, tam sayı olsun diye  //  kullanıldı
    tempNum //= 10

if armstrongNum == num:
    print("{} sayısı Armstrong sayıdır".format(num))
else:
    print("{} sayısı Armstrong sayı değildir".format(num))

"""
--- Problem 3 ---
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

*İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() 
fonksiyonunu kullanarak elde edin.*
"""

for i in range(1, 11):
    print("******************")
    for j in range(1, 11):
        print("{} x {} = {}".format(i, j, i * j))

print("******************\n")
"""
--- Problem 4 ---
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği 
sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı 
zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa 
döngüyü break ile sonlandırın.*
"""

result = 0

while True:
    num = input("Sayı:")

    if num == "q":
        break
    num = int(num)
    result += num

print("Girdiğiniz Sayıların Toplamı:", result)

"""
--- Problem 5 --- 
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. 
Bu işlemi *continue* ile yapmaya çalışın.

"""

for i in range(1, 101):

    if i % 3 != 0:
        continue
    print(i)

"""
--- Problem 6 --- 
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık 
yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan 
sadece çift sayıları bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme 
yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma 
yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

"""

list1 = [i for i in range(1, 101) if i % 2 == 0]
print(list1)