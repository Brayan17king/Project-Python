import core

citas = core.leerArchivo("citas")


def agregarCitas():
    ciclo = True
    while ciclo:
        core.clear()
        print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
        print("-" * 10, "{:^44}".format("AGREGAR CITA📖"), "-" * 10)
        print("-" * 67)
        nombrePaciente = input("\nIngrese el nombre del Paciente: ").title()
        cicilo1 = True
        while cicilo1:
            core.clear()
            print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
            print("-" * 10, "{:^44}".format("AGREGAR CITA📖"), "-" * 10)
            print("-" * 67)
            añoCita = core.TryExcept(input("\n Ingrese el Año de la Cita: "))
            if type(añoCita) == int:
                if añoCita >= 2023:
                    cicilo1 = False
                else:
                    print("\nOpcion No Valida... El año ya paso...")
                    input("Press Enter to Continue...")
        ciclo2 = True
        while ciclo2:
            core.clear()
            print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
            print("-" * 10, "{:^44}".format("AGREGAR CITA📖"), "-" * 10)
            print("-" * 67)
            mesCita = core.TryExcept(input("\nIngrese el Mes de la Cita: "))
            if type(mesCita) == int:
                if (mesCita <= 12) and (mesCita > 0):
                    ciclo2 = False
                else:
                    print(f"\nOpcion No Valida... EL mes {mesCita} no existe... ")
                    input("Press Enter to Continue...")
        ciclo3 = True
        while ciclo3:
            core.clear()
            print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
            print("-" * 10, "{:^44}".format("AGREGAR CITA📖"), "-" * 10)
            print("-" * 67)
            diaCita = core.TryExcept(input("\nIngrese el Dia de la Cita: "))
            if type(diaCita) == int:
                if (mesCita == 1, 3, 5, 7, 8, 10, 12):
                    if (diaCita > 0) and (diaCita <= 31):
                        ciclo3 = False
                    else:
                        print(f"\nOpcion No Valida... el dia {diaCita} No es valido...")
                        input("Press Enter to Continue...")
                elif (mesCita == 4, 6, 9, 11):
                    if (diaCita > 0) and (diaCita <= 30):
                        ciclo3 = False
                    else:
                        print(f"\nOpcion No Valida... el dia {diaCita} No es valido...")
                        input("Press Enter to Continue...")
                elif mesCita == 2:
                    if (diaCita > 0) and (diaCita <= 28):
                        ciclo3 = False
                    else:
                        print(f"\nOpcion No Valida... el dia {diaCita} No es valido...")
                        input("Press Enter to Continue...")
        ciclo4 = True
        while ciclo4:
            core.clear()
            print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
            print("-" * 10, "{:^44}".format("AGREGAR CITA📖"), "-" * 10)
            print("-" * 67)
            horaCita = core.TryExcept(
                input("\nIngrese la Hora de la Cita (8am a 19pm): ")
            )
            if type(horaCita) == int:
                if (horaCita >= 8) and (horaCita <= 19):
                    ciclo4 = False
                else:
                    print("\nOpcion No Valida... Esta Cerrado...")
                    input("Press Enter to Continue...")
        ciclo5 = True
        while ciclo5:
            core.clear()
            print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
            print("-" * 10, "{:^44}".format("AGREGAR CITA📖"), "-" * 10)
            print("-" * 67)
            minutoCita = core.TryExcept(
                input("\nIngrese el minuto de la Cita (30 o 00): ")
            )
            if type(minutoCita) == int:
                if minutoCita == 0:
                    ciclo5 = False
                elif minutoCita == 30:
                    ciclo5 = False
                else:
                    print("\nOpcion No Valida...")
                    input("Press Enter to Continue...")

        motivoCita = input("\nIngrese el Motivo de la Consulta: ").capitalize()

        FechaCompletaCita = {
            "dia": diaCita,
            "mes": mesCita,
            "año": añoCita,
        }
        horaCompletaCita = {"hora": horaCita, "minuto": minutoCita}
        citas.update({nombrePaciente: {}})
        citas[nombrePaciente].update(
            {
                "fecha": FechaCompletaCita,
                "hora": horaCompletaCita,
                "motivo": motivoCita,
            }
        )
        core.escribirArchivo("citas", core.convertirArchivo(citas))
        core.clear()
        print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
        print("-" * 10, "{:^44}".format("AGREGAR CITA📖"), "-" * 10)
        print("-" * 67)
        print(f"\nLas cita de {nombrePaciente} fue agendada satisfactoriamente.")
        input("\nPresione Enter para volver. . . ")
        ciclo = False


