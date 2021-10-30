from PIL import Image


# noinspection PyBroadException
def leer(image_path):
    terminacion = "11111111"
    # noinspection PyBroadException
    imag = Image.open(image_path)
    pix = imag.load()

    tam = imag.size
    anch = tam[0]
    alt = tam[1]

    byte = ""
    mensaje = ""

    for x in range(anch):
        for y in range(alt):
            pixel = pix[x, y]

            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            byte += (bin(red)[2:].zfill(8))[-1]
            if len(byte) >= 8:
                if byte == terminacion:
                    break
                mensaje += chr(int(byte, 2))
                byte = ""

            byte += (bin(green)[2:].zfill(8))[-1]
            if len(byte) >= 8:
                if byte == terminacion:
                    break
                mensaje += chr(int(byte, 2))
                byte = ""

            byte += (bin(blue)[2:].zfill(8))[-1]
            if len(byte) >= 8:
                if byte == terminacion:
                    break
                mensaje += chr(int(byte, 2))
                byte = ""

        else:
            continue
        break
    print("El mensaje oculto es:")
    print(mensaje)