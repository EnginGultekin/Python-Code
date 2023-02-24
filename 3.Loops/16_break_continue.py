# Loops

# Break ifadesi
"""
Döngü herhangi bir yerde ve herhangi bir zamanda break
ifadesiyle karşılaştığı zaman çalışmasını bir anda durdurur.
Böylelikle döngü hiçbir koşula bağlı kalmadan sonlanmış olur.

break ifadesi **sadece ve sadece** içindeki bulunduğu döngüyü sonlandırır.
Eğer iç içe döngüler bulunuyorsa ve en içteki döngüde break kullanılmışsa
sadece içteki döngü sona erer. Örneklerle *break* ifadesini anlamaya çalışalım.
"""

i = 0

while i < 20:
    print(i)
    if i == 7:
        # i değeri 10 trunc bu koşul sağlanıyor ve  break
        # ifadesiyle karşılaşıldığı için döngü anında sona eriyor.
        break
    i += 1
print("------------------")

# for döngüsüyle break kullanalım.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in liste:
    if i == 4:
        break
    print(i)

# continue ifadesi

"""
Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle 
karşılaştığı zaman geri kalan işlemlerini yapmadan direk bloğunun başına döner.
        
*continue* ifadesini anlamak için örneklerimize bakalım.
"""

i = 0

while i < 5:

    if i == 2:
        i += 1  # Artırma işlemini yapmasak devam edemez
        continue

    print("i:", i)
    i += 1

print("------------------------")

liste = [1, 2, 3, 4, 5, 6]

for i in liste:
    if i == 3 or i == 5:
        continue
    print("i:", i)
