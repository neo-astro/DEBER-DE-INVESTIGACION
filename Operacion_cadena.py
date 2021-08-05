import os

class Cadena():
    def __init__(self, cadena):
        self.cadena = cadena

    def mostrar(self):
        opc = input(f'''{"Menu Operaciones de Cadenas".center(60, "-")}

1)	Recorrer y presentar los datos de una cadena
2)	Buscar un carácter en una cadena
3)	Retornar una lista con la posiciones dado un carácter de la cadena
4)	Retornar una lista con todas las palabras de una cadena
5)	Retornar una cadena a partir de una lista
6)	Insertar un dato en una cadena dada lo Posición
7)	Eliminar todas las ocurrencias en una cadena
8)	Retornar cualquier valor de una cadena eliminándolo 
9)	Concatenar cadenas
10)	Salir         

Elija una opción: ''')
        if opc == "1":
            Cadena.recorrerCadena(self)

        elif opc == "2":
            Cadena.buscarCaracter(self)

        elif opc == "3":
            Cadena.listaPosiciones(self)

        elif opc == "4":
            Cadena.listaPalabras(self)

        elif opc == "5":
            Cadena.cadenaLista(self)

        elif opc == "6":
            Cadena.insertarDato(self)

        elif opc == "7":
            Cadena.eliminarOcurrencias(self)

        elif opc == "8":
            Cadena.retornaValor(self)

        elif opc == "9":
            Cadena.concatenarCadena(self)

        elif opc == "10":
            pass

        else:
            return os.system("cls"), print("Elija una opción valida\n"), Cadena.mostrar(self)

    def recorrerCadena(self):
        os.system("cls")
        cad = input("Datos: ")
        lista = cad.split()
        print("La lista es: ", lista)
        input("CONTINUAR...")
        os.system("cls"), Cadena.mostrar(self)

    def buscarCaracter(self):
        os.system("cls")
        buscado = input("Ingrese su string: ")
        if buscado in self.cadena:
            print("El caracter {} si se encuentra en la cadena".format(buscado))
        else:
            print("El caracter {} no se encuentra en la cadena".format(buscado))
            input("CONTINUAR...")
            os.system("cls"), Cadena.mostrar(self)

    def listaPosiciones(self):
        os.system("cls")
        caracter = self.cadena
        for i, c in enumerate(caracter):
            print("Carácter: %s - Indice: %i" % (c, i))
            input("CONTINUAR...")
            os.system("cls"), Cadena.mostrar(self)

    def listaPalabras(self):
        os.system("cls")
        lista = self.cadena
        palabras = lista.split()
        print(palabras)
        print(len(palabras))
        input("CONTINUAR...")
        os.system("cls"), Cadena.mostrar(self)

    def cadenaLista(self):
        os.system("cls")
        lista = self.cadena
        lista1 = lista.split()
        lista2 = " ".join(lista1)
        print("La lista es: ", lista1)
        print("La cadena es: ", lista2)
        input("CONTINUAR...")
        os.system("cls"), Cadena.mostrar(self)

    def insertarDato(self):
        os.system("cls")
        listaNum = self.cadena
        listaNum1 = listaNum.split()
        valor = str(input("Ingrese una dato: "))
        try:
            pos = int(input("Ingrese una posición: "))
            if pos > len(listaNum1):
                print("Rango fuera del alcanze")
            else:
                listaNum1 = listaNum1[0:pos] + [valor] + listaNum1[pos:]
                print(listaNum1)
            input("CONTINUAR...")
            os.system("cls"), Cadena.mostrar(self)
        except ValueError:
            os.system("cls"), print("Escriba un número"), Cadena.insertarDato(self)

    def eliminarOcurrencias(self):
        os.system("cls")
        cad = self.cadena
        lista = cad.split()
        elim = input("Que ocurrencia quiere eliminar: ")
        for i in lista:
            if elim == i:
                lista.remove(elim)
        print(lista)
        input("CONTINUAR...")
        os.system("cls"), Cadena.mostrar(self)

    def retornaValor(self):
        try:
            os.system("cls")
            cad = self.cadena
            lista = cad.split()
            elim = input("Que ocurrencia quiere eliminar: ")
            if elim in lista:
                for i in lista:
                    if i == elim:
                        lista.remove(i)
                print("Se eliminado: {}\nLa lista actualizada es: {}.".format(elim, lista))
            else:
                os.system("cls"), print("Elemento no se encontro en la lista"), Cadena.mostrar(self)
        except ValueError:
            os.system("cls"), print("¡Inserte un string!"), Cadena.mostrar(self)

    def concatenarCadena(self):
        os.system("cls")
        cad = input("Ingrese la segunda cadena: ")
        cont = self.cadena + cad
        print()
        print("La concatenación de las cadenas es: {}".format(cont))
        input("CONTINUAR...")
        os.system("cls"), Cadena.recorrerCadena(self)
