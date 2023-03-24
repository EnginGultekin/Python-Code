# Modules

"""
--- Proje 1 ---

**Math** modülündeki hazır fonksiyonları kullanarak gelişmiş bir
hesap makinesi geliştirmeye çalışın."""

import math
import time

print("""
 Hesapmakinesi
 
 Toplama için : +
 Çıkarma için : -
 Çarpmak için : *
 Bölmek için  : /
 Tam bölmek için : //
 Kuvvetini Almak için : **
 Kare Kökünü almak için : /*
 Faktoriyel almak için  : !

 
 Çıkmak için : q ya basmalısınız     
    
""")

result = 0

while True:
    num1 = input("\nLütfen birinci sayı giriniz: ")
    if num1 == 'q':
        print("\nProgram sonlandırılıyor...")
        time.sleep(1)
        break
    op = input("Lütfen yapacağınız işlemi seçiniz: ")
    if op != '/*' and op != '!':
        num2 = int(input("Lütfen ikinci sayı giriniz: "))

    num1 = int(num1)
    if op == '+':
        result = num1 + num2
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '-':
        result = num1 - num2
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '*':
        result = num1 * num2
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '/':
        result = num1 / num2
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '//':
        result = num1 // num2
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '**':
        result = math.pow(num1, num2)
        print("{} {} {} = {}".format(num1, op, num2, int(result)))
    elif op == '/*':
        result = math.sqrt(num1)
        print("{} = {}".format(num1, int(result)))
    elif op == '!':
        result = math.factorial(num1)
        print("{} = {}".format(num1, int(result)))
    else:
        print("Hatalı işlem yaptınız tekrar deneyin")

"""
--- Proje 2 --- 

**Math** modülünde kullandığınız fonksiyonları kendiniz de ayrı bir 
modüle (Python dosyasına) yazmaya çalışın ve bu yazdığınız modülü 
kullanarak gelişmiş bir hesap makinesi yazın."""

import module_func_library as custom
import time

print("""
 Hesapmakinesi

 Toplama için : +
 Çıkarma için : -
 Çarpmak için : *
 Bölmek için  : /
 Tam bölmek için : //
 Kuvvetini Almak için : **
 Kare Kökünü almak için : /*
 Faktoriyel almak için  : !


 Çıkmak için : q ya basmalısınız     

""")

result = 0

while True:
    num1 = input("\nLütfen birinci sayı giriniz: ")
    if num1 == 'q':
        print("\nProgram sonlandırılıyor...")
        time.sleep(1)
        break
    op = input("Lütfen yapacağınız işlemi seçiniz: ")
    if op != '/*' and op != '!':
        num2 = int(input("Lütfen ikinci sayı giriniz: "))

    num1 = int(num1)
    if op == '+':
        result = custom.add(num1, num2)
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '-':
        result = custom.subtraction(num1, num2)
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '*':
        result = custom.multiply(num1, num2)
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '/':
        result = custom.divide(num1, num2)
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '//':
        result = custom.divideInteger(num1, num2)
        print("{} {} {} = {}".format(num1, op, num2, result))
    elif op == '**':
        result = custom.power(num1, num2)
        print("{} {} {} = {}".format(num1, op, num2, int(result)))
    elif op == '/*':
        result = custom.sqrt(num1)
        print("{} = {}".format(num1, int(result)))
    elif op == '!':
        result = custom.factorial(num1)
        print("{} = {}".format(num1, int(result)))
    else:
        print("Hatalı işlem yaptınız tekrar deneyin")
