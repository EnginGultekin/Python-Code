# Loops

"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.

1,1,2,3,5,8,13,21,34...............
"""
firstNumber = 1
secondNumber = 1
fibonacci = [firstNumber, secondNumber]

ranges = int(input("Fibbonacciyi kaçıncı aşamada görmek istiyorsunuz: ")) - 2

for i in range(ranges):
    firstNumber, secondNumber = secondNumber, (firstNumber + secondNumber)
    fibonacci.append(secondNumber)
print(fibonacci)
