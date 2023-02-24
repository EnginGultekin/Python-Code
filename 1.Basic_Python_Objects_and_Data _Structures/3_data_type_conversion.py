# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

# Veri Tip dönüşümü
integer = 51
print('int float oldu: ', float(integer))

# Ondalık sayıyı tam sayıya çevirme
print('Ondalık sayı oldu: ', int(4.7))

# Sayıları stringe  çevirme
number = 4587
metin = str(number)
print('integer String oldu: ', metin, ' Buda string uzunluğu:', len(metin))

# Stringi tam sayıya çevirme bunu yaparken
# stringin tüm karakterlerin rakam olması önemlidir

metin = '36545421554545'
number = int(metin)
print('String oldu integer: ', number)
