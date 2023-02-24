# Function

# Find Prime Number


def primeNumber(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print("if you want to exit, press q")
while True:
    num = input("Please enter number: ")

    if num == "q":
        break
    else:
        if primeNumber(int(num)):
            print(num, "Sayısı Asal Sayıdır")
        else:
            print(num, "Sayısı Asal Sayı Değildir")
