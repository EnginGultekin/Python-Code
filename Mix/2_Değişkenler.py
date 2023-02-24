# -*- coding: utf-8 -*- 

""" Pythonda C ve Javadaki gibi veri tipi belirtmeden değikenlere
        değer atayabiliyoruz örneğin bi sayı dğişkeni oluşturalım ve bir tam  
           sayı atıyalım " sayı = 10 " ve daha sonra istersek  " sayı = 2.3 " gibi bir 
              float değer atıyabiliriz buda Python'nın güzelliklerinden biridir.
"""

# Tam sayı atama
sayı= 17
print("First Value:",sayı)

# Aynı değişkene Float değer atama
sayı= 22.345
print("Second Value:",sayı)                    


a=5
b=14
# Değişkenleri değişkenlere atamak
c= 2*a + b
print("C:",c)
print()
print("Before change: a=",a,"and b=",b)

# NOOOT: **** İt is very İmportant ****
# iki değişkenin değerlerini birbiriyle değiştirmek Python da çok kolaydır

a,b=b,a # şeklinde yazarsak a=14 ve b=5 olacaktır  
print("After change: a=",a,"and b=",b)



""" Son olarak değişkenlerimize isim verirken dikkat etmemiz gereken noktalardan bahsedelim.

    1. Değişken isimleri bir sayı ile başlayamaz.
    2. Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
    3. :'”,<>/?|\()!@#$%^&*~-+ Buradaki semboller değişken ismi içinde kullanılamaz.(Sadece _ sembolü kullanılabilir)
    4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz.(while, not vs. )
"""

# Hatalı ' i? = 5 ' ,' 3i= 5 ' ...

#Doğru  ' _i = 5 ' 



