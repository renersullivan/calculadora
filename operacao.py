from calculadora.calc import Calculadora
from sair import Saida

class Calc:
    def operacao():
        operation = input('''
        :
        + para adição
        - para subtração
        * para multiplicação
        / para divisão
        [S] para sair 
        :  ''')
        if operation == '+' :
            Calculadora.soma()
         
        if operation == '-':
            Calculadora.subtracao()
            
        if operation == '*':
            Calculadora.multiplicacao()
           
        if operation == '/':
            Calculadora.divisao()
            
        if operation != 'S':
             Calc.operacao()

        if operation == 'S':
            Saida.saindo()   
 


