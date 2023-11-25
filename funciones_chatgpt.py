import random
import yagmail

# Mensajes de bienvenida para el cuerpo del correo
mensajes_bienvenida = [
    "¡Bienvenido a nuestro servicio!",
    "Saludos y bienvenido a bordo.",
    "Hola, nos alegra verte aquí.",
    "Te damos la bienvenida con gusto.",
    "¡Hola y bienvenido a la comunidad!",
]

# Mensajes de bienvenida para el asunto del correo
mensajes_bienvenida_asunto = [
    "¡Bienvenido a bordo!",
    "Hola y bienvenido.",
    "Te damos la bienvenida.",
    "¡Bienvenido a la familia!",
    "¡Bienvenido a la comunidad!",
]

# Mensajes de despedida para el cuerpo del correo
mensajes_despedida_cuerpo = [
    "Gracias por ser parte de nosotros.",
    "Esperamos verte pronto de nuevo.",
    "Hasta la próxima, ¡cuídate!",
    "Si necesitas ayuda, estamos aquí.",
    "¡Adiós y que tengas un gran día!",
]

# Mensajes de despedida para el asunto del correo
mensajes_despedida_asunto = [
    "Hasta pronto",
    "Gracias por tu visita",
    "¡Nos vemos pronto!",
    "¡Adiós por ahora!",
    "Cuídate mucho",
]


# Función para formar y enviar correos de bienvenida de las listas
def enviar_mail_bienvenida(mail, contrasena, destinatario):
    yag = yagmail.SMTP(mail, contrasena)

    asunto_bienvenida = random.choice(mensajes_bienvenida_asunto)
    cuerpo_bienvenida = random.choice(mensajes_bienvenida)

    yag.send(destinatario, asunto_bienvenida, cuerpo_bienvenida)

    yag.close()


# Función para formar y enviar correos de despedida de las listas
def enviar_mail_despedida(mail, contrasena, destinatario):
    yag = yagmail.SMTP(mail, contrasena)

    asunto_despedida = random.choice(mensajes_despedida_asunto)
    cuerpo_despedida = random.choice(mensajes_despedida_cuerpo)

    yag.send(destinatario, asunto_despedida, cuerpo_despedida)

    yag.close()


# Funcionalidad para enviar correos
print("****************")
print("ENVÍO DE CORREOS")
print("****************")

mail = input("Ingresa tu correo: ")
contrasena = input("Ingresa tu contraseña: ")
destinatario = input("Ingresa el correo del destinatario: ")

print("Ingresa 1 si deseas enviar un correo de bienvenida")
print("Ingresa 2 si deseas enviar un correo de despedida")
opcion = int(input("Ingresa una opción: "))
print("Enviando correo...")

if opcion == 1:
    enviar_mail_bienvenida(mail, contrasena, destinatario)
    print("Correo de bienvenida enviado")
elif opcion == 2:
    enviar_mail_despedida(mail, contrasena, destinatario)
    print("Correo de despedida enviado")
else:
    print("Ingresa una opción correcta")
