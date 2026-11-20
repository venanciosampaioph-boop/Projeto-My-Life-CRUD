
print("===== MyLife 1.0 =====")

tarefas = []
tarefas_concluidas = []
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
            for indice, descriçao in enumerate(tarefas, start=1):
                    print(indice, "-", descriçao)

    elif opcao == "3":
        if tarefas == []:
            print("Nenhuma tarefa cadastrada.")
        else:
            for indice, descriçao in enumerate(tarefas, start=1):
                 print(indice, "-", descriçao)

            escolha = int(input("Escolha a tarefa que deseja concluir (digite o número): "))
            if escolha < 1 or escolha > len(tarefas):
             print("Opção inválida!")
            elif escolha in tarefas_concluidas:
             print("Essa tarefa já foi concluída.")
            else:
             tarefas_concluidas.append(tarefas[escolha - 1])
             print("Tarefa concluída com sucesso!")
            

    elif opcao == "4":
        if tarefas == []:
            print("Nenhuma tarefa para excluir.")
        else:
            for indice, descriçao in enumerate(tarefas, start=1):
                print(indice, "-", descriçao)
            escolha = int(input("Digite o número da tarefa que deseja excluir: "))
            if escolha <1 or escolha > len(tarefas):
                    print("Opção inválida!")
            else:
                    tarefas.pop(escolha - 1)
                    print("Tarefa excluída com sucesso!")

    elif opcao == "5":
        print("Encerrando o MyLife...")
        break

    else:
        print("Opção inválida!")
