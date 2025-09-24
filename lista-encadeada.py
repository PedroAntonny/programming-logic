lista = None

def exibeLista():
    if not lista:
        print('Lista vazia.')
        return
    elemento = lista

    while elemento != None:
        print(elemento['valor'], end=' ')
        elemento = elemento['proximo']

    print('.')

def adicionaNoFim(elemento):
    global lista
    if not lista:
        lista = { 'valor': elemento, 'proximo': None }
        return  
    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual['proximo'] = { 'valor': elemento, 'proximo': None }                  

exibeLista()
print('Adicionando o 7...')
adicionaNoFim(7)
exibeLista()
print('Adicionando o 9...')
adicionaNoFim(9)
print('Adicionando o 15...')
adicionaNoFim(15)
print('Adicionando o 16...')
adicionaNoFim(16)
exibeLista()

