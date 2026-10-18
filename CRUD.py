
print("===== MyLife 1.0 =====")

tarefa = ""
concluida = False

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if tarefa != "":
            print("Já existe uma tarefa cadastrada.")
        else:
            tarefa = input("Digite sua tarefa: ")

            if tarefa == "":
                print("A tarefa não pode estar vazia.")
            else:
                concluida = False
                print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if tarefa == "":
            print("Nenhuma tarefa cadastrada.")
        elif concluida == True:
            print("Tarefa:", tarefa, "- Concluída")
        else:
            print("Tarefa:", tarefa, "- Pendente")

    elif opcao == "3":
        if tarefa == "":
            print("Nenhuma tarefa cadastrada.")
        elif concluida == True:
            print("Essa tarefa já foi concluída.")
        else:
            concluida = True
            print("Tarefa concluída com sucesso!")

    elif opcao == "4":
        if tarefa == "":
            print("Nenhuma tarefa para excluir.")
        else:
            tarefa = ""
            concluida = False
            print("Tarefa excluída com sucesso!")

    elif opcao == "5":
        print("Encerrando o MyLife...")
        break

    else:
        print("Opção inválida!")
