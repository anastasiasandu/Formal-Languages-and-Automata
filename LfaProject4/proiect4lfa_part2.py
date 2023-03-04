import re
import requests
from bs4 import BeautifulSoup

titluri=[]
linkuri=[]
def web(WebUrl):
          url = WebUrl
          code = requests.get(url)
          plain = code.text
          s = BeautifulSoup(plain, "html.parser")
          for link in s.findAll('a'):
               cuv="https://www.olx.ro"
               tet_2 = link.get('href')
               if tet_2!=None and re.search("/d/oferta/",tet_2):
                    cuv=cuv+tet_2
                    print(cuv)
                    titluri.append(tet_2)
                    linkuri.append(cuv)
web('https://www.olx.ro/d/anunturi-agricole/?currency=RON&search%5Bdescription%5D=1')

descrieri=[]
def web2(WebUrl):
     url = WebUrl
     code = requests.get(url)
     plain = code.text
     s = BeautifulSoup(plain, "html.parser")
     for descriere in s.findAll('div', class_="css-g5mtbi-Text"):
          descrieri.append(descriere)

#for cuv in cuvinte:
#     web2(cuv)

for i in range(3):
     web2(linkuri[i])

preturi=[]
def web3(WebUrl):
    url = WebUrl
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    for pret in s.findAll('h3', class_="css-okktvh-Text eu5v0x0"):
        preturi.append(pret)

for i in range(3):
     web3(linkuri[i])

for i in range(3):
    # titluri[i].replace('-',' ') # ???
    print("Titlu:")
    print(titluri[i])
    print("Descrieri:")
    print(descrieri[i])
    print("Pret:")
    print(preturi[i])

"""
print(re.search("/(?<=>)\d{10}(?=<)/", preturi[i])) #??? de ex: >300<
"""
