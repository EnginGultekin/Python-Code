# Custom Module

"""
Buraya istediğimiz kadar obje ve fonksyon yazabiliriz
ve her yerde kullanmak istersek bu dosyayı  ** Python35/Lib ** klasörü
altında tanımlayabiliriz
"""

explanation = ['Module', 'List', 'Fonksyonlar', 'import']


# İki Sayı Toplama Fonksyonu
def add(num1, num2):
    return num1 + num2


# İstediğimiz Kadar Sayı Toplama Fonksyonu
def addMultipleNumbers(*parameters):
    result = 0
    for i in parameters:
        result += i
    return result


# İki Sayı Çıkarma Fonksyonu
def subtraction(num1, num2):
    return num1 - num2


# İki Satı Arasındaki Fark Hesaplayan Fonksyon
def difference(num1, num2):
    return max(num1, num2) - min(num1, num2)


# İki Sayıyı Çarpma Fonksyonu
def multiply(num1, num2):
    return num1 * num2


# İstediğimiz Kadar Sayı Çarpım Fonksyonu
def multiplyNumbers(*parameters):
    result = 1
    for i in parameters:
        result *= i
    return result


# İki Sayı bölme Fonksyonu
def divide(num1, num2):
    return num1 / num2


# Tam Sayı bölme Fonksyonu
def divideInteger(num1, num2):
    return num1 // num2


# Kuvvet Alma
def power(num, po):
    for i in range(1, po + 1):
        num *= num
    return num


# Kare Kök Alma
def sqrt(num):
    return num ** 0.5


# Faktoriyel Alma
def factorial(num):
    for i in range(1, num):
        num *= i
    return num
