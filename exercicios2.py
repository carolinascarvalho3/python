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

    def valores(self, num1, num2):
        num1 = 10
        num2 = 20

        num1, num2 = num2, num1

    def antecessor(self):
        num1 = int(input('Digite um número: '))

        num2 = num1 - 1

        return num2

    def retangulo(self, base, altura, area):
        base = int(input('Digite um número: '))
        altura = int(input('Digite um número: '))

        area = base * altura * altura
        return area
    def calculoIdade(self, idade, meses, anos, dias, nasc):
        diasTot = (anos * 365) + (meses * 30) + dias

        idade = ""
        meses = ""
        anos = ""
        dias = ""

        idade_em_dias = (anos, meses, dias)
        return diasTot
    def eleitores(self, brancos, nulos, validos, pBrancos, pNulos, pValidos, eleitores):

        eleitores = int(input('Digite o número total de eleitores: '))
        brancos = int(input('Digite o número total de brancos: '))
        nulos = int(input('Digite o número total de nulos: '))
        validos = int(input('Digite o número total de validos: '))

        pBrancos = (brancos * 100) /eleitores
        pNulos = (nulos * 100) /eleitores
        pvalidos = (validos * 100) /eleitores

    def salarioMensal(self, salAtu, novoSal, per):

        salAtu = int(input('Informe o salário atual: '))
        novoSal = salAtu + (salAtu *10/100)

        return novoSal

    def custoDecarro(self, custoFabrica, pDistribuidor,pImpostos, cutoCarro):

       custoFabrica = ""
       pDistribuidor = ""
       pImpostos = ""
       custoCarro = ""

       custoFabrica = int(input('Qual o custo de fábrica: '))
       pDistribuidor = int(pDistribuidor * 100) /custoFabrica
       pImpostos = int(pImpostos * 100) /custoFabrica
       custoCarro = (pImpostos + pDistribuidor + custoFabrica)

       return custoCarro

    def notas(self, nota1, nota2, nota3, media):

        nota1 = int("")
        nota2 = int("")
        nota3 = int("")
        media = int(nota1 + nota2 + nota3)/3

        int(input('Digite a primeira nota: '))
        int(input('Digite a segunda nota: '))
        int(input('Digite a terceira nota: '))

        if nota1 >= 8 and nota3 >=8:
            'Aluno Aprovado'
        if nota1 <8 and nota3 >=5:
            'Alubo em Recuperação'
        else: 'Aluno Reprovado'

    def macas(self):

        mac = int("")
        duzia = float("")
        total = float("")
        num = ""

        num = int(input('Quantas maçãs foram compradas? : '))

        if mac < 12:
            total = (mac * 1.30)
        else: total = (duzia * 1.00)

        return total

    def lerValores(self, cont):
        cont = 0
        while True:
         print(cont)
         cont =+1
         if cont >= 10:
          break

        return cont

    def salarioVendedor(self, salFixo, pComissao, salTotal, totVendas):

        salFixo = ""
        pComissao = ""
        salTotal = ""
        totVendas = float("")

        salFixo = (int(input('Digite o salario fixo')))

        if totVendas == 1.500:
            totVendas = (totVendas * 3) /100
        pComissao = (totVendas * 3)/100

        if totVendas > 1.500:
            totVendas = (totVendas * 5)/100
            salTotal = totVendas, salFixo
            return salTotal

    def extratoBanco(self):

        contCli = int(input('Digite o número de sua conta e dígito'))
        saldo = float(10.00)
        debito = float(-50.00)
        credito = float(1.430)

        saldAtu = (saldo - debito + credito)
        if saldAtu < 0:
         return saldAtu, 'Saldo Negativo'
        if saldAtu > 0:
         return saldAtu, 'Saldo Positivo!'

    def tabuadaUsuario(self):

     num1 = int(input('Digite um número entre 1 a 10: '))
     for i in range(1,11):
        print(f'{num1} x {i} = {num1 * i}')
        return i

    def imprimirValores(self):

        valor1 = int(input('Digite um valor: '))
        cont = 1
        while True:
            print(cont)
            cont = +1
            if cont == valor1:
                break

        return cont

    def ler10(self):

       neg = 0
       for i in range(1,11):
        valor = float(input('Digite um valor: '))
        if valor < 0:
                neg =+ 1

    def somar40(self):

        soma = 0
        numero = 0
        for i in range(1,11):
          numero = float(input('Digite um número: '))
        if soma < 40 :
          soma += numero

    def mediaAritmetica(self):

        mediaAri =  0
        quantidade = 0

        for i in range(15, 100):
            mediaAri += i
            quantidade += 1
            media = mediaAri / quantidade

    def quantidade(self):
        quantidade = int(input('Digite a quantidade de números: '))

        numeros = {}
        soma = 0

        for i in range(quantidade):
            numero = int(input('Digite um números: '))

            numeros[numero] = soma
            soma += numero

            media = soma / quantidade

            maiorNumero = max(numeros)








