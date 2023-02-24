
# List Comprehension Yöntemi ile Bir listeyi Başka bir listeye kolayca eşitliyebiliyoruz

#List Comprehension kullanmadan yapalım

liste = [1,2,3,4,5]
liste1 = list()

for x in liste:
	liste1.append(x)
	
print("Liste1: " ,liste1)	
	

# Şimdi List Comprehension Yöntemi ile yapalım


liste2 = [1,2,3,4,5,6]
liste3 = [x for x in liste2]    #List Comprehension Yöntemi Bu şekildedir
print("Liste3: ",liste3)


liste4 = [(1,2),(3,4),(5,6)]
liste5 = [(x,y) for x,y in liste4]   
print("Liste5: ",liste5)

liste6 = [x*y for x,y in liste4]   
print("Liste6: ",liste6)

s = "PYTHON"
liste7 = [x*3 for x in s]
print("Liste7: ", liste7)


liste8 = [(1,2,3),(4,5,6,7,8),(9,10,11,12,13)]     # Normal Yolla
liste9 = list()

for x in liste8:
	for y in x:
		liste9.append(y)
		
print("Liste9: ",liste9)




liste10 = [(1,2,3),(4,5,6,7,8),(9,10,11,12,13)]     #List Comprehension Yöntemi ile
liste11 = [x for y in liste10 for x in y] 
print("Liste11: ",liste11)









