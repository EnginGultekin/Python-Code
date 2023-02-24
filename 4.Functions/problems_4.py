# Function

"""
Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""


def perfectNum(num):
    toplam = 0
    for n in range(1, num):
        if num % n == 0:
            toplam += n

    return toplam == num


for i in range(1, 1001):
    if perfectNum(i):
        print("Mükemmel Sayı:", i)

"""
Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini 
(EBOB) dönen bir tane fonksiyon yazın.
"""


def findEbob(numb1, numb2):
    ebob = min(numb1, numb2)

    while True:
        if numb1 % ebob == 0 and numb2 % ebob == 0:
            return ebob
        else:
            ebob -= 1


"""  2. Yol
    e = 1
    ebob = 1
    while e <= numb1 and e <= numb2:
        if not (numb1 % e) and not (numb2 % e):
            ebob = e
        e += 1
    return ebob
"""

num1 = int(input("\nSayı-1: "))
num2 = int(input("Sayı-2: "))

print("Ebob:", findEbob(num1, num2))

"""
Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını 
(EKOK) dönen bir tane fonksiyon yazın.
"""


def findEkok(num3, num4):
    ekok = max(num3, num4)

    while True:
        if ekok % num3 == 0 and ekok % num4 == 0:
            return ekok
        else:
            ekok += 1


""" 2. Yol
    k = 2
    ekok = 1

    while True:
        if num3 % k == 0 and num4 % k == 0:
            ekok *= k
            num3 //= k
            num4 //= k

        elif num3 % k == 0 and num4 % k != 0:
            ekok *= k
            num3 //= k

        elif num3 % k != 0 and num4 % k == 0:
            ekok *= k
            num4 //= k
        else:
            k += 1
        if num3 == 1 and num4 == 1:
            break
        return ekok    
"""

nums1 = int(input("\nSayı-1: "))
nums2 = int(input("Sayı-2: "))

print("Ekok:", findEkok(nums1, nums2))

"""
Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu 
bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi
"""

digitOne = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz",
            "Dokuz"]
digitTen = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş",
            "Seksen", "Doksan"]


def readNumbers(number):
    first = number % 10
    second = number // 10

    return digitTen[second] + " " + digitOne[first]


number1 = int(input("\nPlease enter a number: "))

print(readNumbers(number1))

"""
Problem 5
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana 
yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
"""


def findPisagor():
    pisagorList = list()
    for p in range(1, 101):
        for j in range(1, 101):
            c = (p ** 2 + j ** 2) ** 0.5
            if c == int(c):
                pisagorList.append((p, j, int(c)))
    return pisagorList


for i in findPisagor():
    print(i)
