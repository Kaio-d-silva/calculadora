from operacoes import seleciona_operacao
from executa_calculadora import executa_calculadora
from texto import texto 



print(texto())


saida = ''
input_um = 0
input_dois = 0
operacao = ''

while saida != 'exit':
    (input_um, input_dois, operacao) = executa_calculadora(input_um, input_dois, operacao)

    if input_um == 'exit' or input_dois == 'exit' or operacao  == 'exit':
        saida = 'exit'
    if saida != 'exit':
        resultado = ''
        
        operacao_selecionada = seleciona_operacao(operacao)

        if callable(operacao_selecionada):
            resultado = operacao_selecionada(input_um, input_dois)
        else:
            print(operacao_selecionada)

        if resultado != '':
            if resultado == "True":
                print(f'\nO valor de {input_um} é {operacao} {input_dois}')
            elif resultado == "False":
                print(f'\nO valor de {input_um} não é {operacao} {input_dois}')
            else:
                print(f'\nO resultado da operação {operacao} é: {resultado}\n')