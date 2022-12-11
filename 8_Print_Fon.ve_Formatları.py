# -*- coding: utf-8 -*-

""" Bu kod içeriğinde 'Print' fonksyonunu ve formatlarını göstreceğiz
"""
# \n Karakteri  alt satıra geçmeyi sağlıyor
print("Alt satıra geç\n Geçtim")

# \t Karakteri  aynı satırda Tab boşluğu bırakmayı sağlıyor 
print("Boşluk Bırak\t Bıraktım\n")

# type() Fonksyonu istediğimiz değişkenin tipini öğrenmemizi sağlıyor
print(type(3))            # İnteger
print(type(3.4))          # Float
print(type('Engin'))      # String
print()

# sep() Fonksyonu yazdırdığımız verilerin arasına istediğimiz karakteri koymamızı sağlıyor
print(15,10,1999,sep = "/") 
print(21,35,7545,5,sep = ".")
print("T","B","M","M",sep = ".") 
print() 

""" YA DA daha kısa bir yolla '*' parametresini kullanarak yapabiliriz
"""
print(*"TBMM",sep = ".") # '*' operatörü girdiğmiz karakterler arasında birer boşluk bırakıyor
print(*"Python")
print(*"ython",sep = "\n")
print()
 
# Formatlama Bunu Ezberlememize Gerek Yok İstediğimiz Zaman Siteden Bakabiliriz .....  


