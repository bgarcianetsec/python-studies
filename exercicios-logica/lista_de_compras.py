"""
ENUNCIADO: Gestão de Lista de Compras com Tratamento de Erros

O objetivo é criar uma aplicação de terminal que permita ao usuário gerenciar 
uma lista de compras, garantindo que o programa não pare de funcionar caso 
o usuário digite valores inválidos ou índices inexistentes.

Funcionalidades:
1. Inserir itens à lista.
2. Apagar itens baseando-se no índice (número da linha).
3. Listar todos os itens com seus respectivos índices.
4. Prevenção de erros de ValueError (letras onde se espera números) e IndexError.
"""

# Inicialização da lista
lista_compras = []

print("-" * 40)
print(f"{'LISTA DE COMPRAS DIGITAL':^40}")
print("-" * 40)

while True:
    print("\nMENU DE OPÇÕES:")
    print("[1] - Inserir item")
    print("[2] - Deletar item (Índice)")
    print("[3] - Listar itens")
    print("[4] - Sair")

    try:
        # Etapa 1: Coleta e validação da opção do menu
        entrada_opcao = input("\nEscolha uma opção: ")
        opcao = int(entrada_opcao)

    except ValueError:
        print("\n[ERRO] Por favor, digite um número inteiro entre 1 e 4.")
        continue

    # Opção 1: Adicionar item
    if opcao == 1:
        novo_item = input("Nome do item: ").strip()
        if novo_item:
            lista_compras.append(novo_item)
            print(f"✅ '{novo_item}' adicionado!")
        else:
            print("⚠️ Não é possível adicionar um item vazio.")

    # Opção 2: Excluir item por índice
    elif opcao == 2:
        if not lista_compras:
            print("⚠️ A lista está vazia. Nada para excluir.")
            continue

        try:
            indice_str = input("Digite o índice para apagar: ")
            indice = int(indice_str)
            item_removido = lista_compras.pop(indice)
            print(f"🗑️ Item '{item_removido}' removido com sucesso.")

        except ValueError:
            print("⚠️ Erro: Digite um número inteiro válido.")
        except IndexError:
            print("⚠️ Erro: Esse índice não existe na lista.")

    # Opção 3: Listar itens
    elif opcao == 3:
        if not lista_compras:
            print("\n📭 Sua lista está vazia no momento.")
        else:
            print("\n--- ITENS NA LISTA ---")
            for i, item in enumerate(lista_compras):
                print(f"{i} | {item}")
            print("-" * 22)

    # Opção 4: Encerrar programa
    elif opcao == 4:
        print("\nEncerrando aplicação. Boas compras!")
        break

    else:
        print("⚠️ Opção inexistente. Tente novamente.")
        






    

    


