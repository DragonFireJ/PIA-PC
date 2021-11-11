from PIL import Image
import math  # Utilizado sólo para redondear hacia abajo


def mod_color(color_original, bit):
    # Modificamos el color con el un nuevo bit
    color_binario = bin(color_original)[2:].zfill(8)
    color_modificado = color_binario[:-1] + str(bit)
    # Regresamos el color modificado
    return int(color_modificado, 2)


def lista_bits(texto):
    # Definicimos la cadena con la cual vamos a indicar que hasta ahi llega nuestro mensaje
    terminacion = [1, 1, 1, 1, 1, 1, 1, 1]
    lista = []
    for letra in texto:
        # Buscamos sus valores en ASCII y binario
        bus_ascii = ord(letra)
        binario = bin(bus_ascii)[2:].zfill(8)
        for bit in binario:
            # Agregamos los elementos binarios a la lista
            lista.append(bit)
    for bit in terminacion:
        # Cuando hayamos terminado de escribir el mensaje en lista agregamos la cadena de terminacion
        lista.append(bit)
    return lista


def ocultar_texto(msj, ruta, salida):
    print(f"Ocultando mensaje: {msj}")
    # Abrimos la imagen
    imag = Image.open(ruta)
    pix = imag.load()

    # Obtenemos el tamaño de la imagen
    tam = imag.size
    anch = tam[0]
    alt = tam[1]

    # Convertimos el mensaje a bits
    lista = lista_bits(msj)
    cont = 0
    long = len(lista)
    # Comenzamos con la ocultacion del mensaje
    for x in range(anch):
        for y in range(alt):
            if cont < long:
                # Vamos a asignar el ancho a x, el alto a y
                pixel = pix[x, y]

                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]

                # Modificamos un poco la imagen y agregamos el mensaje
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

    # Si se termian correctamente se lanza este mensaje
    if cont >= long:
        print("Mensaje escrito correctamente")
    # Si algo fallo se ejecuta este mensaje.
    else:
        sobra = math.floor((long - cont) / 8)
        print(f"Advertencia: no se pudo escribir todo el mensaje, sobraron {sobra} caracteres")
    # Se guarda la imagen.
    imag.save(salida)

