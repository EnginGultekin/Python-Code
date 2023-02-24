# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

"""
Verilen denklemin köklerini bulma

2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c
Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)
"""

num1 = int(input('number1: '))
num2 = int(input('number2: '))
num3 = int(input('number3: '))

print("Girilen Denklem: {}x^2 + {}x + {}\n".format(num1, num2, num3))

delta = num2 ** 2 - 4 * num1 * num3

root1 = (-num2 + delta ** 0.5) / (2 * num1)
root2 = (-num2 - delta ** 0.5) / (2 * num1)

print('Denklemin\nBirinci kökü: {}\nİkinci kökü: {}\n'.format(root1, root2))
