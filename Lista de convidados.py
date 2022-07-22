print ("Programa LISTA DE CONVIDADOS")
pw = 0
senha = '123456'
nome = input('digite o nome de usuario: ')
while (pw != senha):
    pw = input('Digite sua senha: ')
    if senha == pw:
        print("Senha correta")
    else:
        print('Sua incorreta. Tente novamente')
print ('Bem vindo',nome,'\nVocê entrou no sistema.')
lista_nomes = ['Andre', 'Thiago', 'João', 'Lucas']
resp = 0
S = str('s')
while (resp != S):
    print('Deseja imprimir sua lista de convidados?')
    resp = str(input('Digite S/N:'))
    if resp == S:
        print(lista_nomes)
        print('Programa finalizado')
    else:
        print('Programa finalizado')
        break
