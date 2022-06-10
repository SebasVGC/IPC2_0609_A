from xml.dom import minidom
import xml.etree.ElementTree as ET

def todos():
    doc=minidom.parse('data.xml')
    discos = doc.getElementsByTagName("cd")
    for cd in discos:
        title = cd.getElementsByTagName("title")[0]
        artist = cd.getElementsByTagName("artist")[0]
        price = cd.getElementsByTagName("price")[0]
        year = cd.getElementsByTagName("year")[0]
        print(title.firstChild.data)
        print(artist.firstChild.data)
        print(year.firstChild.data)
        print(price.firstChild.data)

tree= ET.parse('data.xml')
root=tree.getroot()

#Buscar los libros del año 1996
def buscar():
    resultado=root.findall('./cd')
    for elemento in resultado:
        x=elemento.findall("year")[0].text
        if (x=="1996"):
            print(elemento.findall("title")[0].text)
            print(elemento.findall("artist")[0].text)
            print(elemento.findall("year")[0].text)
            print(elemento.findall("price")[0].text)
            print("----------")

def buscar2():
    year_=input("ingrese year: ")
    resultado=root.findall('./cd')
    for elemento in resultado:
        x=elemento.findall("year")[0].text
        if (x==year_):
            print(elemento.findall("title")[0].text)
            print(elemento.findall("artist")[0].text)
            print(elemento.findall("year")[0].text)
            print(elemento.findall("price")[0].text)
            print("----------")

def buscar3():
    artista_=input("ingrese artista: ")
    resultado=root.findall('./cd')
    for elemento in resultado:
        x=elemento.findall("artist")[0].text
        if (x==artista_):
            print(elemento.findall("title")[0].text)
            print(elemento.findall("artist")[0].text)
            print(elemento.findall("year")[0].text)
            print(elemento.findall("price")[0].text)
            print("----------")

buscar3()