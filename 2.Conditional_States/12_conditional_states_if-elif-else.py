# Conditional States

# if-elif-else Koşul Durumları

"""
if condition
    do it ...
elif condition
    do it ...
elif condition
    do it ...

    //
    //

else:
    do it
"""

process = int(input("Choose process 1 or 2 or 3: "))  # 3 tane işlemimiz olsun.

if process == 1:
    print("1. process run.")
elif process == 2:
    print("2. process run.")
elif process == 3:
    print("3. process run.")
else:
    print("can't run  process!")

print("----------------------------")

note = float(input("Notunuzu giriniz: "))

if note >= 90:
    print("AA")
elif note >= 85:
    print("BA")
elif note >= 90:
    print("BA")
elif note >= 80:
    print("BB")
elif note >= 75:
    print("CB")
elif note >= 70:
    print("CC")
elif note >= 65:
    print("DC")
elif note >= 60:
    print("DD")
else:
    print("Can't pass")

print("----------------------")

# Eğer hepsi if bloklarıyla yazılırsa sonuç çok doğru olmayacaktır

if note >= 90:
    print("AA")
if note >= 85:
    print("BA")
if note >= 90:
    print("BA")
if note >= 80:
    print("BB")
if note >= 75:
    print("CB")
if note >= 70:
    print("CC")
if note >= 65:
    print("DC")
if note >= 60:
    print("DD")
else:
    print("Can't pass")
