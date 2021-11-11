from cryptography.fernet import Fernet
import os


def retornarKey(rutakey): #Retornamos la key y la leemos
    return open(rutakey, "rb").read()


def decrypt(items, key): # Desencriptamos los archivos 
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read() # Lee el contenido del archivo
        data = i.decrypt(file_data)

        with open(x, "wb") as file:
            file.write(data)

def archivos(archivos, rutakey): # Definimos los archivos a desencriptar 
    items = os.listdir(archivos) # Devuelve una lista que contiene la key dado por la ruta.
    archivos_2 = [archivos+"\\"+x for x in items]
    key = retornarKey(rutakey)
    decrypt(archivos_2, key)