def buscarCitas():
    ciclo = True
    while ciclo:
        ciclo2 = True
        while ciclo2:
            core.clear()
            print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
            print("-" * 10, "{:^44}".format("BUSCAR CITA📖"), "-" * 10)
            print("-" * 67)
            nombrePaciente = input(
                "\nIngrese el nombre del Paciente a Buscar: "
            ).title()
            core.clear()
            print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
            print("-" * 10, "{:^44}".format("BUSCAR CITA📖"), "-" * 10)
            print("-" * 67)
            if nombrePaciente in citas:
                print(f"\nEL paciente {nombrePaciente} esta registrado")
                for items, nombre in enumerate(citas):
                    if nombre == nombrePaciente:
                        for dato, valor in citas[nombre].items():
                            if dato == "fecha":
                                print(
                                    f'\nFecha: {valor["dia"]}/{valor["mes"]}/{valor["año"]}'
                                )
                            elif dato == "hora":
                                print(f'Hora: {valor["hora"]}:{valor["minuto"]}')
                            elif dato == "motivo":
                                print(f"Motivo: {valor}")
                                input("\nPresione Enter para volver...")
            else:
                print("Error... EL paciente no se encuentra registrado...")
                input("\nPresione Enter para volver...")
            ciclo2 = False
        ciclo = False


