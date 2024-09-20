from exercicios2 import Exercicios2

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer  = Exercicios2()
        self.num1  = 0
        self.num2  = 0


    def mostrarMenu2(self):
            print('\n------Menu-----\n\n'           +
                  'Escolha uma das opções abaixo: ' +
                  '\n0. Sair'                       +
                  '\n1. Imprimir Números'           +
                  '\n2. Pares'                      +
                  '\n3. Soma de 100'                +
                  '\n4. Múltiplos '                 +
                  '\n5. Par ou Ímpar'               +
                  '\n6. Positivo ou Negativo'       +
                  '\n7. Tabuada'                    +
                  '\n8. Tabuada 2'                  +
                  '\n9. Somar'                      +
                  '\n10. Primo'                     +
                  '\n11. Valores'                   +
                  '\n12. Antecessor'                +
                  '\n13. Retângulo'                 +
                  '\n14. Cálculo da Idade'          +
                  '\n15. Eleitores'                 +
                  '\n16. Salário Mensal'            +
                  '\n17. Custo de um Carro'         +
                  '\n18. Três Notas'                +
                  '\n19. Maçãs Compradas'           +
                  '\n20. Ler Valores'               +
                  '\n21. Salário Vendedor'          +
                  '\n22. Extrato de Banco'          +
                  '\n23. Tabuada Usuário'           +
                  '\n24. Imprimir Valores'          +
                  '\n25. Ler 10'                    )

    def coletar(self):
            self.num1 = int(input('Informe o primeiro número:  '))
            self.num2 = int(input('Informe o segundo número:  '))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu2() #chamando as opções
            self.opcao = int(input('Escolha uma das opções acima:  '))
            if self.opcao == 0:
                print(f'Obrigado')

            if self.\
                    opcao == 1:
                self.coletar() #Chamando o input por meio do coletar
                print(f'Os números de 0 a 10 são estes: {self.exer.imprimirNumeros()}')
            elif self.opcao == 2 :
                print(f'Os números pares até 20 são: {self.exer.pares()}')
            elif self.opcao == 3:
                print(f'A soma dos números de 1 a 100 é: {self.exer.soma100()}')
            elif self.opcao == 4:
                print(f'Os múltiplos de 5 até 50 números são: {self.exer.multiplos()}')
            elif self.opcao == 5:
                print(f'O número é: {self.exer.parImpar(self.num1)}')
            elif self.opcao == 6:
                self.coletar()
                print(f'O número é: {self.exer.positivoNegativo(self.num1)}')
            elif self.opcao == 7:
                self.coletar()
                print(f'{self.exer.tabuada(self.num1)}')
            elif self.opcao == 8:
                self.coletar()
                print(f'{self.exer.tabuada2(self.num1)}')
            elif self.opcao == 9:
                print(f'{self.exer.somar(self.num1)}')
            elif self.opcao == 10:
                print(f'{self.exer.primo20()}')
            elif self.opcao == 11:
                num1 = int(input('Informe um número: '))
                num2 = int(input('Informe um número: '))
                print(f'{self.exer.valores(self.num1, self.num2)}')
            elif self.opcao == 12:
                print(f'O número é: {self.exer.antecessor()}')
            elif self.opcao == 13:
                 print(f'As dimensões do retângulo são: {self.exer.retangulo}')
            elif self.opcao == 14:
                print(f'O cálculo da idade em dias, meses e anos é: {self.exer.calculoIdade}')
            elif self.opcao == 15:
                print(f' O cálculo de votos é: {self.exer.eleitores}')
            elif self.opcao == 16:
                print(f'O salário com reajuste é: {self.exer.salarioMensal}')
            elif self.opcao == 17:
                print(f'O custo de um carro novo é: {self.exer.custoDecarro}')
            elif self.opcao == 18:
                print(f'A média das notas é: {self.exer.notas}')
            elif self.opcao == 19:
                print(f'O preço das maçãs compradas é: {self.exer.macas}')
            elif self.opcao == 20:
                print(f'{self.exer.lerValores}')
            elif self.opcao == 21:
                print(f'O salário total dos vendedores é: {self.exer.salarioVendedor}')
            elif self.opcao == 22:
                print(f'{self.exer.extratoBanco}')
            elif self.opcao == 23:
                print(f'{self.exer.tabuadaUsuario}')
            elif self.opcao == 24:
                print(f'{self.exer.imprimirValores}')
            elif self.opcao == 25:
                print(f'{self.exer.ler10}')






