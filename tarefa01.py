# Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.

dicionario = {}

def m_chave():
    while True:
        chave = input('Digite uma chave (digite "fim"): ')
        if chave == '' or chave == 'fim':
            break
        valor = int(input('Digite um número para a chave: '))
        dicionario[chave] = valor


    srfantastico = None
    sus = 0
         
    for chave, valor in dicionario.items():
        if valor > sus:
            srfantastico = chave
            sus = valor
    print(srfantastico)

m_chave()