def modificarCitas():
    ciclo = True
    while ciclo:
        ciclo2 = True
        while ciclo2:
            core.clear()
            print("-" * 10, "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "), "-" * 10)
            print("-" * 10, "{:^44}".format("MODIFICAR CITA📖"), "-" * 10)
            print("-" * 67)
            nombrePaciente = input(
                "\nIngrese el nombre del Paciente a Modificar: "
            ).title()
            if nombrePaciente in citas:
                for index, nombre in enumerate(citas):
                    if nombrePaciente == nombre:
                        for dato, valor in citas[nombre].items():
                            if dato == "fecha":
                                print(
                                    f'\n1 - Fecha: {valor["dia"]}/{valor["mes"]}/{valor["año"]}'
                                )
                            elif dato == "hora":
                                print(f'2 - Hora: {valor["hora"]}:{valor["minuto"]}')
                            elif dato == "motivo":
                                print(f"3 - Motivo: {valor}")
                        print(f"4 - Nombre: {nombre}")
                        indexDato = core.TryExcept(
                            input("\n Ingrese el dato a modificar: ")
                        )
                        if type(indexDato) == int:
                            if (indexDato > 0) and (indexDato <= 4):
                                ciclo2 = False
                        if indexDato == 1:
                            ciclo3 = True
                            while ciclo3:
                                core.clear()
                                print(
                                    "-" * 10,
                                    "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                                    "-" * 10,
                                )
                                print(
                                    "-" * 10,
                                    "{:^44}".format("MODIFICAR FECHA"),
                                    "-" * 10,
                                )
                                print("-" * 67)
                                añoNuevo = core.TryExcept(
                                    input("\n Ingrese el nuevo año de la cita: ")
                                )
                                if type(añoNuevo) == int:
                                    if añoNuevo >= 2023:
                                        ciclo3 = False
                                    else:
                                        print("\nOpcion No Valida... El año ya paso...")
                                        input("Press Enter to Continue...")
                            ciclo4 = True
                            while ciclo4:
                                core.clear()
                                print(
                                    "-" * 10,
                                    "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                                    "-" * 10,
                                )
                                print(
                                    "-" * 10,
                                    "{:^44}".format("MODIFICAR FECHA"),
                                    "-" * 10,
                                )
                                print("-" * 67)
                                mesNuevo = core.TryExcept(
                                    input("\n Ingrese el nuevo mes de la cita: ")
                                )
                                if type(mesNuevo) == int:
                                    if (mesNuevo > 0) and (mesNuevo <= 12):
                                        ciclo4 = False
                                    else:
                                        print(
                                            f"\nOpcion No Valida... El mes {mesNuevo} No existe..."
                                        )
                                        input("Press Enter to Continue...")
                            ciclo5 = True
                            while ciclo5:
                                core.clear()
                                print(
                                    "-" * 10,
                                    "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                                    "-" * 10,
                                )
                                print(
                                    "-" * 10,
                                    "{:^44}".format("MODIFICAR FECHA"),
                                    "-" * 10,
                                )
                                print("-" * 67)
                                diaNuevo = core.TryExcept(
                                    input("\n Ingrese el nuevo dia de la cita: ")
                                )
                                if type(diaNuevo) == int:
                                    if (mesNuevo == 1, 3, 5, 7, 8, 10, 12):
                                        if (diaNuevo > 0) and (diaNuevo <= 31):
                                            ciclo5 = False
                                    elif (mesNuevo == 4, 6, 9, 11):
                                        if (diaNuevo > 0) and (diaNuevo <= 30):
                                            ciclo5 = False
                                    elif mesNuevo == 2:
                                        if (diaNuevo > 0) and (diaNuevo <= 28):
                                            ciclo5 = False
                                    else:
                                        print(
                                            f"\nOpcion No Valida... El dia {diaNuevo} No existe..."
                                        )
                                        input("Press Enter to Continue...")

                            citas[nombre]["fecha"].update(
                                {"dia": diaNuevo, "mes": mesNuevo, "año": añoNuevo}
                            )
                            core.escribirArchivo("citas", core.convertirArchivo(citas))
                            core.clear()
                            print(f"la Fecha Fue Modificada Satisfactoriamente...")
                            input("\nPresione Enter para volver...")
                            ciclo = False
                            break
                        elif indexDato == 2:
                            ciclo6 = True
                            while ciclo6:
                                core.clear()
                                print(
                                    "-" * 10,
                                    "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                                    "-" * 10,
                                )
                                print(
                                    "-" * 10,
                                    "{:^44}".format("MODIFICAR HORA"),
                                    "-" * 10,
                                )
                                print("-" * 67)
                                horaNuevo = core.TryExcept(
                                    input("\n Ingrese la nueva hora de la cita: ")
                                )
                                if type(horaNuevo) == int:
                                    if (horaNuevo) >= 8 and (horaNuevo <= 19):
                                        ciclo6 = False
                                    else:
                                        print(
                                            "\nOpcion No Valida... La hora ya paso..."
                                        )
                                        input("Press Enter to Continue...")
                            ciclo7 = True
                            while ciclo7:
                                core.clear()
                                print(
                                    "-" * 10,
                                    "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                                    "-" * 10,
                                )
                                print(
                                    "-" * 10,
                                    "{:^44}".format("MODIFICAR HORA"),
                                    "-" * 10,
                                )
                                print("-" * 67)
                                minutoNuevo = core.TryExcept(
                                    input(
                                        "\n Ingrese el nuevo minuto de la cita (00 o 30): "
                                    )
                                )
                                if type(minutoNuevo) == int:
                                    if minutoNuevo == 00:
                                        ciclo7 = False
                                    elif minutoNuevo == 30:
                                        ciclo7 = False
                                    else:
                                        print(
                                            f"\nOpcion No Valida... El minuto {minutoNuevo} No existe..."
                                        )
                                        input("Press Enter to Continue...")
                            citas[nombre]["hora"].update(
                                {"hora": horaNuevo, "minuto": minutoNuevo}
                            )
                            core.escribirArchivo("citas", core.convertirArchivo(citas))
                            core.clear()
                            print(f"la Hora Fue Modificada Satisfactoriamente...")
                            input("\nPresione Enter para volver...")
                            ciclo = False
                            break
                        elif indexDato == 3:
                            ciclo8 = True
                            while ciclo8:
                                core.clear()
                                print(
                                    "-" * 10,
                                    "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                                    "-" * 10,
                                )
                                print(
                                    "-" * 10,
                                    "{:^44}".format("MODIFICAR MOTIVO"),
                                    "-" * 10,
                                )
                                print("-" * 67)
                                motivoNuevo = input(
                                    "\n Ingrese el nuevo motivo de la cita: "
                                ).capitalize()
                                if motivoNuevo == "str":
                                    ciclo8 = False
                                else:
                                    print("Error.. EL dato ingresado es numerico...")

                                citas[nombre].update({"motivo": motivoNuevo})
                                core.escribirArchivo(
                                    "citas", core.convertirArchivo(citas)
                                )
                                core.clear()
                                print(f"El Motivo Fue Modificado Satisfactoriamente...")
                                input("\nPresione Enter para volver...")
                                ciclo = False
                                break
                        elif indexDato == 4:
                            ciclo9 = True
                            while ciclo9:
                                core.clear()
                                print(
                                    "-" * 10,
                                    "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                                    "-" * 10,
                                )
                                print(
                                    "-" * 10,
                                    "{:^44}".format("MODIFICAR NOMBRE"),
                                    "-" * 10,
                                )
                                print("-" * 67)
                                nombreNuevo = input(
                                    "\n Ingrese el nuevo nombre de la cita: "
                                ).title()
                                if nombreNuevo == "str":
                                    ciclo9 = False
                                else:
                                    print("Error.. EL dato ingresado es numerico...")
                                    input("\nPress Enter to continue...")
                                citas.update({nombreNuevo: citas.pop(nombre)})
                                core.escribirArchivo(
                                    "citas", core.convertirArchivo(citas)
                                )
                                core.clear()
                                print(f"El Nombre Fue Modificado Satisfactoriamente...")
                                input("\nPresione Enter para volver...")
                                ciclo = False
                                break
                        elif indexDato == 0:
                            ciclo = False


