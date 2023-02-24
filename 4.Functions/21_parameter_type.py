# Function

# Functions Parameter Type

# Default değer verip fonksyon tanımlayalım

def hello(name="Anybody"):
    print("Welcome, ", name)


# Hiç bir değer göndermedik. "isim" parametresinin değeri varsayılan
# olarak "İsimsiz" olarak belirlendi

hello()

# Değer verirsek varsayılan değerin yerine bizim verdiğimiz değer geçer.
hello("Lugan Han\n")


def showInfo(name="Bilgi Yok", surname="Bilgi Yok", num="Bilgi Yok"):
    print("\nAd:", name, "\nSoyad:", surname, "\nNumara:", num)


showInfo()
showInfo("Lugan", "Han")
showInfo(num="541522")


# NOOT !!!!!!  help(print)  # sep parametresine varsayılan olarak boşluk
# değeri verildiğini görebiliyoruz.


# Esnek Sayıda Değerler

def add(a, b, c):
    print(a + b + c)


# add(5,6,3,3) 4 tane argüman veremeyiz. Hata alırız
# add(5,6) 2 tane argüman veremeyiz. Hata alırız

"""
Peki istediğimiz kadar argüman kullanmak için ne yapmalıyız
 * YILDIZLI PARAMETRE * kullanmamız gerekiyor
"""


# Artık parametreler değişkenini bir demet gibi kullanabilirim.
def addNums(*parameters):
    result = 0
    print("\nParameters:", parameters)
    for i in parameters:
        result += i
    return result


print("Toplam: ", addNums(6, 3, 9, 8, 7, 4, 1, 23, 12, 45))

print("Toplam: ", addNums())

print("Toplam: ", addNums(6, 3))
