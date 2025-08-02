def listar_sh(lista):

    tam_sh = len(lista)
    for i in range(tam_sh):
        print(f'[{i}] - {lista[i][0]} - {lista[i][1]}')

lista_sh = [['Batman', 'inteligencia'],['Super-Homem', 'força'], ['Flash', 'Velocidade'], ['Mulher Maravilha', 'força']]

while True:
    print('=== Sistema de Super Hero===')
    print('1 - Cadastrar um Super Hero')
    print('2 - Alterar um Super Hero')
    print('3 - Deletar um Super Hero')
    print('4 - Listar um Super Hero')
    print('0 Sair do Sistema')


    op = int(input('Digite a opção desejada: '))

    if op == 1:
        print('### CADASTRO DE SUPER HERO ###')
        nome = input('Digite o nome do super hero:')
        skill = input('Digite a skill do super hero:')
        lista_sh.append([nome, skill])

    elif op == 2:
       print("### ALTERAR UM SUPER HERO ###")
       listar_sh(lista_sh)

       op_alt = int(input('Digite o herói a ser alterado: '))
       nome = input('Digite o novo nome do super hero:')
       skill = input('Digite a nova skill do super hero:')
       lista_sh[op_alt] = [nome, skill]


    elif op == 3:
        print("### DELETAR UM SUPER HERO ###")

        listar_sh(lista_sh)
        op_del = int(input('Digite o herói a ser deletado: '))
        del lista_sh[op_del]

    elif op == 4:
        print('### LISTA DE SUPER HEROS ###')
        listar_sh(lista_sh)

    elif op == 0:
        print ("Saindo do sistema")

        break

    else:
        print ('Digte uma opção válida!:')



