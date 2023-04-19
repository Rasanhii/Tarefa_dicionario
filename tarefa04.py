# Escreva uma função que receba um dicionário como entrada e retorna duas listas. Uma com chave e outra com valor.

dicionario = {}

def criar_dicionario():
    while True:
        chave = input('Digite uma chave (ou digite "fim"): ')
        if chave == '' or chave == 'fim':
            break
        valor = int(input('Digite um número para a chave: '))
        if valor == '' or chave == 'fim':
            break
        dicionario[chave] = valor
        
        
    for i in dicionario.keys():
        print(f'As chaves são: {i}' )
    for i in dicionario.keys():
        print(f'Os valores são: {dicionario[i]}')
    
criar_dicionario()