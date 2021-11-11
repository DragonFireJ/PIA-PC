import os


def descifrado_cesar(message, clave):
    key = int(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    return translated

def cifrado_cesar(message, clave):
    key = int(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    return translated


def encriptar_txt(txt, clave):
    y = open(txt, "r")
    lin = y.readlines()
    y.close()
    y = open(f"encriptado_{txt}", "w")
    for i in lin:
        y.write(cifrado_cesar(i, clave))
    y.close()
    print("Mensaje encriptado")


def desencriptar_txt(txt, clave):
    y = open(txt, "r")
    lin = y.readlines()
    y.close()
    y = open(f"desencriptado_{txt}", "w")
    for i in lin:
        y.write(descifrado_cesar(i, clave))
    y.close()
    print("Mensaje desencriptado")
