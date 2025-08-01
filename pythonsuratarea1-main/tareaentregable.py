from datetime import datetime
import os

# Listas para almacenar amigos, libros y préstamos
amigos = []
libros = []
prestamos = []

# Función para registrar un nuevo amigo
def registrar_amigo():
    amigos.append(input("Nombre del amigo: "))


def registrar_libro():
    libros.append({"titulo": input("Título del libro: "), "disponible": True})


def ver_amigos():
    for i, n in enumerate(amigos, 1):
        print(f"{i}. {n}")


def ver_libros():
    for i, l in enumerate(libros, 1):
        print(f"{i}. {l['titulo']} - {'Disponible' if l['disponible'] else 'Prestado'}")


def prestar_libro():
    ver_amigos()  
    try:
        id_amigo = int(input("ID amigo: ")) - 1  # Seleccionar amigo
        ver_libros()  
        id_libro = int(input("ID libro: ")) - 1  
        # Si el libro está disponible, se presta
        if libros[id_libro]["disponible"]:
            fecha = datetime.now().strftime("%Y-%m-%d")  # Fecha actual
            prestamos.append((id_amigo, id_libro, fecha))  # Guardar el préstamo con fecha
            libros[id_libro]["disponible"] = False  # Marcar libro como prestado
            print("Préstamo realizado.")
        else:
            print("Libro no disponible.")
    except:
        print("Opción inválida.")

# Función para devolver un libro prestado
def devolver_libro():
    # Mostrar solo los préstamos activos (libros no disponibles)
    for i, (id_amigo, id_libro, fecha) in enumerate(prestamos, 1):
        if not libros[id_libro]["disponible"]:
            print(f"{i}. Libro {libros[id_libro]['titulo']} a {amigos[id_amigo]}")
    try:
        idx = int(input("Número de préstamo a devolver: ")) - 1 
        id_amigo, id_libro, fecha = prestamos[idx]
        libros[id_libro]["disponible"] = True  # Marcar libro como disponible
        print("Libro devuelto.")
    except:
        print("Opción inválida.")

# Nueva función para ver los préstamos y la fecha de hoy
def ver_prestamos():
    hoy = datetime.now().strftime("%Y-%m-%d")
    print(f"Fecha de hoy: {hoy}")
    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        for i, (id_amigo, id_libro, fecha) in enumerate(prestamos, 1):
            estado = "Activo" if not libros[id_libro]["disponible"] else "Devuelto"
            print(f"{i}. Libro: {libros[id_libro]['titulo']} | Amigo: {amigos[id_amigo]} | Fecha préstamo: {fecha} | Estado: {estado}")

def menu():
    while True:
        print("\n1. Registrar amigo\n2. Registrar libro\n3. Ver amigos\n4. Ver libros\n5. Prestar libro\n6. Devolver libro\n7. Ver préstamos\n8. Salir")
        op = input("Opción: ")
        if op == "1": registrar_amigo()
        elif op == "2": registrar_libro()
        elif op == "3": ver_amigos()
        elif op == "4": ver_libros()
        elif op == "5": prestar_libro()
        elif op == "6": devolver_libro()
        elif op == "7": ver_prestamos()
        elif op == "8": break  # Salir del programa

# Ejecutar el menú si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()