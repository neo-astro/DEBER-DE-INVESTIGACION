import os
class Basico:
    def mostrar(self):
        opcion = input(f"""{'Menu Operación Numeros'.center(60, "-")}

1)	Presentar los números de 1 a n
2)	Sumar los números de 1 a n
3)	Múltiplo de cualquier numero
4)	Presentar los divisores de un numero
5)	Numero Primo
6)	Factorial de cualquier numero
7)	Fibonacci de una serie de n números
8)	Perfecto
9)	Primos gemelos
10)	Números amigos
11)	Salir


Elija una opciòn: """)

        if opcion == '1':
            os.system("cls")
            try:
                n = int(input("Escribe un numero: "))
                Basico.numerosN(self, n)
                input("CONTINUAR..."), os.system("cls"), Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero!"), Basico.mostrar(self)

        elif opcion == '2':
            os.system("cls")
            try:
                numero = int(input("Escribe un numero: "))
                if numero < 0:
                    raise ValueError
                Basico.recorrer(self, numero)
                input("CONTINUAR..."), os.system("cls"), Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero y que este sea mayor que 0"), Basico.mostrar(self)

        elif opcion == '3':
            os.system("cls")
            try:
                numero = int(input("Escribe un numero: "))
                Basico.multiplos(self, numero)

                input("CONTINUAR..."), os.system("cls"), Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero!"), Basico.mostrar(self)

        elif opcion == '4':
            os.system("cls")
            try:
                numero = int(input("Escribe un numero: "))
                print(f"Los divisores de {numero} son: {Basico.divisores(self, numero)}")
                input("CONTINUAR..."), os.system("cls"),  Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero!"), Basico.mostrar(self)

        elif opcion == '5':
            os.system("cls")
            try:
                numero = int(input("Escribe un numero: "))
                Basico.primo(self, numero)
                input("CONTINUAR..."), os.system("cls"),  Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero!"), Basico.mostrar(self)

        elif opcion == '6':
            run = Intermedio()
            try:
                n = int(input("El factorial de que numero deseas: "))
                run.numerosN(n)
                input("CONTINUAR..."), os.system("cls"), Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero!"), Basico.mostrar(self)

        elif opcion == '7':
            run = Intermedio()
            try:
                numero = int(input("Ingresa un numero: "))
                if numero <= 0:
                    raise ValueError
                run.factorial(numero)
                input("CONTINUAR..."), os.system("cls"), Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero! y que este sea mayor a cero"), Basico.mostrar(self)

        elif opcion == '8':

            try:
                numero = int(input("Ingresa un numero: "))
                if numero <= 0:
                    raise ValueError
                Basico.perfecto(self, numero)
                input("CONTINUAR..."), os.system("cls"), Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero! y que este sea mayor a cero"), Basico.mostrar(self)


        elif opcion == '9':
            run = Intermedio()

            try:
                n1 = int(input("Escribe: "))
                n2 = int(input("Escribe: "))
                run.primosGemelos(n1, n2)
                input("CONTINUAR..."), os.system("cls"), Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero!"), Basico.mostrar(self)

        elif opcion == '10':
            run = Intermedio()
            os.system("cls")
            try:
                num1 = int(input("Escribe un numero: "))
                num2 = int(input("Escribe otro numero: "))
                run.amigos(num1, num2)
                input("CONTINUAR..."), os.system("cls"), Basico.mostrar(self)
            except ValueError:
                os.system("cls"), print("Escribe un numero!"), Basico.mostrar(self)

        elif opcion == '11':
            return opcion

        else:
            volver = False
            os.system("Cls"), print("ELIE UN OPCION! VALIDA\n"), Basico.mostrar(self)

    def numerosN(self, n):
        for n in range(1, 10 + 1):
            print(n)


    def recorrer(self, num1):
            lista = [x for x in range(1, num1 + 1)]
            print(f"La suma es: {sum(lista)}", "\n")
    # multiplos
    def multiplos(self, numero):
        multiplos = [numero*x for x in range(1, 101) ]
        print(f"En el rango de los 100 primeros numeros los multiplos de {numero} son: {multiplos}" )


    # DIVISORES
    def divisores(self, numero):
        numeros = [num for num in range(1, numero + 1)]
        divisores = list(filter(lambda x: numero % x == 0, numeros))
        return (divisores)

    def perfecto(self, numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        if suma == numero:
            print(f"El numero {numero} es perfecto")
        else:
            print(f"El numero {numero} no es perfecto")
#Primo

    def primo(self, numero):
        if numero > 1 and numero%2 != 0 and numero%3 != 0:
            print(f"El numero {numero} es primo")
        else:
            print(f"El numero {numero} no es primo")

class Intermedio(Basico):
    def __init__(self):
        super().__init__()

#FACTORIAL
    def numerosN(self, num):
        aux = num
        lista_factorial = []
        while num != 0:
            lista_factorial.append(num)
            num -= 1
        print(f"Los factoriales de {aux} son: {lista_factorial}")

#FIBONACCI
    def factorial(self, numero):
        factorial = 1
        for i in range(numero):
            print(factorial, "*", numero)
            factorial *= numero
            numero -= 1
        return factorial

    def fibonacci(self, num):
        anterior = 0
        siguiente = 1
        print(1)
        for i in range(num):
            r = anterior + siguiente
            anterior = siguiente
            siguiente = r
            print(r)


    def primosGemelos(self, n1, n2):
        prueba = 2
        es_primo = lambda x: x == 3 or (x % 2 != 0 and x % 3 != 0)

        if n1 == n2:
            print("No son primos gemelos")

        elif n1 == 1 or n2 == 1:
            print("No son primos gemelos")

        else:

            if es_primo(n1) and es_primo(n2):
                if n1 > n2:
                    if n1 - n2 == prueba:
                        print("Son primos gemelos")
                    else:
                        print("No son primos gemelos")
                elif n2 > n1:
                    if n2 - n1 == prueba:
                        print("Son primos gemelos")
                    else:
                        print("No son primos gemelos")

            else:
                print("No son primos gemelos")


    def amigos(self, num1, num2):
        divisores_n1 = Basico.divisores(self, num1)[:-1]
        divisores_n2 = Basico.divisores(self, num2)[:-1]
        if sum(divisores_n1) == num2 and sum(divisores_n2) == num1:
            print("Son amigos!")
        else:
            print("Los numeros no son amigos")
