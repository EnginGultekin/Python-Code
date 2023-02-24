# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

# Sözlük (Dictionary) yapısı diğer dillerdeki map'a denk gelmektedir

dict1 = {'zero': 0, 'one': 1, 'two': 2}
print(dict1)

# boş tanımlama
dict2 = {}
dict3 = dict()

# elemanlara ulaşma ( key-value )
print(dict1['one'])

dict1 = {
    'list1': [1, 2, 3, 'python'],
    'list2': [[1, 2], [3, 4], [5, 6]],
    'list3': 45
}

# sözlüğün içindeki liste tutan listenin içindeki 2. liste elemanı 4
print('liste elemanının elemanı', dict1['list2'][1][1])

dict1['list3'] += 15
print('toplama özelliği:', dict1['list3'])

print('Sözlüğün tamamı: ', dict1)
print('---------------------------')

dict5 = {'one': 1, 'eleven': 11, 'two': 2}
print('Öncesi: ', dict5)
dict5['there'] = 3
print('Sonrası', dict5)

print('---------------------------')

# İç içe sözlükler
dict6 = {
    "numbers": {"one": 1, "two": 2, "three": 3},
    "fruits": {"cheery": "summer", "orange": "winter", "plum": "summer"}
}

print(dict6['numbers']['one'])
print(dict6['fruits']['orange'])

print('---------------------------')

# Temel Sözlük Methodları " values(), keys(), items() "

dict1 = {"one": 1, "two": 2, "three": 3}
print('Values: ', dict1.values())
print('Keys: ', dict1.keys())
print('Items: ', dict1.items())
