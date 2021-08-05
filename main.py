from Basico_intermedio import *
from Intermedio_Lista import *
from Calculadora import *
from Operacion_cadena import *
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
            try:
                num1 = float(input("Debes enviar datos para acceder a esta función\nPrimer dato: "))
                num2 = float(input("segundo dato: "))
                os.system("cls")
                calculadora = Calculadora(num1, num2)
                if calculadora.mostrar() != "10":
                    os.system("cls")
                    Menu.menu(self)

            except ValueError:
                os.system("cls"), print("Escribe un valor numerico!\n"), Menu.menu(self)

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
                if lista.mostar() != "11":
                    os.system("cls")
                    Menu.menu(self)

            except ValueError:
                os.system("cls"), print("Escribe solo numeros!\n"), Menu.menu(self)

        elif opcion == "4":
            cad = input("Escribe una cadena para acceder al menu selecionado: ").lower()
            cadena = Cadena(cad)
            os.system("cls")
            if cadena.mostrar() != "10":
                os.system("cls")
                Menu.menu(self)

        elif opcion == "5":
            exit()

        else:
            return os.system("cls"), print("Elije una opciòn correcta\n"), Menu.menu(self)


menu = Menu()
menu.menu()
