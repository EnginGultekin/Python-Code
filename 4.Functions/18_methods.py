# Function

# Methods

"""
### Metod nedir ?

Şimdiye kadar Pythonda kullanabildiğimiz bir çok veri tipi gördük ve bazı
veri tipleri üzerinde bu veri tiplerinin metodlarını kullandık. Aslında bu
veritiplerin oluşturulan her bir değişken Pythonda **obje( object)** olarak
düşünülür ve Python geliştiricileri bu objelere birçok metod tanımlamıştır.
Peki nedir bu metodlar ?

**Metodlar**  bir obje üzerinde belli işlemleri gerçekleştiren  objelere
özgü fonksiyonlardır ve objelerin üzerinde metodlar şu şekilde kullanılır.

**---------------------------------------------------------------------**
    obje.herhangi_bir_metod(değerler(opsiyonel))
**---------------------------------------------------------------------**

Örneğin bir **liste objesi** oluşturduğumuz zaman bu objenin üzerinde belli
metodları uygulayabiliriz.
"""

liste = [1, 2, 3, 4, 5, 6]

liste.insert(2, "Murat")

print(liste)

liste.pop()
print(liste)

"""
Örneğin liste metodlarına  erişmek için Jupyterde **Tab** tuşuna basabiliriz. 
Ayrıca bir metodun ne iş yaptığını anlamak için **help** 
fonksiyonunu kullanabiliriz.
"""

help(liste.insert)



"""
Metodların ne anlama geldiğini **Nesne Tabanlı Programlama** kısmında 
çok daha iyi anlayacağız.
"""
