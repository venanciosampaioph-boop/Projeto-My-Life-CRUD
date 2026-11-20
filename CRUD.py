
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
        tarefas_pendentes = []

        for descricao in tarefas:
            if descricao not in tarefas_concluidas:
                tarefas_pendentes.append(descricao)

        if tarefas_pendentes:
            print("\n====TAREFAS PENDENTES====")
            for indice, descricao in enumerate(tarefas_pendentes, start=1):
                print(indice, "-", descricao)
        else:
            print("Nenhuma tarefa pendente.")

        if tarefas_concluidas:
            print("\n====TAREFAS CONCLUIDAS====")
            for indice, descricao in enumerate(tarefas_concluidas, start=1):
                print(indice, "-", descricao)

    elif opcao == "3":
        if tarefas == []:
            print("Nenhuma tarefa cadastrada.")
        else:
             tarefas_pendentes = []

             contador = 1

             for descricao in tarefas:
                 if descricao not in tarefas_concluidas:
                     tarefas_pendentes.append(descricao)
                     print(contador, "-", descricao)
                     contador += 1

             if tarefas_pendentes == []:
               print("Todas as tarefas já foram concluídas.")
             else:
                escolha = int(input("Escolha a tarefa que deseja concluir (digite o número): "))

                if escolha < 1 or escolha > len(tarefas_pendentes):
                   print("Opção inválida!")
                else:
                     tarefas_concluidas.append(tarefas_pendentes[escolha - 1])
                     print("Tarefa concluída com sucesso!")
            

    elif opcao == "4":
        if tarefas == []:
            print("Nenhuma tarefa para excluir.")
        else:
            for indice, descricao in enumerate(tarefas, start=1):
                print(indice, "-", descricao)

            escolha = int(input("Digite o número da tarefa que deseja excluir: "))

            if escolha < 1 or escolha > len(tarefas):
                print("Opção inválida!")
            else:
                tarefa_excluida = tarefas.pop(escolha - 1)

                if tarefa_excluida in tarefas_concluidas:
                    tarefas_concluidas.remove(tarefa_excluida)

                print("Tarefa excluída com sucesso!")

    elif opcao == "5":
        print("Encerrando o MyLife...")
        break

    else:
        print("Opção inválida!")
