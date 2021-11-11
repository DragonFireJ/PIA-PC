# PIA-PC

_Este proyecto fue realizado con la intencion de cumplir con la tarea asignada por la maestra Perla Marlene Viera Gonzalez, y es una serie de programas
creados en python con funcionalidades para la carrera de LSTI. Se compone de alrededor de 8 programas funcionales, para que podamos realizar ciertas
tareas relacionadas con la seguridad de la inforamcion de manera mas sencilla_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


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

---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
