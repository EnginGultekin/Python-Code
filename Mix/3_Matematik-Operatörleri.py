# -*- coding: utf-8 -*-
 
"""Bu kodda sırayla   
    Toplama
       Çıkarma
         Çarpma
            Bölme 
              Tam Sayı Bölmesi            
                 Bölümden Kalanı Bulacağız 
                    Üst Alma
                       Karakök Alma 
                         Küp Kök Alma 
                      
"""
s1 =10
s2 =5
s3 =20
s4 =8
s5 =2.8
s6 =9.554   
s7 =62.4
s8 = -5
s9 = -13
s10 = -6.35

# Toplama ' + '
print("Toplama1:",s1+s2+s4)
print("Toplama2:",s5+s6)
print("Toplama3:",s8+s10)
print("Toplama4:",s2+s8)
print()

# Çıkarma ' - '  
print("Çıkarma1:",s3-s4)
print("Çıkarma2:",s8-s7)
print("Çıkarma3:",s9-s8)
print("Çıkarma4:",s6-s10)
print()

# Çarpma ' * '
print("Çarpma1:",s4*s5)
print("Çarpma2:",s8*s1)
print("Çarpma3:",s9*s10)
print()

# Bölme ' / ' 
print("Bölme1:",s3/s2)
print("Bölme2:",s7/s6)
print("Bölme3:",s9/s1)
print()

# Tam Sayı Bölmesi ' // ' bu ifade ile yapılır
print("Bölme:65/9=",65/9)
print("Tam Sayı BÖlmesi:65/9=",65//9) 
print()

# Bölümden kalanı bulma ' % ' 
print("92/9 Bölümünden kalan =",92%9)
print("12/3 Bölümünden kalan =",12%3)
print("65.45/8.2 Bölümünden kalan =" ,65.45%8.2) 
print()

# Üst alma ' ** ' işareti ile istediğimiz sayını istediğimiz kuvvetini alabiliriz
print("a^b = a**b = b kadar a.a...")
print("4'ün 3.Kuvveti =",4**3)
print()

# Karakök bulma ' ** ' işareti ile aynı ama (0.5. kuvvetini alıyoruz)
print("81'in Karakökü =",81**0.5)
print("122'nin Karakökü =",122**0,5)
print()

# Küp Kök Bulma
print("sayı ** (1/3)")
print("27'nin Küp Kökü=",27**(1/3))
print()

"""
                            Operatörleri beraber kullanma ve İşlem sırası

Bütün bu öğrendiğimiz şeyleri beraber nasıl kullanabiliriz? Bunun için matematikteki işlem sırasını biliyorsak çok rahat edeceğiz, çünkü Pythondaki işlem sırası matematiktekiyle birebir aynıdır. Nedir bu işlem sırası ? Kurallar şunlar ;

   - 1. Parantez içi her zaman önce yapılır.
   - Çarpma ve Bölme her zaman Toplama ve Çıkarma işlemine göre önce yapılır.
   - İşlemler soldan sağa değerlendirilir.

Ancak, buradaki işlemleri ezberlememize hiç gerek yok. Kafamızın karıştığı yerler de işlemleri parantez içine almak, hayat kurtarır 🙂 Şimdi örneklere bakalım.

"""
