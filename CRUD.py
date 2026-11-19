
print("===== MyLife 1.0 =====")

tarefas = []
while True:
    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
       
        descriçao = input("Digite sua tarefa: ")

        if descriçao == "":
             print("A tarefa não pode estar vazia.")
        else:
                tarefas.append(descriçao)
                print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if tarefas == []:
            print("Nenhuma tarefa cadastrada.")
       
        else:
            for descriçao in tarefas:
                print("Tarefa:", descriçao)

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
