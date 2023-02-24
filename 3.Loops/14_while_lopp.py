# Loops

# While loop

# Döngüde i değerlerini ekrana yazdırma
i = 0
while i < 10:
    print("i değeri: ", i)
    # Koşulun bir süre sonra False olması için gerekli - Unutmayalım
    i += 1

# Liste üzerinde indeks ile gezinme
liste = [1, 2, 3, 4, 5]
a = 0
# Liste uzunluğu kadar dönecektir tabi a yı arttırdığımız sürece
while a < len(liste):
    print("index: ", a, "item: ", liste[a])
    a += 1
