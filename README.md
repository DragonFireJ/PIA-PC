# PIA-PC

_Este proyecto fue realizado con la intencion de cumplir con la tarea asignada por la maestra Perla Marlene Viera Gonzalez, y es una serie de programas
creados en python con funcionalidades para la carrera de LSTI. Se compone de alrededor de 8 programas funcionales, para que podamos realizar ciertas
tareas relacionadas con la seguridad de la inforamcion de manera mas sencilla_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

_Aplicaciones necesarias:_

-Necesitaras instalar Python [Descarga](https://www.python.org/downloads/)

-Necesitaras instalar PIP

-Para usar el modulo de PS tendras que tener PowerShell en tu computadora

-Tener una API de [VirusTotal](https://www.virustotal.com/gui/)


### Instalación 🔧

_Descarga todos los archivos y colocalos en una carpeta_

-Da click en code

-Da click en donwload zip

-Descomprome el archivo en una carpeta

_Ahora instala los modulos necesario_


```
Abre la terminal de tu pc y escribe
-pip install -r requirements.txt
```

_Ya estas listo para usarlo_

## ¿Como usarlo? ⚙️

_Este script funciona con argparse, por lo que tendras que pasar los argumentos_

* Analisis de puertos
  - Flags para el analisis de puertos
  ```
  -porti
  -portf
  -ip
  ```
   -porti
   
      Se pondra la flag seguida del puerto inicial, se tiene por defecto el puerto 0, por lo que se puede omitir.
      
      -porti 5
    
    -porf
    
      Se pondra la flag seguida del puerto final, se tiene por defecto el puerto 100, por lo que se puede omitir.
      
      -portf 10 
    
    -ip
    
      Se pondra la direccion IP, a la que se le quiere hacer el escaneo de puertos
      
      -ip 127.0.01
    
   - Forma de ejecucion
    ```
    python Menu.py -porti 0 -portf 100 -ip '127.0.0.1'
    ```
    
* API VirusTotal
  - Flags para el uso de la API VirusTotal
  ```
  -api
  -type
  ```
   -api
   
      Se pondra la flag seguida de tu API de VirusTotal.
      
      -api 'ABCDEFGHI000000000000'
    
    -type
    
      Se pondra la flag seguida del tipo de API que tienes, 0=Gratis, 1=Premium, recuerda que esta por defecto
      en 0 por lo que puede ser opcional ponerlo.
      
      -type 0
    
   - Forma de ejecucion
    ```
    python Menu.py -api 'ABCDEFGHI000000000000' -type 1
    ```
* Estenografia
  - Flags para hacer uso de estenografia
  ```
  -img
  -reimg
  -msj
  ```
   -img
   
      Se pondra la flag seguida de la ruta o bien el nombre de la imagen (si se encuentra en el mismo directorio) a la que 
      se le quiere añadir un mensaje oculto o bien la que contiene el mensaje oculto (Si se quiere desencriptar).
      
      -img 'C:\Users\Documents\Ejemplo.jpg'
    
    -reimg
    
      Se pondra la flag seguida del nombre o ruta de la imagen que tendra como resultado la imagen con el mensaje encriptado,
      recuerda usar la extension ".png". Puede ser opcional pues viene con un valor default que es "Salida.png".
      
      -reimg 'Salida.png'
    
    -msj
    
      Se pondra la flag seguida del mensaje, que se esconder dentro de la imagen.
      
      -msj 'Hola soy un mensaje en la imagen'
    
   - Forma de ejecucion para esconder un mensaje
    ```
    python Menu.py -img 'C:\Users\Documents\Ejemplo.jpg' -msj 'Hola soy un mensaje en la imagen' -reimg hola.png
    ```
    
   - Forma de ejecucion para encontrar un mensaje en una imagen
    ```
    python Menu.py -img 'C:\Users\Documents\Ejemplo.png'
    ```

* KeyLogger
  - Flags para el uso del keylogger
  ```
  -klogger
  -mail
  -pwd
  ```
   -klogger
   
      Se pondra la flag seguida de la cantidad en segundos que quieres que se ejecute el keylogger.
      
      -klogger 3600
    
    -mail
    
      Se pondra la flag seguida del correo electronico que se estara usando para enviar el correo con el reporte del keylogger 
      ademas tambien servira para recibir este reporte. Recuerda que tiene que ser una cuenta de Gmail
      
      -mail 'ejemplo@gmail.com'
    
    -pwd
    
      Se pondra la flag seguida por la contraseña del correo electronico que se usara para enviar y recibir el reporte. 
      Recuerda que tiene que ser una cuenta de Gmail.
      
      -pwd 'Password1'
    
   - Forma de ejecucion
    ```
    python Menu.py -klogger 3600 -mail 'ejemplo@gmail.com' -pwd 'Password1'
    ```
* Copeado de USB (Se necesita tener conectada la USB)
  - Flags para el copeado de una usb a la pc
  ```
  -usb
  -rescop
  -temcop
  ```
   -usb
   
      Se pondra la flag seguida de la letra "A" para activar este modo.
      
      -usb A
    
    -rescop
    
      Se pondra la flag seguida de la ruta donde se guaradaran los archivos (Backup) de la memoria usb, es opcional si 
      la copia se quiere guardar en el directorio donde esta el script, puesto que la guara en el directorio actual.
      
      -rescop 'C:\Users\Documents'
    
    -temcop
    
      Se pondra la flag seguida de una direccion donde se ejecutara temporalmente el comando, esta flag puede ser opcional
      pues tiene un valor por default y es practicamente indifirente se haga esta ejecucion temporal
      
      -temcop 'C:\Users\Documents\tmp'
    
   - Forma de ejecucion
    ```
    python Menu.py -usb A -rescop 'C:\Users\Documents' -tempcop 'C:\Users\Documents\tmp'
    ```

* Atacar una carpeta con Ransomware
  - Flags para el ataque con Ransomware
  ```
  -ataque
  ```
   -ataque
   
      Se pondra la carpeta que sea ser atacada con Ransomware
      
      -ataque 'C:\Users\Documents'
    
   - Forma de ejecucion
    ```
    python Menu.py -ataque 'C:\Users\Documents'
    ```
    
   - Nota importante: 

      Se generara un archivo llamado key.key, guardarlo antes de ejecutar otra vez el programa
      pues se podra perder la informacion ya que cada key que se genera es diferente, por lo que son
      necesarias para recuperar el archivo, la recomendacion es tomar una copia y guardarla.
    
* Rescate de archivos encriptados con Ransomware
  - Flags para el rescate de Ransomware
  ```
  -resc
  -resckey
  ```
   -resc
   
      Se pondra la flag seguida de la carpeta que esta infectada con Ransomware (Generado por este programa), que se quiera rescatar
      
      -resc 'C:\Users\Documents'
    
    -resckey
    
      Se pondra la flag seguida de la ruta donde esta el archivo key.key para desencriptar la carpeta, este sera ocpional si
      la carpeta se encuentra dentro de la misma carpeta de ejecucion del script. Si se ejecuta en pruebas, y el archivo key.key
      se encuentra en pruebas no sera necesaria la flag, pues la buscara en el directorio actual
      
      -reskey 'C:\Users\Documents\key.key'
    
   - Forma de ejecucion
    ```
    python Menu.py -resc 'C:\Users\Documents' -reskey 'C:\Users\Documents\key.key'
    ```
* Encripatacion de un txt con Caesar.
  - Flags para el encriptado con Caesar
  ```
  -tarces
  -clave
  ```
   -tarces
   
      Se pondra la flag seguida de la ruta con el txt y el nombre de este, que se desea encriptar.
      
      -tarces 'C:\Users\Documents\cesar.txt'
    
    -clabe
    
      Se pondra la flag seguida de el numero que se desea desplazar a la hora de usar Caesar.
      
      -clave 5

   - Forma de ejecucion
    ```
    python Menu.py -tarces 'C:\Users\Documents\cesar.txt' -clave 5
    ```
   - Nota importante:
      
     Se usa el siguiente alfabeto: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
     
* Dsencripatacion de un txt con Caesar.
  - Flags para el desencriptado con Caesar
  ```
  -desces
  -clave
  ```
   -desces
   
      Se pondra la flag seguida de la ruta con el txt y el nombre que se desea desencriptar.
      
      -tarces 'C:\Users\Documents\cesar.txt'
    
    -clabe
    
      Se pondra la flag seguida de el numero que se desea desplazar a la hora de usar Caesar.
      
      -clave 5

   - Forma de ejecucion
    ```
    python Menu.py -desces 'C:\Users\Documents\cesar.txt' -clave 5
    ```
   - Nota importante:
      
     Se usa el siguiente alfabeto: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
     
    
## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Python](https://www.python.org/) - Lenguage utilizado
* [PowerShell](https://docs.microsoft.com/en-us/powershell/) - Lenguaje auxiliar

## Autores ✒️

_Equipo conformado por:_

* **Jairo Santana García** -  [DragonFireJ](https://github.com/DragonFireJ)
* **Pablo de Jesus García Medina** -  [pxblo1325](https://github.com/pxblo1325)
* **Jose Pablo Perez Hernandez** -  [Nadrod](https://github.com/nadrod)
* **Luís Roberto Díaz Pineda** -  [R0bert0DP](https://github.com/R0bert0DP)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia del equipo conformado por Jairo Santana García, Pablo de Jesus García Medina, Jose Pablo Perez Hernandez y Luís Roberto Díaz Pineda

## Expresiones de Gratitud 🎁

* Gracias a la profesora Perla por las clases impartidas 📢
* Gracias al apoyo del profesor Osvaldo para la solucion de algunos detalles menores. 
* Gracias a las paginas de las cuales tomamos referencias como [Parzibytes's blog](https://parzibyte.me/blog/)
---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
