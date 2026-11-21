
print("===== MyLife 2.0 =====")

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
                tarefas.append({
                    "descricao": descriçao,
                    "status": "Pendente"
                })
                print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
       if tarefas:
         print("\n==== TAREFAS ====")
         print(tarefas)

         for indice, tarefa in enumerate(tarefas, start=1):
            print(indice, "-", tarefa["descricao"], "-", tarefa["status"])
       else:
             print("Nenhuma tarefa cadastrada.")

    elif opcao == "3":
     if tarefas == []:
        print("Nenhuma tarefa cadastrada.")
     else:
        print("\n==== TAREFAS PENDENTES ====")

        pendentes = []

        for indice, tarefa in enumerate(tarefas, start=1):
            if tarefa["status"] == "Pendente":
                pendentes.append((indice, tarefa))
                print(indice, "-", tarefa["descricao"])

        if pendentes == []:
            print("Todas as tarefas já foram concluídas.")
        else:
            escolha = int(input("Digite o número da tarefa que deseja concluir: "))

            if escolha < 1 or escolha > len(tarefas):
                print("Opção inválida!")
            elif tarefas[escolha - 1]["status"] == "Concluída":
                print("Essa tarefa já foi concluída.")
            else:
                tarefas[escolha - 1]["status"] = "Concluída"
                print("Tarefa concluída com sucesso!")
            

    elif opcao == "4":
     if tarefas == []:
        print("Nenhuma tarefa para excluir.")
     else:
        for indice, tarefa in enumerate(tarefas, start=1):
            print(indice, "-", tarefa["descricao"], "-", tarefa["status"])

        escolha = int(input("Digite o número da tarefa que deseja excluir: "))

        if escolha < 1 or escolha > len(tarefas):
            print("Opção inválida!")
        else:
            tarefas.pop(escolha - 1)
            print("Tarefa excluída com sucesso!")

    elif opcao == "5":
        print("Encerrando o MyLife...")
        break

    else:
        print("Opção inválida!")
