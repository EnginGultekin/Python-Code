
# Sözlükler : Kısaca index kullanmak yerine her elemana bir value key ataması yapıyoruz

sözlük = {"bir":1 ,"iki":2 ,"üc":3 ,"dort":4}
print(type(sözlük))

# Sözlükler bu şekilde de oluştutrulabilirler

sözlük2 ={}
print(sözlük2)

sözlük3 = dict()
print(sözlük3)
print()

print(sözlük["bir"])
print(sözlük["iki"])

sözlük["bes"] = 5
print(sözlük)
print()


sözlük1 =  {"bir":[1,2,3], "iki":[[1,2],[3,4],[5,6]], "üc":25 }

print(sözlük1)
print(sözlük1["iki"])
print(sözlük1["iki"][1])
print(sözlük1["iki"][1][1])


# İç içe Sözlükler


# Sözlüklerin Metodları 

sözlük4 = {"sayılar":{"bir":1,"iki":2,"üç":3,"dort":4}, "Meyveler":{"yaz":"elma","kıs":"armut","yaz2":"portakal","kıs2":"karpuz","yaz3":"cilek"}}

print(sözlük4)
print(sözlük4["Meyveler"])
print(sözlük4["Meyveler"]["yaz2"])
print()

sözlük4.keys()  #Çalışmıyor

sözlük4.values()   #Çalışmıyor

sözlük4.items()    #Çalışmıyor

for k,v in sözlük4.items():
	print(k,v)












