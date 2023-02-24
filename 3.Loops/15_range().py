# Loops

# range() function

"""
Bu yapı başlangıç, bitiş ve opsiyonel olarak artırma değeri alarak listelere
benzeyen bir sayı dizisi oluşturur.
"""

#  range(0,25,5) --> 0 dan başla 25 e kadar 25 (dahil değil)
#  5 er 5 er atlayarak sayıları oluştur

# 0'dan 20' a kadar (dahil değil) sayı dizisi oluşturur.
print(range(0, 20))

# Yazdırmak için başına "*" koymamız gerekiyor.
print(*range(0, 20))

# list fonksiyonuyla listeye dönüştürebilir.
list1 = list(range(0, 20))
print(list1)

print(*range(5, 10))

# Başlangıç değeri vermediğimiz 0'dan başlar
print(*range(8))

# 5'ten 100'e kadar olan ve 5 ile bölünebilen sayılar
print(*range(3, 100, 10))

""" !!!!!!
# 20'den geri gelen sayıları oluşturmaz.
print(*range(20,0))  Çalışmaz
"""

# 20'den geri gelen sayıları oluşturur.
print(*range(20, 0, -2))

# for ile range() kullanımı
for num in range(0, 10):
    print(num)

for num in range(1, 20):
    print("* " * num)
