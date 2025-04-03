from Clase_libros import Libro, normalizar_texto

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)

lista_libros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]

while True:
    print("""
        Que desea hacer?
          1. Ingresar un libro
          2. Buscar libro por genero
          3. Recomendar libro
          4. Ver libros cargados
          5. Salir                      
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
        genero_busqueda = input("Que genero desea buscar?: ")
        libros_en_genero = []
        for libro in lista_libros:
            if normalizar_texto(libro.genero) == normalizar_texto(genero_busqueda):
                libros_en_genero.append(libro)
        if libros_en_genero:
            print(f"Los libros que pertenecen a la categoria {genero_busqueda} son:")
            for libro in libros_en_genero:
                print(f"{libro.titulo} de: {libro.autor}")
        else:
            print("no hay libros en ese genero")

    elif opcion == "3": #recomendar libro
        genero_busqueda = input("Que genero desea buscar?: ")
        libros_en_genero = []
        for libro in lista_libros:
            if normalizar_texto(libro.genero) == normalizar_texto(genero_busqueda):
                libros_en_genero.append(libro)
        if libros_en_genero:
            mejor_libro = max(libros_en_genero, key=lambda libro:libro.puntuacion)
            print (f"Recomendamos el libro: {mejor_libro.titulo} con una puntuacion de: {mejor_libro.puntuacion}")
        

    elif opcion == "4": #ver todos los libros
        if lista_libros:
            for libro in lista_libros:
                print(libro)
        else:
            print("No hay libros ingresados.")

    elif opcion == "5": #salir del programa
        break

    else: #no se ingreso una opcion valida
        print("ingrese una opcion valida")
    