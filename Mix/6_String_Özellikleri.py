# -*- coding: utf-8 -*-

""" String uzunluğunu ' len() ' fonk. sayesinde bulabiliyoruz

   NOOOOT : Bİr Stringin herhangi bir indexindeki 
                karekteri keyfiize göre değiştiremeyiz  
     
      Example:  String = 'Engin'   String[0]=e yapmak istersek ERROR alırız
       
"""

String = ' End of the world is coming soon '  #string uzunluğu boşluklar hesaplanarak bulunur ' 33 '    
print(len(String))   #  len(String) = 33 


a='Python '
b="Programlama "
c="""Dili"""
print(a+b+c)    # Stringlerin Toplma Özelliği

s='Caming Soon '
print(s*3)      # Üç kere Caming Soon yazdırıyor

e='Engin '
e=e+ 'GÜLTEKİN'

print(e)
             
