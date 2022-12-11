
# if - elif - else

vize1 = int(input("Vize1 (%30) : "))
vize2 = int(input("Vize2 (%30) : "))
final = int(input("Final (%40) : "))

sonuc = vize1*1/3 + vize2*1/3 + final*1/4

if(sonuc >= 90):
	print("AA : Pek Çok İyi")
elif(sonuc >= 85):
	print("AB : Çok İyi")
elif(sonuc >= 80):
	print("BB : İyi")
elif(sonuc >= 75):
	print("BC : Orta")
elif(sonuc >= 70):
	print("CC : Zayıf")
elif(sonuc >= 65):
	print("CD : Çok Zayıf")
elif(sonuc >= 60):
	print("DD : Sınırda")
elif(sonuc <= 60 ):
	print("FF : Kaldınız")
else:
	print("Girmedi")
	