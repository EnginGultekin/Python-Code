# Conditional States

"""
--- Problem 1 ---
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini
hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)
BKİ 18.5'un altındaysa -------> Zayıf
BKİ 18.5 ile 25 arasındaysa ------> Normal
BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
BKİ 30'un üstündeyse -------------> Obez
"""
print("--- Boy Kilo Endexi ---")

height = float(input("Boyunuzu Giriniz:"))
weight = int(input("Kilonuzu Giriniz:"))

bki = height / (weight ** 2)

if bki < 18.5:
    print("Zayıf")
elif 18.5 <= bki < 25:
    print("Normal")
elif 25 <= bki < 30:
    print("Fazla Kilolu")
else:
    print("Obez")

"""
--- Problem 2 ---
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
print("\n--- Maximum Number ---")
num1 = int(input("Number1:"))

num2 = int(input("Number2:"))

num3 = int(input("Number3:"))

if num1 >= num2 and num1 >= num3:
    print("En büyük sayı:", num1)
elif num2 >= num1 and num2 >= num3:
    print("En büyük sayı:", num2)
elif num3 >= num1 and num3 >= num2:
    print("En büyük sayı:", num3)

"""
--- Problem 3 --- 
Kullanıcının girdiği vize1,vize2,final notlarına 
notlarına göre harf notunu hesaplayın.

Vize1 toplam notun %30'una etki edecek.
Vize2 toplam notun %30'una etki edecek.
Final toplam notun %40'ına etki edecek.

Toplam Not >=  90 -----> AA
Toplam Not >=  85 -----> BA
Toplam Not >=  80 -----> BB
Toplam Not >=  75 -----> CB
Toplam Not >=  70 -----> CC
Toplam Not >=  65 -----> DC
Toplam Not >=  60 -----> DD
Toplam Not >=  55 -----> FD
Toplam Not <  55 -----> FF
"""
print("\n--- Ortalama Hesaplama ---")

exam1 = int(input("Vize1:"))
exam2 = int(input("Vize2:"))
finalExam = int(input("Final:"))

average = exam1 * 3 / 10 + exam2 * 3 / 10 + finalExam * 4 / 10

if average >= 90:
    print("AA")
elif average >= 85:
    print("BA")
elif average >= 80:
    print("BB")
elif average >= 75:
    print("CB")
elif average >= 70:
    print("CC")
elif average >= 65:
    print("DC")
elif average >= 60:
    print("DD")
elif average >= 55:
    print("FD")
else:
    print("FF")

"""
--- Problem 4 --- 
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan 
üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin 
kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin 
ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. 
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana 
"Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. 
Bunun için, Pythonda hazır bir fonksiyon olan 
abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

input: abs(-4) abs(5)
output:   4      5
"""

shape = input("\nHangi şeklin tipini öğrenmek istiyorsunuz? ")

if shape == "Dörtgen":
    print("Lütfen kenarları sırayla giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))

    if a == b and a == c and a == d:
        print("Kare")
    elif a == c and b == d:
        print("Dikdörtgen")
    else:
        print("Dörtgen")


elif shape == "Üçgen":
    a = int(input("Kenar1:"))
    b = int(input("Kenar2:"))
    c = int(input("Kenar3:"))
    if abs(a + b) > c and abs(a + c) > b and abs(b + c) > a:
        if a == b and a == c:
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (
                b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz Şekil...")
