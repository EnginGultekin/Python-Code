# Tutorials 1:  Temel Python Objeleri ve Veri Yapıları

"""
Oyuncu bilgilerini al , bilgileri bir listede tut ve ekrana yazdır
"""

print("--- Oyuncu Kaydetme Programı ---")

name = input('Player name: ')
surname = input('Player surname: ')
age = int(input("Player age: "))
team = input("Player team: ")

playerInf = [name, surname, age, team]

print("\nBilgiler Kaydediliyor....\n")

print(
    "Player name: {}\nPlayer surname: {}\nPlayer age: {}\nPlayer team: {}\n".format(
        playerInf[0], playerInf[1], playerInf[2], playerInf[3]))

print("Bilgiler Kaydedildi.")
