# Function

# Global and Local variables

"""
Bu konuda **global** ve **yerel (local)** değişkenleri öğrenmeye çalışacağız.


Pythonda her bir değişkenin, fonksiyonun ve ileride göreceğimiz
sınıfların(class) aslında bir **kapsamı(scope)** bulunur ve Python herbir
değişkeni bir **isim alanında (namespace)** tanımlar. Değişkenlerin
**İsim alanı** ise,  bu değişkenlerin nerelerde var olduğunu ve
nerelerde kullanılabileceğini gösterir.

Pythonda fonksiyonlarda tanımlanan değişkenler Python tarafından
**Yerel (Local) değişkenler ** olarak tanımlanırlar. Yani bir
**fonksiyon bloğunda**  oluşturulan değişkenler fonksiyona özgüdür ve
**fonksiyon çalışmasını** bitirdikten sonra bu değişkenler bellekten silinir
ve yok olur. Böylelikle , fonksiyon içinde tanımlanmış bir değişkene
başka bir yerden **erişilemez**.

Pythonda en genel kapsama sahip değişkenler ise **Global değişkenler**
olarak tanımlanırlar ve global değişkenlere **tanımlandığı andan itibaren**
programın her yerinden ulaşabiliriz.

***Yerel değişkenleri*** anlamak için bir tane fonksiyon tanımlayalım.
"""


def func1():
    num = 10  # Yerel isim alanında bir değişken
    print(num)


func1()
# print(num)  burda kullanamayız çünkü etki alanı dışında


# Global isim alanında bir değişken .
a = 5


def func2():
    print(a)  # a değişkeni globalde tanımlandığı için burada tanımlı.


func2()

""" Example """

# Globalde tanımlanmış bir değişken
c = 10


def func3():
    c = 2  # Yerelde tanımlanmış bir değişken
    print(c)  # Yerel değişken kullanılıyor.


func3()
print(c)

"""
Kodumuz çalıştığında ilk olarak **c** isimli global değişken oluşuyor. 
**fonksiyon çağrıldığında ise** **c** isimli başka bir yerel değişken 
oluşuyor gibi düşünebilirsiniz. Böyle bir durumda elimizden iki tane **c** 
değişkeni var. Python bu durumda **global c** değişkeni yerine **kendi 
yerel c** değişkenini kullanıyor. 
"""

# Global deyimi

"""
Peki bir fonksiyonda globalde tanımlanmış bir değişkeni nasıl kullanacağız ? 
Bunun için Pythonda **global** ifadesi bulunmaktadır. Şimdi aşağıdaki 
kodu beraber inceleyelim.
"""

d = 10


def func4():
    global d

    print(d)
    d = 4
    print(d)


func4()
print(d)

"""
bu kullanımla fonkyonumuz d global değişkenini yerelde kullanmak istediğini 
belirtmiş oluyor 

Peki bu yerel değişkenler sadece fonksyonlarda mı yoksa if-else ya da while da 
da yerel olarak tanımlanıyor. 
"""

# aşağıda görüldüğü gibi global olarak tanımlanmıştır

if True:
    t = 10
    print(t)

print(t)

while True:
    value = 7
    print(value)
    break

print(value)
