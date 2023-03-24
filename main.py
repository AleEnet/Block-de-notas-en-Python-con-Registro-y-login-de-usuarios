"""
Proyecto python MySQL

El pryecto consiste en crear una aplicacion
que sirva para guardar notas de diferentes usuarios:
* Abrir asistente
* Login o registro
* Si elegimos registro, crear un usuario en la DB
* Si elegimos Login, identificar al usuario y preguntar acciones
* Crear, mostraar y eliminar notas

"""

from usuarios import acciones


hacer = acciones.Acciones()

print(""" Acciones disponibles: 
    * Registro (r)
    * Login (l)
""")

accion = input("¿Que desea hacer?:")

if accion == "r":
    hacer.registro()
    
elif accion == "l":
    hacer.login()