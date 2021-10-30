from PIL import Image
import math  # Utilizado sólo para redondear hacia abajo


def mod_color(color_original, bit):
    color_binario = bin(color_original)[2:].zfill(8)
    color_modificado = color_binario[:-1] + str(bit)
    return int(color_modificado, 2)


def lista_bits(texto):
    terminacion = [1, 1, 1, 1, 1, 1, 1, 1]
    lista = []
    for letra in texto:
        bus_ascii = ord(letra)
        binario = bin(bus_ascii)[2:].zfill(8)
        for bit in binario:
            lista.append(bit)
    for bit in terminacion:
        lista.append(bit)
    return lista


def ocultar_texto(msj, ruta, salida):
    print(f"Ocultando mensaje: {msj}")

    imag = Image.open(ruta)
    pix = imag.load()

    tam = imag.size
    anch = tam[0]
    alt = tam[1]

    lista = lista_bits(msj)
    cont = 0
    long = len(lista)
    for x in range(anch):
        for y in range(alt):
            if cont < long:
                pixel = pix[x, y]

                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]

                if cont < long:
                    red_mod = mod_color(red, lista[cont])
                    cont += 1
                else:
                    red_mod = red

                if cont < long:
                    green_mod = mod_color(green, lista[cont])
                    cont += 1
                else:
                    green_mod = green

                if cont < long:
                    azul_modificado = mod_color(blue, lista[cont])
                    cont += 1
                else:
                    azul_modificado = blue

                pix[x, y] = (red_mod, green_mod, azul_modificado)
            else:
                break
        else:
            continue
        break

    if cont >= long:
        print("Mensaje escrito correctamente")
    else:
        sobra = math.floor((long - cont) / 8)
        print(f"Advertencia: no se pudo escribir todo el mensaje, sobraron {sobra} caracteres")
    imag.save(salida)

