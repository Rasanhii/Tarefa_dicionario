# Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.



def chave_maior_valor(dicionario):
    chave_max = None
    valor_max = float('-inf') # inicializa com um valor muito baixo
    for chave, valor in dicionario.items():
        if valor > valor_max:
            chave_max = chave
            valor_max = valor
    return chave_max

dicionario = {'a': 10, 'b': 5, 'c': 20}
chave = chave_maior_valor(dicionario)
print(chave) # imprime 'c'

