# Escreva uma função que receba Nome e Idade. Retorne valores que contêm a chave "idade" e cujo valor é maior que 18.
dicionario = {}

def m_chave():
    while True:
        nome = input('Digite um nome (digite "fim"): ')
        if nome == '' or nome == 'fim':
            break
        idade = int(input(f'Digite a idade de {nome}: '))
        dicionario[nome] = {'idade':idade}

         
    for nome, maior in dicionario.items():
        if maior['idade'] >= 18:
            maior_18 = maior['idade']
            print(f'Nome: {nome}\nIdade:{maior_18}\n')

m_chave()