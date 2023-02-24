# Function

# Functions Definition and Call

"""
Fonksiyonlar programlamada belli işlevleri olan ve tekrar tekrar kullandığımız
yapılardır. Örneğin kursumuzun başlarından beri kullandığımız **print()**
fonksiyonunun görevi **içine gönderdiğimiz değerleri** ekrana yazdırdırmaktır.
Bu fonksiyon Python geliştiricileri tarafından bir defa yazılmış ve biz de bu
fonksiyonu programlarımızın değişik yerlerinde tekrar tekrar kullanıyoruz.
İşte fonksiyonların kullanım amacı tam olarak budur. Fonksiyonlar bir defa
tanımlanır ve programlarda ihtiyacımız olduğu zaman kullanırız. Ayrıca
fonksiyonlar kod tekrarını engeller ve kodlarımız daha derli toplu durur.

İsterseniz şimdi de  fonksiyonların ne olduğunu gerçek hayattan benzetme
yaparak anlamaya çalışalım. Örneğin evimize bir adet **katı meyve sıkacağı**
alıyoruz ve canımız ne zaman meyve suyu isterse bu aleti kullanıyoruz. Yani
aslında bu aletin görevi ve fonksiyonu **meyve suyu** hazırlamaktır.

Python geliştiricilerin yazdığı fonksiyonlara yani bizim hazır kullandığımız
fonksiyonlara(print(),type() vs.) gömülü fonksiyonlar(built-in function)
denilmektedir.Ancak bunlardan hariç olarak biz kendi özel
fonksiyonlarımızı(user-defined functions) da tanımlayabiliriz.

Peki biz kendi fonksiyonlarımızı nasıl tanımlayacağız ? İsterseniz şimdi
yavaştan fonksiyonların nasıl tanımlanacağını öğrenelim.

"""

# Fonksiyonların Tanımlanması

"""
Fonksiyon tanımlamanın yapısı şu şekildedir;

            def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
                # Fonksiyon bloğu
                Yapılacak işlemler
                # dönüş değeri - Opsiyonel
                
İsterseniz şimdi bir tane "hello" isimli bir fonksiyon tanımlayalım.

"""


def hello():
    print("Hello my friends")
    print("How are you")


print(type(hello))  # Fonksiyonumuz tanımlandı.

# Fonksiyonların Kullanılması veya Çağrılması (Function Call)

"""
Tanımlanan bir fonksiyonun kullanılmasına programlama dillerinde 
*Fonksiyon Çağrısı* denmektedir. O halde **hello** fonksiyonumuzu nasıl 
çağıracağımızı öğrenelim. Fonksiyon çağrısı şu şekilde yapılabilmektedir;

            fonksiyon_adı(Argüman1,Argüman2....)
İsterseniz şimdi **hello** fonksiyonumuzu çağıralım.
"""

# Fonksiyon parametre almadığında içine argümanlarımızı göndermiyoruz.
hello()

# Parametreler ve Argümanlar

"""
Biliyorsunuz biz hello fonksiyonunun içine herhangi bir değer göndermiyorduk 
ve fonksiyonumuz hep aynı işi yapıyordu. Ancak çoğu zaman fonksiyonlarımız 
içine gönderdiğimiz değerlerle farklı işlemler yaparlar. Örneğin **katı meyve 
sıkacağına** eğer "Elma" verirsek elma suyu,  "Nar" verirsek nar suyu 
hazırlayacaktır. Fonksiyonlarda da **Parametreleri** bu şekilde 
düşünebilirsiniz. İsterseniz şimdi **hello** fonksiyonumuzu 
bir tane parametre alacak şekilde tanımlayalım.
"""


def hello(name):
    print("Hoşgeldin,", name)


hello("Lugan Han")
hello("Eng Leng\n")

"""
Bizim *fonksiyon tanımlarken* tanımladığımız herbir değişken birer 
**Parametre** , *fonksiyon çağrısı* yaptığımız zaman içine gönderdiğimiz 
değerler ise **Argüman** olmaktadır. Burada fonksiyonu çağırırken 
gönderdiğimiz "Kemal" değeri "isim" isimli parametreye eşit oluyor ve 
fonksiyonumuz bu değere göre işlem yapıyor. "Ayşe" değerini gönderdiğimizde 
ise fonksiyonumuz bu değere göre işlem yaparak ekrana farklı bir değer 
yazdırıyor. Şimdi isterseniz farklı bir fonksiyon tanımlayalım ve 3 
tane parametre alsın.
"""


def addFunc(a, b, c):
    print("Toplam: ", a + b + c)


addFunc(4, 8, 9)
addFunc(41, 82, 89)


# Factorial Function

def factorial(num):
    result = 1
    if num == 0 or num == 1:
        print("Factorial: ", result)
    else:
        while num > 1:
            result *= num
            num -= 1
        print("Factorial: ", result)


factorial(5)

factorial(7)