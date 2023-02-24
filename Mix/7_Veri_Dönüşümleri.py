# -*- coding: utf-8 -*- 

# Veri Tipleri Dönüşümleri

"""   1-Tamsayıyı Ondalıklı Sayıya Çevirme
""" 
a=58
print(float(a))
print(float(2))
print(float(932))
print(float(-65))
print("---------------------------------")

"""   2-Ondalıklı Sayıyı Tamsayıya Çevirme
"""
b=23.3435
print(int(b))
print(int(1.4868995454995))
print(int(5.0))
print(int(-6.515))
print("---------------------------------")

"""   3-Sayıları Stringlere Çevirme
"""
c=343
c=str(c)                 #Bu işlemi yapınca 343 artık 3 karakterli bir String olur
print(c,"  Uzunluğu:",len(c)) #Burda ise stringi yazdırıp ve uzunluğunu alıp String olduğunu kanıtlıyoruz   ' 3 '

c=str(5.98)   
print(c,"  Uzunluğu:",len(c))    # ' 4 '

c=str(-512.854)
print(c,"  Uzunluğu:",len(c))    # ' 8 '
print("---------------------------------")       

"""   4-Stringleri Tamsayıya Çevirme
"""
d='123456789'
d=int(d)        #Yukarıdaki stringi  bir tamsayıya çevirdik
print(d)          #HATALI KOOD:  d='123abc' Şeklinde Olsaydı Bu Stringi İnteger Değere dÖnüştüremezdik 
print(d+876543211)   #Burasıda Değişkeni İnteger Değere Dönüştüdüğümüzün Kanıtı Niteliğindedir
print("---------------------------------")

"""   5-Stringleri Ondalıklı Sayıya Çevirme
"""
e='412.54'
e=float(e)      #Stringi Ondalıklı Sayıya Çevirdik
print(e)          #HATALI KOOD:  e='12.82.51' Bu şekilde bir Stringi Ondalıklı sayıya dönüştüremeyiz
print(e+87.46) 
print("---------------------------------")
















