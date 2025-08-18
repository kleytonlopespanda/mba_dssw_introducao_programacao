agenda = [
    ['Paulo', '88941756'],
    ["Veronica", '84572541'],
    ['André','87452654'],
    ['João', '87452365'],
    ['kleyton', '45129856'],
    ["Barbara", '85234562'],
    ["Lucas" , '85961247'],
    ]

while True:
    print("=== Agenda de Contatos ===")
    print("1 - Adicionar Contato")
    print("2 - Pesquisar Contato")
    print("3 - Listar Contatos")
    print("0 - Sair")

    op = int(input("Escolha: "))

    if op == 1:
        nome = input("Nome: ")
        tel = input("Telefone: ")
        agenda.append([nome, tel])

    elif op == 2:
        busca = input("Digite o nome para pesquisar: ")
        encontrados = [c for c in agenda if busca.lower() in c[0].lower()]
        if encontrados:
            for c in encontrados:
                print(f"{c[0]} - {c[1]}")
        else:
            print("Nenhum contato encontrado.")

    elif op == 3:
        for i, c in enumerate(agenda):
            print(f"[{i}] {c[0]} - {c[1]}")

    elif op == 0:
        print("Saindo do programa...")

        break
    else:
        print("Opção inválida!")
