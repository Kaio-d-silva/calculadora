from recebe_numero import recebe_numero

def executa_calculadora(input_um, input_dois, operacao):
    operacao = input(f'\nDigite o simbolo da operação Matemática\n')
    if operacao == 'exit':
        return input_um, input_dois, operacao
    
    input_um = recebe_numero('Digite o primeiro valor: ')
    if input_um == 'exit':
        return input_um, input_dois, operacao
    if operacao !=  'raiz':
        input_dois = recebe_numero('\nDigite o segundo valor:' )
        if input_dois == 'exit':
            return input_um, input_dois, operacao
        
        
    return input_um, input_dois, operacao

