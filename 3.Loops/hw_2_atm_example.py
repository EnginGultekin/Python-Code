# Loops

print("********************\nATM sistemine hoşgeldiniz\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme


Programdan 'q' tuşu ile çıkabilirsiniz.
""")

# Bakiyemiz 1000 lira olsun.
balance = 1000

while True:
    process = input("\nYapmak istediğiniz işlemi giriniz: ")

    if process == "q":
        print("Yine bekleriz....")
        break
    elif process == "1":
        print("Bakiyeniz {} $".format(balance))

    elif process == "2":
        amount = int(input("Yatırmak istediğiniz tutar: "))
        balance += amount
        print("Bakiyeniz {} $".format(balance))

    elif process == "3":
        amount = int(input("Çekmek istediğiniz tutar: "))
        if balance - amount < 0:
            print("Bakiyeniz yeterli değil...")
            print("Bakiyeniz {} $".format(balance))
            continue
        balance -= amount

    else:
        print("Lütfen geçerli bir işlem giriniz.")
