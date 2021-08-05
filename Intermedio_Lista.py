import os


class Lista:

    def __init__(self, lista):
        self.lista = lista

    def mostar(self):
        opcion = input(f"""{'MENU TRATAMIENTO LISTA'.center(60, "-")}

1) Recorrer y presentar los datos de una lista
2) Buscar un valor en una lista
3) Retornar una lista con los factoriales
4) Retornar una lista de números primos
5) Recorrer una lista de diccionario con notas de alumnos
6) Insertar un dato en una Lista dada lo Posición
7) Eliminar todas las ocurrencias en una Lista
8) Retornar cualquier valor de una lista eliminándolo
9) Copiar cada elemento de una tupla en una lista
10) Dar el vuelto a varios clientes
11) Salir

Elija una opciòn: """)

        if opcion == '1':
            Lista.presentarLista(self)

        elif opcion == '2':
            Lista.buscarLista(self)

        elif opcion == '3':
            Lista.listaFactorial(self)

        elif opcion == '4':
            Lista.listaPrimo(self)

        elif opcion == '5':
            os.system("cls")
            try:
               lista_nota = input("Escribe las notas seguido de un espacio: ").split()
               lista_entero = [int(x) for x in lista_nota]
               Lista.listaNotas(self, lista_entero)
               input("CONTINUAR..."), Lista.mostar(self)

            except ValueError:
                os.system("cls"), print("Escribe solo numeros!"), Lista.mostar(self)

        elif opcion == '6':
            try:
               dato_ingresar = int(input("Que numero vas a ingresar a la lisa: "))
               posicion = int(input("En que posiciòn deseas colocar dicho numero: "))

               Lista.insertarLista(self, dato_ingresar, posicion)
            except ValueError:
                os.system("cls"), print("Se esperaba un numero!"), Lista.mostar(self)

        elif opcion == '7':
            os.system("cls")
            try:
                numero = int(input("Escribe un numero: "))
                Lista.eliminarLista(self, numero)
            except ValueError:
                os.system("cls"), print("Se esperaba un numero!"), Lista.mostar(self)

        elif opcion == '8':
            try:
                posicion = int(input("\nEscribe un posicion: "))
                Lista.retornaValorLista(self, posicion)


            except ValueError:
                os.system("cls"), print("Se esperaba un numero!"), Lista.mostar(self)


        elif opcion == '9':
            Lista.copiarTuplaLista(self)


        elif opcion == '10':
            os.system("cls")
            try:
                clientes = input("Escriba el nombre de los clientes: ").split()
                lista_diccionario = [{cliente: ""} for cliente in clientes]
                print("Ingrese los siguientes datos para cada cliente en el respectivo orden\n")
                for dic_cliente in lista_diccionario:
                    for clave in dic_cliente:
                        pago = int(input("Escribe la cantidad a cobrar: "))
                        efectivo = int(input("Escribe cuanto paga el cliente: "))
                        vuelto = str(pago - efectivo)
                        dic_cliente[clave] = vuelto

                Lista.vueltoLista(self, lista_diccionario)
            except ValueError:
                os.system("cls"), print("DEBES INGRESAR LOS VALORES EN NUMEROS"), Lista.mostar(self)

        elif opcion == '11':
            pass
        else:
            os.system("cls"), print("Elije una alternativa existente!"), Lista.mostar(self)


    def presentarLista(self):
        os.system("cls")
        print("Los elementos de tu  lista se muestran a continuaciòn:")
        for ele in self.lista:
            print(ele)
        input("\nCONTINUAR...")
        os.system('cls')
        Lista.mostar(self)

    def buscarLista(self):
        try:
            os.system("cls")
            buscado = int(input("\nEscribe un valor que quieras buscar en la lista: "))

            if buscado in self.lista:
                print(f"El valor {buscado} ,si se encuentra en la lista\n")

            else:
                print(f"El valor {buscado}, no se encuentra en la lista\n")
            input("CONTINUAR...")
            os.system("cls")
            Lista.mostar(self)

        except ValueError:
            os.system("cls"), print("Ingresa un dato valido"), Lista.mostar(self)

    def listaFactorial(self):
        try:
            os.system("cls")
            numero = int(input("\nEscribe un numero: "))
            aux = numero
            aux_lista = []

            if numero > 0:
                while numero != 0:
                    aux_lista.append(numero + 1 - 1)
                    numero -= 1

                print(f"Los factoriales de {aux} son los siguientes:"
                      f"{aux_lista}\n")

            else:
                print("Ingresa un numero mayo que 0")

            input("CONTINUAR...\n")
            os.system("cls")
            Lista.mostar(self)

        except ValueError:
            os.system("cls"), print("Se esperaba un numero!\n"), Lista.mostar(self)

    def listaPrimo(self):
        os.system("cls")
        primos = [num for num in self.lista if num > 0 and num % 3 != 0 and num%2 != 0]
        print(f"De tu lista: {self.lista}\nLos primos obtenidos son: {primos}")

        input("CONTINUAR"), os.system("cls"), Lista.mostar(self)

    def listaNotas(self, listaNotasDicccionario):
        os.system("cls")
        dic = {"Notas": f"{listaNotasDicccionario}"}
        for llave in dic:
            print(llave, dic[llave])
        input("\nCONTINUAR..."), os.system("cls"), Lista.mostar(self)

    def insertarLista(self, valor, posicion):
        os.system("cls")
        if posicion > len(self.lista) or posicion < -(len(self.lista)):
            os.system("cls"), print("El rango que eligio no existe en la lista, eliga un rango que no exceda el rango de su lista "), Lista.mostar(self)
        else:
            lista = self.lista[0:posicion] + [valor] + self.lista[posicion:]
            print(f"La lista esta actualizada: {lista}")
            self.lista = lista
            input("CONTINUAR...")
            os.system("cls"), Lista.mostar(self)


    def eliminarLista(self, valor):
        os.system("cls")
        lista_eliminado = list(filter(lambda x: x != valor, self.lista))

        if valor not in self.lista:
            print(f"El numero {valor} no se encontro en la lista")

        print(f"Lista actualizada {lista_eliminado}")
        self.lista = lista_eliminado
        input("CONTINUAR..."), os.system("cls"), Lista.mostar(self)


    def retornaValorLista(self, posicion):


        os.system("cls")

        if posicion > len(self.lista) or posicion < -(len(self.lista)):
            print("La posiciòn esta fuera del rango de la lista, elige una posicion que exista")
        elif len(self.lista) == 0:
            print("No siento, la lista se encuentra vacia")
        else:
            lis_act = list(filter(lambda x: x != self.lista[posicion], self.lista))
            print(f"El dato de la posicion {posicion} es: {self.lista[posicion]}\nLa lista ha sido actualizada\n{lis_act}")
            self.lista = lis_act
        input("CONTINUAR..."), os.system("cls"), Lista.mostar(self)


    def copiarTuplaLista(self):
        os.system("cls")
        tupla = input("Escribe los datos que tendra tu tupla:").split()
        lista_de_tupla = [x for x in tupla]
        print(f"La lista conformada por datos de la tupla es: {lista_de_tupla}")
        input("CONTINUAR...")
        os.system("cls")
        Lista.mostar(self)


    def vueltoLista(self, listaClientesDiccionario):
        os.system("cls")
        for cada_dic in listaClientesDiccionario:
            for cliente in cada_dic:
                print(f"EL vuelto del cliente {cliente} es: {cada_dic[cliente]}")
        input("CONTINUAR...")
        os.system("cls"), Lista.mostar(self)