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
        datos = self.cadena.split()
        print("La cadena contiene lo siguiente:")
        for ele in datos:
            print(ele)
        input("CONTINUAR..."), os.system("cls"), Cadena.mostrar(self)

    def buscarCaracter(self):
        os.system("cls")
        buscado = input("Ingrese su string: ")
        if buscado in self.cadena:
            print("El caracter {} si se encuentra en la cadena!".format(buscado))
        else:
            print("El caracter {} no se encuentra en la cadena!".format(buscado))

        input("CONTINUAR...")
        os.system("cls"), Cadena.mostrar(self)

    def listaPosiciones(self):
        os.system("cls")
        caracter = (input("Escribe el caracter que quieres buscar en la cadena: ")).lower()
        lista_de_caracter = []
        for pos, ele in enumerate(self.cadena):
            if caracter == ele:
                lista_de_caracter.append(pos)
        print(f"Tu busqueda del caracter {caracter} tiene las siguientes posiciones dentro de la cadena: {lista_de_caracter}")
        input("CONTINUAR..."), os.system("cls"), Cadena.mostrar(self)

    def listaPalabras(self):

        os.system("cls")
        cad = self.cadena
        lista = cad.split()
        print(f"Las palabras en tu cadena son las siguientes: {lista}")
        input("CONTINUAR..."), os.system("cls"), Cadena.mostrar(self)


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

        try:
            listaNum1 = self.cadena.split()
            valor = input("Ingrese una dato: ").lower()

            pos = int(input("Ingrese una posición: "))
            if pos > len(listaNum1) or pos < - len(listaNum1):
                print("Rango fuera del alcanze!")
            else:
                #Metodo facil
                # listaNum1.insert(pos, valor)
                listaNum1 = listaNum1[:pos] + [valor] + listaNum1[pos:]
                print(f"La cadena se ha actualizado: {listaNum1}")
                self.cadena = " ".join(listaNum1)
            input("CONTINUAR..."), os.system("cls"), Cadena.mostrar(self)
        except ValueError:
            os.system("cls"), print("Debes escribir un número"), Cadena.insertarDato(self)

    def eliminarOcurrencias(self):
        os.system("cls")
        if len(self.cadena) == 0:
            print("No siento, la cadena se encuentra vacia")
        else:
            eliminar = input("Escriba lo que un string que quiera eliminar: ")
            cad = self.cadena
            lista = cad.split()
            res = list(filter(lambda x: x != eliminar, lista))
            self.cadena = " ".join(res)
        print(f"Cadena actualizada: {self.cadena}")
        input("CONTINUAR...")
        os.system("cls"), Cadena.mostrar(self)

    def retornaValor(self):
        try:
            os.system("cls")
            lista = self.cadena.split()
            elim = input("Que ocurrencia quiere eliminar: ").lower()
            if len(self.cadena) == 0:
                print("No siento, la lista se encuentra vacia")
            elif elim in lista:
                for pos, i in enumerate(lista):
                    if i == elim:
                        lista.pop(pos)
                print("Se eliminado: {}\nLa lista actualizada es: {}.".format(elim, lista))
                self.cadena = " ".join(lista)
            else:
                os.system("cls"), print("Elemento no encontrado en la lista!"), input("CONTINUAR..."), Cadena.mostrar(self)
            input("CONTINUAR..."), os.system("cls"), Cadena.mostrar(self)
        except ValueError:
            os.system("cls"), print("¡Inserte un string!"), Cadena.mostrar(self)

    def concatenarCadena(self):
        os.system("cls")
        cadena2 = input("Ingrese la segunda cadena: ").lower()
        space = " "
        cont = self.cadena + space + cadena2
        print("La concatenación de las cadenas es: {}".format(cont))
        input("CONTINUAR..."), os.system("cls"), Cadena.mostrar(self)