def eliminarCitas():
    ciclo = True
    while ciclo:
        ciclo2 = True
        while ciclo2:
            core.clear()
            print(
                "-" * 10,
                "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                "-" * 10,
            )
            print(
                "-" * 10,
                "{:^44}".format("CANCELAR CITAS"),
                "-" * 10,
            )
            print("-" * 67)
            nombre = input(
                "\nIngrese el nombre de la persona a cancelar su cita: "
            ).title()
            print("\nSeguro quiere cancelar la cita? \n\n1.Si \n2.No")
            eliminar = core.TryExcept(input("\nIngrese la Opcion: "))
            if type(eliminar) == int:
                if (eliminar >= 1) and (eliminar <= 2):
                    ciclo2 = False
                else:
                    print("\nOpcion No Valida...")
                    input("\nPress Enter to continue...")
        if eliminar == 1:
            citas.pop(nombre)
            citas.update()
            core.escribirArchivo("citas", core.convertirArchivo(citas))
            core.clear()
            print(f"La Cita de {nombre} ha sido cancelada...")
            input("\nPresione Enter para volver...")
            ciclo = False
            break
        elif eliminar == 2:
            core.clear()
            print(
                "-" * 10,
                "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                "-" * 10,
            )
            print(
                "-" * 10,
                "{:^44}".format("CANCELAR CITAS"),
                "-" * 10,
            )
            print("-" * 67)
            print("\nNo se elimino la cita.")
            input("\nPresione Enter para volver...")
            ciclo = False
            break
