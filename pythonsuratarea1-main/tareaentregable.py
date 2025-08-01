

from datetime import datetime
import os

amigos = []
libros = []
prestamos = []

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
        id_amigo = int(input("ID amigo: ")) - 1
        ver_libros()
        id_libro = int(input("ID libro: ")) - 1
        if libros[id_libro]["disponible"]:
            prestamos.append((id_amigo, id_libro))
            libros[id_libro]["disponible"] = False
            print("Préstamo realizado.")
        else:
            print("Libro no disponible.")
    except:
        print("Opción inválida.")

def devolver_libro():
    for i, (id_amigo, id_libro) in enumerate(prestamos, 1):
        if not libros[id_libro]["disponible"]:
            print(f"{i}. Libro {libros[id_libro]['titulo']} a {amigos[id_amigo]}")
    try:
        idx = int(input("Número de préstamo a devolver: ")) - 1
        id_amigo, id_libro = prestamos[idx]
        libros[id_libro]["disponible"] = True
        print("Libro devuelto.")
    except:
        print("Opción inválida.")

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
        elif op == "7": break

if __name__ == "__main__":
    menu()