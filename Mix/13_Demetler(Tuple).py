
# Demetler (Tuple'lar) Listelere Benzerler ancak tek farkları Değiştirilemez  olmalarıdır

demet = (1,2,3,4,5,6,7)
print(type(demet))
print()

print(demet[4])
print()

print(demet[:4])
print()

print(demet[::-1])
print() 

# Demetlerin Temel Methotları (Sadece iki metodları vardır )  count() index()

demet2 = (1,1,1,1,1,2,2,3,5,4,7)

print(demet2.count(1))
print(demet2.count(5))
print(demet2.count(6))
print()

demet3 = ("Python","PHP","Java","C")

print(demet3.index("PHP"))
print()












