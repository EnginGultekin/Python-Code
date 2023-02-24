# Function

# Divisors Numbers

def findDivisors(number):
    divisors = []
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


print("if you want to exit, press q")
while True:
    num = input("Number:")

    if num == "q":
        print("Program Ending ...")
        break
    else:
        num = int(num)
        print("Divisors:", findDivisors(num))
