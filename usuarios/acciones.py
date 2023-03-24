from usuarios.usuario import Usuario
from notas.acciones import Acciones as Acciones_nota

class Acciones: 
    
    def registro(self):

        print("\nBien, comencemos a registrarte!")

        nombre = input("\nNombre: ")
        apellido = input ("\nApellido: ")
        email = input("\nE-mail: ")
        password = input("\nContraseña: ")

        usuario = Usuario(nombre,apellido,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Se ha registrado {registro[1].nombre} con el email {registro[1].email} correctamente!")
        else:
            print("Hubo un error en el registro de tus datos!")


        
    def login(self):
        print("Ingresa tus datos: ")
        
        email = input("\nE-mail: ")
        password = input("\nContraseña: ")

        usuario = Usuario("", "", email, password)

        login = Usuario.identificar(usuario)
        
        if login is None:
            print("Los datos ingresados no corresponden a un usuario registrado en la base de datos")
        else:
            print(f"Bienvenido {login[1]} al sistema de notas! ")
            self.proximasAcciones(login)

    def proximasAcciones(self,usuario):
        print(
            """
            Acciones disponibles:
            * Crear nota (C)
            * Leer nota (L)
            * Modificar nota (M)
            * Eliminar nota (E)
            * Salir del programa (exit)
            """
        )

        accion = input("¿Que acción desea realizar?: ")
        hazEl = Acciones_nota()

        if accion == "C":
            print("Nueva nota: ")
            hazEl.crear(usuario)
            otra_accion = input("Desea realizar otra acción? (Si/No): ")
            if otra_accion == "Si" or otra_accion == "si":
                self.proximasAcciones(usuario)
            else:
                print("Muchas gracias por utilizar la aplicación de notas")
                exit()
        elif accion == "L":
            hazEl.mostrar(usuario)
            otra_accion = input("Desea realizar otra acción? (Si/No): ")
            if otra_accion == "Si" or otra_accion == "si":
                self.proximasAcciones(usuario)
            else:
                print("Muchas gracias por utilizar la aplicación de notas")
                exit()
        elif accion == "M":
            print("Modificar nota: ")
            otra_accion = input("Desea realizar otra acción? (Si/No): ")
            if otra_accion == "Si" or otra_accion == "si":
                self.proximasAcciones(usuario)
            else:
                print("Muchas gracias por utilizar la aplicación de notas")
                exit()
        elif accion == "E":
            hazEl.elminar(usuario)

            otra_accion = input("Desea realizar otra acción? (Si/No): ")
            if otra_accion == "Si" or otra_accion == "si":
                self.proximasAcciones(usuario)
            else:
                print("Muchas gracias por utilizar la aplicación de notas")
                exit()
        elif accion == "exit":
            print("Muchas gracias por utilizar la aplicación de notas")
            exit()
        


        