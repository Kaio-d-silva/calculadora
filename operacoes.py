import math

def seleciona_operacao(operacao):
    if operacao == '+':
        return soma
    elif operacao == '-':
        return subtrair
    elif operacao == '/':
        return dividir
    elif operacao == '*':
        return multiplicar
    elif operacao == '**':
        return potencia
    elif operacao == '%':
        return porcentagem
    elif operacao == 'mod':
        return mod
    elif operacao == 'raiz':
        return raiz
    elif operacao == '>':
        return maior  
    elif operacao == '<':
        return menor
    elif operacao == '=':
        return igual    
    else:
        return 'Operação não permitida'

def soma(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def dividir(divisor, dividendo):
    return divisor / dividendo

def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def porcentagem(primeiro_numero, segundo_numero):
    return 100/primeiro_numero * segundo_numero

def mod(primeiro_numero, segundo_numero):
    return primeiro_numero % segundo_numero

def raiz(primeiro_numero, segundo_numero):
    return math.sqrt(primeiro_numero)

def potencia(primeiro_numero, segundo_numero):
    return math.pow(primeiro_numero,segundo_numero)

def maior(primeiro_numero, segundo_numero):
    return str (primeiro_numero > segundo_numero)
#        return "true"
#    return 'false'

def menor(primeiro_numero, segundo_numero):
    return str (primeiro_numero < segundo_numero)
#        return "true"
#    return 'false'

def igual(primeiro_numero, segundo_numero):
    return str (primeiro_numero == segundo_numero)
#        return "true"
#    return 'false'




