# Conditional States

# Calculator

print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
-----------------------------------------------------------
""")

operation = int(input("Lütfen yapmak istediğiniz işlem türünü seçiniz: "))

num1 = int(input('Birinci sayı: '))
num2 = int(input('İkinci sayı: '))

if operation == 1:
    print('{} + {} = {}'.format(num1, num2, (num1 + num2)))
elif operation == 2:
    print('{} - {} = {}'.format(num1, num2, (num1 - num2)))
elif operation == 3:
    print('{} * {} = {}'.format(num1, num2, (num1 * num2)))
elif operation == 4:
    print('{} / {} = {}'.format(num1, num2, (num1 / num2)))
else:
    print('Geçersiz işlem türü')
