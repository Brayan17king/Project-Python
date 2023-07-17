import os
import json


def clear():
    os.system("cls") and os.system("clear")


def TryExcept(variable):
    try:
        numero = int(variable)
        return numero
    except Exception:
        print("\nError... El valor ingresado no es numérico.")
        input("\n Press Enter to continue...")


def leerArchivo(nombreArchivo):
    ciclo = True
    while ciclo:
        localizacionArchivo = f"data/{nombreArchivo}.json"
        try:
            with open(localizacionArchivo, "r") as archivo:
                contenido = archivo.read()
            contenidoDiccionario = json.loads(contenido)
            ciclo = False
            return contenidoDiccionario
        except Exception:
            with open(localizacionArchivo, "x") as archivo:
                archivo.write("{}")


def escribirArchivo(nombreArchivo, escritura):
    localizacionArchivo = f"data/{nombreArchivo}.json"
    try:
        with open(localizacionArchivo, "w") as archivo:
            archivo.write(escritura)
    except Exception:
        print("\nError... No se pudo escribir el archivo.")
        input("\n Press Enter to continue...")


def convertirArchivo(diccionario):
    archivoJson = json.dumps(diccionario, indent=4)
    return archivoJson


def menuPrincipal():
    clear()
    print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
    print("-" * 10, "{:^44}".format("MENU PRINCIPAL📜"), "-" * 10)
    print("-" * 67)
    print(
        "\n1. Agregar Cita📖\n2. Buscar Cita🔍\n3. Modificar Cita📑\n4. Cancelar Cita❌\n\n5.Salir👋"
    )
    print("-" * 67)
