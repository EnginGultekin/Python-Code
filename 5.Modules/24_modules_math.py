# Modules

# Math Module

"""
Ayrıca bir modülü içeri aktarmanın değişik yöntemlerini göreceğiz.
İsterseniz hazır bir modül olan **math** modülünü kullanmaya başlayalım.
"""

#
# Yöntem1 -  import modül_adı
#

"""
Bir modülü içeri aktarmak yani programımıza dahil etmek için 
**import modül_adı** yazabiliriz. İsterseniz bunun için **math**
modülünü içeri aktaralım.
 """

# Modülü içeri aktarıyoruz. Artık bu modülün tüm fonksiyonlarını kullanabiliriz.

import math

# Math modülünün içindekileri görmek için dir fonksiyonunu kullanabiliriz.
print(dir(math))

# Fonksiyonların görevlerini görebilmek için help fonksiyonunu kullanabiliriz.
help(math)

"""
**------------------------------------------**
            modül_adı.fonksiyon_adı()
**------------------------------------------**
"""

help(math.factorial)

print(math.factorial(5))
print(math.factorial(10))

help(math.floor)

print(math.floor(5.4))
print(math.floor(3.5))
print(math.floor(2.8))

help(math.ceil)

print(math.ceil(5.4))
print(math.ceil(3.5))
print(math.ceil(2.8))

"""
Peki biz bir modülü kendi belirlediğimiz isimle nasıl kullanıyoruz ? 
Bunun için de şu şekilde bir şey yapacağız.
"""

import math as matematik

# Modülü artık matematik ismiyle kullanabiliriz.
print(matematik.factorial(6))

#
#  Yöntem2 - from modül_adı import *
#

"""Bir modülü programımıza **dahil etmek** için bu yöntemi de kullanabiliriz.
 İsterseniz **math** modülünü bu yöntem içeri aktaralım."""

from math import *

print(dir(math))

print(factorial(7))
print(floor(4.5))

"""
Peki bir modül içindeki fonksiyonların belli bir kısmını almak için ne 
yapacağız ? Bunun için hangi fonksiyonları alacağımızı özellikle 
belirtmemiz gerekiyor.
"""

# Sadece 2 tanesini dahil ettik.
from math import factorial, floor

print(factorial(5))
print(floor(5.8))
# Dahil etmediğimiz için hata verir
# HATA ---> ceil(3.4)


"""
Peki bu yöntemlerin birbirinden farkı ne  ? 2.yöntemi kullandığımızda 
bildiğimiz gibi sadece fonksiyon isimlerini kullanıyoruz. Ancak eğer 
programa birden fazla modül dahil edersek veya dahil ettiğimiz modülün 
içindeki fonksiyon kendi tanımladığımız fonksiyon ismiyle aynıysa Python 
son gördüğü fonksiyonu çalıştıracaktır.
"""

from math import *


def factorial(num):
    print("Kendi Factorial fonksiyonum.")
    faktoriyel = 1
    if num == 0 or num == 1:
        return 1
    while num >= 1:
        faktoriyel *= num
        num -= 1
    return faktoriyel


print(factorial(5))
print(floor(5.8))
