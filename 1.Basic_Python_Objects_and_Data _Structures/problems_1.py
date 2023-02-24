# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

# Bölüm Sonu problemleri

"""
--- Problem 1 ---
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. 
Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
"""
print("--- 3 tane sayı çarpımı ---")

num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
num3 = int(input("Number3: "))

print("{} * {} * {} = {} Sonucunu vermektedir\n".format(
    num1, num2, num3, (num1 * num2 * num3)))

"""
--- Problem 2 ---
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının 
beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
print("--- Boy kilo indexi ---")

height = float(input("Boy: "))
weight = int(input("Kilo: "))

print("Beden Kitle indexi: {}\n".format(weight / (height ** 2)))
"""
--- Problem 3 ---
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı 
bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
print("--- Araç yol ücreti ---")

cost = float(input("Kilometre başına yakıt maliyeti: "))
road = float(input("Gidilecek toplam kilometre: "))

totalCost = cost * road
print("Ödenmesi gereken tuttar: {} $\n".format(totalCost))

"""
--- Problem 4 ---
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları 
alt alta ekrana yazdırın.
"""
print("--- User Information ---")
name = input("Name: ")
surname = input("Surname: ")
number = input("Number: ")
print("\nInformation...\n")
print("Name: {}\nSur: {}\nNum: {}\n".format(name, surname, number))

"""
--- Problem 5 ---
Kullanıcıdan iki tane sayı isteyin ve bu sayıların 
değerlerini birbirleriyle değiştirin.
"""
print("--- Change values ---")

num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
print("Before Change\nNumber1: {}\nNumber2: {}".format(num1, num2))
num1, num2 = num2, num1
print("After Change\nNumber1: {}\nNumber2: {}\n".format(num1, num2))

"""
--- Problem 6 ---
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs 
uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""
print("--- Hypotenuse Formula ----")

edge1 = int(input("edge1: "))
edge2 = int(input("edge2: "))
hypotenuse = (edge1 ** 2 + edge2 ** 2) ** 0.5

print("Hypotenuse: ", hypotenuse)
