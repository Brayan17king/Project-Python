import core
import citas

if __name__ == "__main__":
    ciclo = True
    while ciclo:
        cicloTry = True
        while cicloTry:
            core.menuPrincipal()
            opcMenu = core.TryExcept(input("Ingrese una Opcion ⬆: "))
            if type(opcMenu) == int:
                cicloTry = False
        if opcMenu == 1:
            citas.agregarCitas()
        elif opcMenu == 2:
            citas.buscarCitas()
        elif opcMenu == 3:
            citas.modificarCitas()
        elif opcMenu == 4:
            citas.eliminarCitas()
        elif opcMenu == 5:
            core.clear()
            ciclo = False
        else:
            print("Opcion no valida")
            input("Press enter to continue...")
