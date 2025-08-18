tarefas = [
    ['Comprar pão'],
    ['Comprar Sorvete'],
    ['Comprar Maçã'],
    ['Trocar óleo do carro'],
    ['Pagar fatura Pós']]


while True:
    print("=== Gerenciador de Tarefas ===")
    print("1 - Adicionar Tarefa")
    print("2 - Concluir Tarefa")
    print("3 - Listar Tarefas")
    print("0 - Sair")

    op = int(input("Escolha: "))

    if op == 1:
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefas)

    elif op == 2:
        for i, t in enumerate('tarefas'):
            print(f"[{i}] {t}")
        idx = int(input("Digite o número da tarefa concluída: "))
        if 0 <= idx < len(tarefas):
            del tarefas[idx]
        else:
            print("Número inválido!")
    elif op == 3:
        for i, t in enumerate(tarefas):
            print(f"[{i}] {t}")
    elif op == 0:
        break
    else:
        print("Opção inválida!")