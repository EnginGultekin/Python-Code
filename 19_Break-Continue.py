
# Break and Continue

while True:
	isim = input("(çıkmak için q'ya basın) İsminiz Girin:")
	print("Adınız:",isim)
	if(isim == 'q'):
		print("Çıkış Yapıldı")
		break                         #Break ile Çıkış yapıldı
		
liste = list(range(0,10))
		
for x in liste:
	if(x==1  or x==3 or x==8):
		continue                  #Continue değerler için devam etti ama o değerleri yazmadı
	print("x: ",liste[x])
	
		

	