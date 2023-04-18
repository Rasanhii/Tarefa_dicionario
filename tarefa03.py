# Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores
# Retorna um dicionário criado a partir dessas listas.

def criar_dicionario(chaves, valores):
    dicionario = {}
    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i]
    return dicionario

criar_dicionario()