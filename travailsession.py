# coding: utf-8 

import csv 
from bs4 import BeautifulSoup
import requests
import time 
import datetime

url1= "http://meteo.gc.ca/airquality/pages/"
url2= "_f.html"

code = {
    "Calgary" : "abaq-002",
    "Charlottetown" : "peaq-003",
    "Edmontnon" : "abaq-001",
    "Fredericton" : "nbaq-002",
    "Halifax" : "nsaq-001",
    "Montréal" : "qcaq-001",
    "Saskatoon" : "skaq-002",
    "Toronto" : "onaq-001",
    "Vancouver" : "bcaq-001",
    "Winnipeg" : "mbaq-001"
}

now= datetime.datetime.now()

jour=now.day
mois=time.strftime("%b")
annee=now.year
heure=time.strftime("%Hh%M")

#print("\n")
#print("#"*50)
#print("Nous sommes le {0} {1} {2}".format(jour, mois, annee))
#print("Il est {O}\n".format(heure))

bob= []

entetes= {
    "User-Agent": "Maxime Bernier - Pour s'intéresser sur la santé des Canadiens",
    "From": "max_bernier@hotmail.com"
}

for ville, code in code.items(): 
    
    url = "{}{}{}".format(url1,code,url2)
    print("L'URL pour {} est {}".format,(ville,url))

    x = requests.get(url,headers=entetes,verify=False)

    page=BeautifulSoup(x.text,"html.parser")
    
    if page.find("p",class_="withBorder"):
        air= page.find("p",class_="withBorder").text
        air=air[0]
        print(air)
    else:
        print("ya pas d'air icitte")
    
    
    
# print("La qualité de l'air est {} en ce moment à {}".format(air,ville))


    
    air=float(air)

    bob.append(air)

    if min(bob) == air:
        villeMin = ville
    if max(bob) == air:  
        villeMax = ville
        
    valMin = min(bob)
        
    valMax = max(bob)
   
    print("\n")
    print("#"*50)

# valMin = str(min(bob))
# valMin = str.replace(valMin,".",",")
# bob.remove(min(bob))

# valMax = str(max(bob))
# valMax = str.replace(valMax,".",",")
# bob.remove(max(bob))

bissonnette = str(round(sum(bob),1))
# bissonnette = str.replace(bissonnette,".",",")    

tweet = "C'est à {1} où la qualité de l'air est la pire ({0}) \n\n C'est à {3} où la qualité de l'air est la meilleure ({2})".format(valMin,villeMin,valMax,villeMax)
print(tweet)
print("\nLe tweet fait {} caractères\n".format(len(tweet)))
    
    
