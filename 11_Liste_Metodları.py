# -*- coding: utf-8 -*-

# 3-Temel Liste Metodları ve İşlemleri
"""Bu kısımda da listelerde yapabileceğimiz temel işlemleri ve bazı temel metodları öğreneceğiz. 
       Listelerin daha bir çok metodunu kursun ileriki kısımlarında görüyor olacağız.
"""

#Bir listeyi birbirine toplama işlemini stringlerdeki gibi yapabiliriz.

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = liste1 + liste2
print(liste3)

liste3 = liste3 + ["ENGİN"]
print(liste3)

liste3[0] = 10   #Listelerde istediğimiz indexi değiştirebiliriz ama bunu stringlerde yapamıyorduk  
print(liste3)
liste3[2] = "GÜLTEKİN"   #Ayrca type farketmeksizin değiştirebiliriz
print(liste3) 
          
liste3[:3] = [1,"BEN",3]   #*********** Buda Efsane Bir Özellik ************* 
print(liste3,"\n")    

#Bir listeyi bir tamsayıyla da çarpabiliriz.
print(liste1)
print(liste1*3)   #Bu ifade listeyi üç kez yazması için ama listeyi bidaha yazdırdığımızda eski haline dönecektir
print(liste1)       #Bunun sebebi atama yapmadığımız için 

liste1 = liste1 *3   #Bu şekilde atama yaptığımız zaman bidaha bastırdığımızda istediğimizi vercektir
print(liste1,"\n")

print(liste2*-2)    #Eksi bir sayı ile çarptuğımızda liste boş oluyor
print(liste1*0)      #Aynı şey 0 içinde geçerli 

""" Şuana kadar listeleri 
       Toplamayı
        Değiştirmeyi 
         Bir sayı ile Çarpmayı gördük 
    12.kodun içerisinde burda gösteremediğimiz Metodları göstereceğiz İYİ ÇALIŞMALAR
"""         















 
  
