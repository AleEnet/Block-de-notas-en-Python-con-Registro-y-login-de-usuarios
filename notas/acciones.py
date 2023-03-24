from notas.nota import Nota as Nota_modelo



class Acciones:
    def crear(self, usuario):
        print(f"{usuario[1]}, se creara la siguiente nota: ")
        
        titulo = input("Titulo de la nota: ")
        descripcion = input("Detalles de la nota: ")

        nota = Nota_modelo(usuario[0], titulo, descripcion)

        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Se guardo la nota {nota.titulo} exitosamente!")
        else:
            print(f"Existen errores ingresados para la creación de la nota {nota.titulo}")
        
    def mostrar (self,usuario):
        print(f"{usuario[1]}, las notas que tienes guardadas son: ")
        nota = Nota_modelo(usuario[0])
        lista_notas = nota.lista()
        
        for i in lista_notas:
            print(f"\nTitulo: {i[2]}        ||      Fecha:{i[4]}")
            print("---------------------------------------")
            print(f"\nDescripcion: {i[3]}")

    def elminar (self, usuario):
        nota = Nota_modelo(usuario[0])
        lista_notas = nota.lista()
        print("\nSelecciona de la lista de tus notas la que deseas eliminar: ")
        
        for i in lista_notas:
            print(f"\n Titulo:{i[2]}       ||    Fecha:{i[4]}")
            print("-------------------------------------")
        
        titulo = input("Ingresa el titulo de la nota que deseas eliminar: )")
        nota_eliminar = Nota_modelo(usuario[0],titulo)
        
        resultado = nota_eliminar.borrar()

        if resultado[0] >= 1:
            print("La nota fue eliminada exitosamente!")
        else:
            print("El id ingresado es incorrecto o no corresponde a alguna de tus notas guardadas.")

       