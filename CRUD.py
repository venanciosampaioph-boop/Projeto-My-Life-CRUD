print("===== MyLife 2.0 =====")


def adicionar_tarefa(tarefas):
    descricao = input("Digite sua tarefa: ").strip()

    if not descricao:
        print("A tarefa não pode estar vazia.")
        return

    tarefas.append({
        "descricao": descricao,
        "status": "Pendente"
    })
    print("Tarefa adicionada com sucesso!")


def exibir_tarefas_recursivo(tarefas, indice=0):
    if indice == len(tarefas):
        return

    tarefa = tarefas[indice]
    print(indice + 1, "-", tarefa["descricao"], "-", tarefa["status"])

    exibir_tarefas_recursivo(tarefas, indice + 1)


def visualizar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n==== TAREFAS ====")
    exibir_tarefas_recursivo(tarefas)


def solicitar_indice_tarefa(tarefas, mensagem):
    try:
        escolha = int(input(mensagem))
    except ValueError:
        print("Digite um número válido.")
        return None

    if escolha < 1 or escolha > len(tarefas):
        print("Opção inválida!")
        return None

    return escolha - 1


def concluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    visualizar_tarefas(tarefas)
    indice = solicitar_indice_tarefa(
        tarefas,
        "Digite o número da tarefa que deseja concluir: "
    )

    if indice is None:
        return

    if tarefas[indice]["status"] == "Concluída":
        print("Essa tarefa já foi concluída.")
        return

    tarefas[indice]["status"] = "Concluída"
    print("Tarefa concluída com sucesso!")


def excluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para excluir.")
        return

    visualizar_tarefas(tarefas)
    indice = solicitar_indice_tarefa(
        tarefas,
        "Digite o número da tarefa que deseja excluir: "
    )

    if indice is None:
        return

    tarefas.pop(indice)
    print("Tarefa excluída com sucesso!")


def exibir_menu():
    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

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
