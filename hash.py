nomes = [
    'João',
    'Antonio',
    'Maria',
    'Saulo',
    'Ana',
    'Pedro',
    'Bianca'
]

tabela = {}

for nome in nomes:
    qtd = len(nome)
    if qtd not in tabela:
        tabela[qtd] = []
    tabela[qtd].append(nome)

print(tabela)        