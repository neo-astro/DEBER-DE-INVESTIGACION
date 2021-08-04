from Basico_intermedio import *
from Intermedio_Lista import *
import os


class Menu:
    def menu(self):
        opcion = input(f"""{'Menu Principal'.center(60, "-")}

1). Calculadora
2). Operación Numeros
3). Tratamiento de Listas
4). Operaciones de  Cadenas
5). Salir

Elija una opcion: """)

        if opcion == "1":
            os.system("cls")
            pass

        elif opcion == "2":
            os.system("cls")
            basico = Basico()
            if basico.mostrar() != "11":
                os.system("cls")
                Menu.menu(self)

        elif opcion == "3":
            os.system("cls")
            try:

                lista_datos = input("""Para usar Tratamiento de Lista debes crear una lista primero
Introdusca los datos que va a tener tu lista: """).split()
                lista_enteros = [int(x) for x in lista_datos]
                input("Se ha guardado la lista\nCONTINUAR...\n")
                os.system("cls")
                lista = Lista(lista_enteros)
                if lista.mostar() == "11":
                    os.system("cls")
                    Menu.menu(self)

            except ValueError:
                os.system("cls"), print("Escribe solo numeros!\n"), Menu.menu(self)

        elif opcion == "4":
            pass

        elif opcion == "5":
            exit()

        else:
            return os.system("cls"), print("Elije una opciòn correcta\n"), Menu.menu(self)


menu = Menu()
menu.menu()
