# Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores
# Retorna um dicionário criado a partir dessas listas.

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
        
    print(f'As chaves são: {chave}')
    print(f'Os valores são: {valor}')
    print(dicionario)
    
criar_dicionario()