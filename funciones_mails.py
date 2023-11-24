import yagmail

# Funcion para leer el archivo de credenciales y asignarlos a mail y contrasena    
def usuario_contrasena(ruta):
    with open(ruta, 'r') as credenciales:
        mail = credenciales.readline().strip()
        contrasena = credenciales.readline().strip()
    return mail, contrasena

# Funcion para enviar el mail
def enviar_mail(mail, contrasena, asunto, mensaje, destinatarios):
    yag = yagmail.SMTP(mail, contrasena)
    yag.send(to=destinatarios, subject=asunto, contents=mensaje)
    yag.close()