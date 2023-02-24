# Loops

print("""*******************
Faktoriyel Bulma Programı

Programdan çıkmak için 'q' ya basın.
*******************""")
while True:
    number = input("\nSayı: ")
    if number == "q":
        print("Programdan çıkılıyor...")
        break
    number = int(number)

    faktoriyel = 1
    for i in range(2, number + 1):
        faktoriyel *= i

    print("Faktoriyel:", faktoriyel)
