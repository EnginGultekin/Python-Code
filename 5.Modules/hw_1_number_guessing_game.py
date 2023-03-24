# Modules

# Guessing Game

import random
import time

print("""************************

Sayı Tahmin Oyunu

1 ile 1000 arasında sayıyı tahmin edin.

************************""")

randomNumber = random.randint(1, 1000)
guessingCount = 10

while True:
    number = int(input("Tahmininiz: "))

    if number < randomNumber:
        print("Bilgiler Sorgulacnıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin....")
        guessingCount -= 1


    elif number > randomNumber:
        print("Bilgiler Sorgulacnıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin....")
        guessingCount -= 1

    else:
        print("Bilgiler Sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler! Sayımız", randomNumber)
        break

    if guessingCount == 0:
        print("Tahmin Hakkınız Bitti...")
        print("Sayımız: ", randomNumber)
        break

    print("Kalan Tahmin Hakkınız: ", guessingCount)