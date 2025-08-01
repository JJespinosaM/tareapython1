from datetime import datetime
import os

# Listas para almacenar amigos, libros y préstamos
amigos = []
libros = []
prestamos = []

# Función para registrar un nuevo amigo
def registrar_amigo():
    amigos.append(input("Nombre del amigo: "))

# Función para registrar un nuevo libro
def registrar_libro():
    libros.append({"titulo": input("Título del libro: "), "disponible": True})

# Función para mostrar la lista de amigos
def ver_amigos():
    for i, n in enumerate(amigos, 1):
        print(f"{i}. {n}")

# Función para mostrar la lista de libros y su estado
def ver_libros():
    for i, l in enumerate(libros, 1):
        print(f"{i}. {l['titulo']} - {'Disponible' if l['disponible'] else 'Prestado'}")

# Función para prestar un libro a un amigo
def prestar_libro():
    ver_amigos()  # Mostrar amigos para elegir
    try:
        id_amigo = int(input("ID amigo: ")) - 1  # Seleccionar amigo
        ver_libros()  # Mostrar libros para elegir
        id_libro = int(input("ID libro: ")) - 1  # Seleccionar libro
        # Si el libro está disponible, se presta
        if libros[id_libro]["disponible"]:
            prestamos.append((id_amigo, id_libro))  # Guardar el préstamo
            libros[id_libro]["disponible"] = False  # Marcar libro como prestado
            print("Préstamo realizado.")
        else:
            print("Libro no disponible.")
    except:
        print("Opción inválida.")

# Función para devolver un libro prestado
def devolver_libro():
    # Mostrar solo los préstamos activos (libros no disponibles)
    for i, (id_amigo, id_libro) in enumerate(prestamos, 1):
        if not libros[id_libro]["disponible"]:
            print(f"{i}. Libro {libros[id_libro]['titulo']} a {amigos[id_amigo]}")
    try:
        idx = int(input("Número de préstamo a devolver: ")) - 1  # Seleccionar préstamo
        id_amigo, id_libro = prestamos[idx]
        libros[id_libro]["disponible"] = True  # Marcar libro como disponible
        print("Libro devuelto.")
    except:
        print("Opción inválida.")

# Menú principal del programa
def menu():
    while True:
        print("\n1. Registrar amigo\n2. Registrar libro\n3. Ver amigos\n4. Ver libros\n5. Prestar libro\n6. Devolver libro\n7. Salir")
        op = input("Opción: ")
        if op == "1": registrar_amigo()
        elif op == "2": registrar_libro()
        elif op == "3": ver_amigos()
        elif op == "4": ver_libros()
        elif op == "5": prestar_libro()
        elif op == "6": devolver_libro()
        elif op == "7": break  # Salir del programa

# Ejecutar el menú si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()