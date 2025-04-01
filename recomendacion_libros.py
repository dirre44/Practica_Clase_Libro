from Clase_libros import Libro

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)

lista_libros = []

while True:
    print("""
        Que desea hacer?
          1. Ingresar un libro
          2. Buscar libro por genero
          3. Recomendar libro
          4. Salir                      
    """)
    opcion = input("Ingrese una opcion: ")

    if opcion == "1": #ingresar libro
        print("ingrese los siguientes datos para agregar un libro:")
        titulo = input("Titulo:")
        autor = input("Autor:")
        genero = input("Genero:")
        puntaje = float(input("Puntaje (en numero):"))
        libro_nuevo = Libro(titulo, autor, genero, puntaje)
        lista_libros.append(libro_nuevo)
        print(f"El libro {libro_nuevo.titulo} fue ingresado correctamente")
    
    elif opcion == "2": #buscar por genero
        pass

    elif opcion == "3": #recomendar libro
        pass

    elif opcion == "4": #salir del programa
        break

    else: #no se ingreso una opcion valida
        print("ingrese una opcion valida")
    