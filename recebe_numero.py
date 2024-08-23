from decimal import Decimal

def recebe_numero(texto): #-> Decimal|str|int:
    input_var = input(f'{texto} \n')
    input_var = int(input_var) if input_var != 'exit' else input_var
    return input_var