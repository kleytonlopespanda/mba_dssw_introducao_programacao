#faça um programa gertenciador de notas de alunos, onde vc pode adicionar, mudar, excluir as notas

notas = [['Alexandre', 'Nota: 10'],
         ['Andre', 'Nota: 9'],
         ['Gustavo', 'Nota: 8'],
         ['Barbara', 'Nota: 10'],
         ['Francisco', 'Nota: 7']]

while True:
    print('1- Adicionar Nota')
    print('2- Alterar Nota')
    print('3- Excluir Nota')
    print('4- Listar Nota')
    print('0- Sair')
    op = int(input('Digite a opção desejada: '))

    if op == 1:
        nome = input('Digite o nome do aluno: ')
        nota = input('Digite a nota do aluno: ')
        notas.append([nome, nota])

    elif op == 2:
        for i, n in enumerate
            print(f'[{i}] {n}')

    elif op == 3:
        for i, n in enumerate
            print(f'[{i}] {n}')

    elif op == 4:
