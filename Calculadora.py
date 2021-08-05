import os


class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def mostrar(self):
        opcion = input(f'''{"Menu Calculadora".center(60, "-")})
1)	Suma
2)	Resta
3)	Multiplicacion
4)	Division
5)	Exponente
6)	Valor Absoluto
7)	Circunferencia
8)	Area Circulo
9)	Area Cuadrado
10)	Salir

Elija una opción: ''')
        if opcion == "1":
            Calculadora.suma(self)

        elif opcion == "2":
            Calculadora.resta(self)

        elif opcion == "3":
            Calculadora.mutiplicacion(self)

        elif opcion == "4":
            Calculadora.division(self)

        elif opcion == "5":
            calstandar = CalEstandar(self, self)
            calstandar.exponenete()

        elif opcion == "6":
            calstandar = CalEstandar(self, self)
            calstandar.ValorAbsoluto()
            input("CONTINUAR..."), os.system("cls"), Calculadora.mostrar(self)

        elif opcion == "7":
            calcientifica = CalCientifica(self, self)
            calcientifica.circunferencia()

        elif opcion == "8":
            calcientifica = CalCientifica(self, self)
            calcientifica.areaCirculo()

        elif opcion == "9":
            calcientifica = CalCientifica(self, self)
            calcientifica.areaCuadrado()


        elif opcion == "10":
            pass

        else:
            os.system("cls"), print("Elija una opción valida\n"), Calculadora.mostrar(self)

    def suma(self):
        os.system("cls")
        print(f"Resultado de sumar {self.numero1} + {self.numero2} = ", self.numero1 + self.numero2)
        input("CONTINUAR..."), os.system("cls"), Calculadora.mostrar(self)

    def resta(self):
        os.system("cls")
        rest = self.numero1 - self.numero2
        print(f"Resultado de restar {self.numero1} - {self.numero2} = ", rest)
        input("CONTINUAR..."), os.system("cls"), Calculadora.mostrar(self)

    def mutiplicacion(self):
        os.system("cls")
        print(f"Resultado de multiplicar {self.numero1}*{self.numero2} ", self.numero1 * self.numero2)
        input("CONTINUAR..."), os.system("cls"), Calculadora.mostrar(self)

    def division(self):
        os.system("cls")
        print(f"Resultado de dividir {self.numero1}/{self.numero2} = ", self.numero1 / self.numero2)
        input("CONTINUAR..."), os.system("cls"), Calculadora.mostrar(self)


class CalEstandar(Calculadora):

    def exponenete(self):
        try:
            num1 = float(input("Escribe la base:"))
            num2 = float(input("Escribe el exponente:"))
            print(f"Resultado {num1}^{num2} = ", num1**num2)
            input("CONTINUAR..."), os.system("cls"), Calculadora.mostrar(self)
        except ValueError:
            os.system("cls"), print("Desbes ingresar valores numericos")

    def ValorAbsoluto(self):
        try:

            numero = float(input("Escribe un numero: "))
            print(f"El valor absoluto de {numero} es = {abs(numero)}")

        except ValueError:
            os.system("cls"), print("Debes escribir un numero!"), CalEstandar.ValorAbsoluto(self)


class CalCientifica(Calculadora):

        def __init__(self, numero1, numero2):
                super().__init__(numero1, numero2)

        def circunferencia(self):
            try:
                os.system("cls")
                from math import pi
                r = float(input("Radio: "))
                circ = 2 * pi * r
                print("La circuferecia es: {:.2f}".format(circ))
                input("CONTINUAR..."), os.system("cls"), Calculadora.mostrar(self)
            except ValueError:
                os.system("cls"), print("Desbes escribir un numero!"), CalCientifica.circunferencia(self)

        def areaCirculo(self):
            try:
                os.system("cls")
                from math import pi
                r = float(input("Radio: "))
                area = pi * r ** 2
                print(f"El area es: {area}")
                input("CONTINUAR...")
                os.system("cls"), Calculadora.mostrar(self)
            except ValueError:
                os.system("cls"), print('Debes escribir un numero!'), CalCientifica.circunferencia(self)

        def areaCuadrado(self):
            try:
                os.system("cls")
                lado = float(input("Escribe el lado del cuadrado: "))
                area = lado ** 2
                print(f"El area es: {area}")
                input("CONTINUAR..."), os.system("cls"), Calculadora.mostrar(self)
            except ValueError:
                os.system("cls"), print("Desbes escribir un numero!"), CalCientifica.areaCuadrado(self)
