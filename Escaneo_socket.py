import socket
import argparse

def escaneo_ports(ip, port_in, port_fin):
    # Vamos a ir de puerto en puerto
    for port in range(port_in, port_fin):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Intentamos establecer conexion
        result = s.connect_ex((ip, port))
        # Si el resultado es 0 el puerto esta abierto
        if result == 0:
            print("Puerto abierto", port)
        else:
            print("Puerto no abierto", port)
        # Cerramos la conexión
        s.close()
