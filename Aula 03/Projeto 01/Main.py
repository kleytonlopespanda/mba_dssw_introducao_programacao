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
       print("Alterou um Super Hero")

    elif op == 3:
        print("### DELETAR UM SUPER HERO ###")

        tam_sh = len(lista_sh)
        for i in range(tam_sh):
            print(f'[{i}] - {lista_sh[i][0]} - {lista_sh[i][1]}')

        op_del = int(input('Digite o herói a ser deletado: '))

        del lista_sh[op_del]

    elif op == 4:
        print('### LISTA DE SUPER HEROS ###')

        tam_sh = len(lista_sh)
        for i in range(tam_sh):
            print(f'[{i}] - {lista_sh[i][0]} - {lista_sh[i][1]}')

    elif op == 0:
        print ("Saindo do sistema")

        break

    else:
        print ('Digte uma opção válida!:')



