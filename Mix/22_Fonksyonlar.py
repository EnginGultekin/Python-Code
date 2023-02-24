
# Fonksyonlar tanımlaması "def Fon._adı(parametre (lazımsa)) : "


def selamlama():                # Burda  parametre almamıştır
	print("Hoşgeldiniz aq .")
	
selamlama()	


def isimler(isim):          # Burda string bir parametre almıştır
	print("Adınız:",isim)

isimler("Engin Gültekkin")


def topla(a,b,c):                    # Burda integer üç parametre almıştır
	print("Toplamları:",(a+b+c))
	
topla(5,10,15)	


def Factorial(x):
	temp=x
	fac=1
	if(x==0 or x==1):
		print(temp,"'in Factoriali:",fac)
	else:
		while(x >= 1):
			fac *= x
			x-=1
		print(temp,"'in Factoriali:",fac)	
		
		
Factorial(0)
Factorial(1)
Factorial(2)
Factorial(3)
Factorial(4)
Factorial(5)

		

def toplama(a,b,c):
	return a+b+c
	
def carp(sayi):
	return sayi*10
	
	
top = toplama(3,5,7)
print(carp(top))	

def top(say):
	return say+20
	
def car(say):
	return say*10

def bol(say):
	return say/7

print(car(bol(top(5))))	
	
	
	
	
	
	
	
	
	
	





