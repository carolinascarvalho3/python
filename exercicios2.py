class Exercicios2:
    def __init__(self):
        self.num  = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def imprimirNumeros(self):
        msg = ""
        for i in range(1,11,1):
          msg +=f'\n{i}'
        return msg

    def pares(self):
        par = ""
        for i in range(1,21):
            if i % 2 == 0:
             par += f'\n{i}'
        return par

    def soma100(self):
        cem = 50 * 101
        return cem

    def multiplos(self):
        mul = ""
        for i in range(5,51,5):
            mul += f'\n{i}'
        return mul

    def parImpar(self, num1):
        input('Informe um número')
        if num1 % 2 == 0:
          return 'Par'
        else:
          return 'Ímpar'
    def positivoNegativo(self, num1):
        input('Informe um número')
        if num1 <0:
            return 'Negativo'
        else: return 'Positivo'

    def tabuada(self, num1):
        resultado = ""
        for i in range(0,11,1):
            resultado+= f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def tabuada2(self, num1):
        resultado = ""
        for i in range(0,num1,1):
            resultado+= f'\n{num1} * {i} = {num1 * i}'
        return resultado
    def somar(self, num1):
        input('Informe um número: ')
        resultado = ""
        for i in range(0,num1,1):
            resultado+= f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def primo20(self):
        primo = '1\n2\n3\n5'
        for i in range(5,21,1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo+=f'\n{i}'
        return primo

    def primo(self, num1):
        num1 = int(input('Digite um número: '))
        for i in range(1, num1 + 1):
            if num1 % i == 0:
                print('É primo')
            else:
                print('Não é primo')



