print("===== MyLife 2.0 =====")


def adicionar_tarefa(tarefas):
    descricao = input("Digite sua tarefa: ").strip()

    if not descricao:
        print("A tarefa não pode estar vazia.")
    else:
        tarefas.append({
            "descricao": descricao,
            "status": "Pendente"
        })
        print("Tarefa adicionada com sucesso!")


def visualizar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n==== TAREFAS ====")

        for indice, tarefa in enumerate(tarefas, start=1):
            print(indice, "-", tarefa["descricao"], "-", tarefa["status"])


def concluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    visualizar_tarefas(tarefas)

    try:
        escolha = int(input("Digite o número da tarefa que deseja concluir: "))
    except ValueError:
        print("Digite um número válido.")
        return

    if escolha < 1 or escolha > len(tarefas):
        print("Opção inválida!")
    elif tarefas[escolha - 1]["status"] == "Concluída":
        print("Essa tarefa já foi concluída.")
    else:
        tarefas[escolha - 1]["status"] = "Concluída"
        print("Tarefa concluída com sucesso!")


def excluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para excluir.")
        return

    visualizar_tarefas(tarefas)

    try:
        escolha = int(input("Digite o número da tarefa que deseja excluir: "))
    except ValueError:
        print("Digite um número válido.")
        return

    if escolha < 1 or escolha > len(tarefas):
        print("Opção inválida!")
    else:
        tarefas.pop(escolha - 1)
        print("Tarefa excluída com sucesso!")


def exibir_menu():
    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            excluir_tarefa(tarefas)
        elif opcao == "5":
            print("Encerrando o MyLife...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
