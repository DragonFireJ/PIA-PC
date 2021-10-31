import socket
import argparse


def escaneo_ports(ip, port_in, port_fin):
    for port in range(port_in, port_fin):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print("Puerto abierto", port)
        else:
            print("Puerto no abierto", port)
        s.close()
