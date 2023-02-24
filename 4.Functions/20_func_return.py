# Function

# Functions Return


"""
Bu konuda fonksiyonlardan değer döndürmemizi sağlayan **return** ifadesini
görmeye çalışacağız. Önceki bölümde yazdığımız fonksiyonları hatırlayacak
olursak, bu fonksiyonlar sadece ekrana **print** ile değer yazdırıyordu.
Ancak bu fonksiyonlar yaptıklar işlemler bize herhangi bir değer vermiyorlardı.
Ancak biz programlarımızda bir fonksiyon sonucunda elde edilen değerleri
alıp programlarımızın bambaşka yerlerinde kullanmak isteyebiliriz. Bu derste
bunu nasıl yapacağımızı öğrenmeye çalışacağız.

**return** ifadesi fonksiyonun işlemi bittikten sonra **çağrıldığı yere**
değer döndürmesi  anlamı taşır. Böylelikle, fonksiyonda aldığımız değeri bir
değişkende depolayabilir ve değeri programın başka yerlerinde kullanabiliriz.
Şimdi iki tane çok basit fonksiyon yazalım ve **return** neden gereklidir
anlamaya çalışalım.
"""


# return'un kullanımı

def add(a, b, c):
    return a + b + c


def multiple(num):
    return num * 2


print(multiple(add(2, 4, 6)))

"""
İşte **return** ifadesinin anlamı tam olarak budur. **return** yardımıyla 
fonksiyonlar değerleri çağrıldığı yere döndürebilir ve biz de bu değerleri 
istediğimiz yerde kullanabiliriz. 
"""


def multipleThree(num):
    print("1.Func run")
    return num * 3


def addTwo(num):
    print("2.Func run")
    return num + 2


def divideFour(num):
    print("3.func Run")
    return num / 4


print(divideFour(addTwo(multipleThree(5))))

"""
**return** ifadesinden sonra fonksiyonumuz tamamıyla sona erer. Yani, 
**return** ifadesinden sonra yapılan herhangi bir işlem çalıştırılmaz.
"""


"""
Fonksiyonlarda çağrıldığı yere herhangi bir değer döndürmeyen
(**return kullanılmayan**) fonksiyonlara **void** fonksiyonlar denmektedir..
"""
