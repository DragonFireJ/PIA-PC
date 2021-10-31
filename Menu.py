from Escaneo_socket import escaneo_ports
from Estenografia import ocultar_texto
from Decode_esteno import leer
from Virustotal import Virustotal
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("-porti", dest="port_in", type=int, default=0)
parser.add_argument("-portf", dest="port_fin", type=int, default=100)
parser.add_argument("-api", dest="key")
parser.add_argument("-type", dest="tipo", type=int, default=0)
parser.add_argument("-txt", dest="txt", default="urls_sospechosas.txt")
parser.add_argument("-img", dest="ruta")
parser.add_argument("-msj", dest="msj")
parser.add_argument("-ip", dest="ip")
params = parser.parse_args()

logging.basicConfig(level=logging.INFO, filename='erroresPIA.log')

try:
    if params.ip is not None:
        escaneo_ports(params.ip, params.port_in, params.port_fin)
    elif params.key is not None:
        Virustotal(params.key, params.tipo, params.txt)
    elif params.ruta is not None:
        if params.msj is not None:
            print(params.ruta)
            ocultar_texto(params.msj, params.ruta, "salida.png")
        else:
            leer(params.ruta)
    else:
        print("Ponga argumentos validos")
except IOError as e:
    logging.error("Ha ocurrido un error: " + str(e))
    print("Ha ocurrido un error: " + str(e))
except KeyError as e:
    mensaje1 = "Ha ocurrido un error, al encontar una llave "
    mensaje2 = "(Puede que su clave API este mal): "
    logging.error(mensaje1 + mensaje2 + str(e))
    print(mensaje1 + mensaje2 + str(e))
