"""Roleta UNIRPIX - menu principal."""
import aposta
import cadastro
import deposito
import resgata
from controle_saldo import consultar_saldo


def mostrar_saldo():
    print("\n--- Consultar saldo ---")
    cpf = input("CPF: ").strip()
    saldo = consultar_saldo(cpf)
    if saldo is None:
        print("Usuário não encontrado.")
    else:
        print(f"Saldo atual: R$ {saldo:.2f}")


def menu():
    while True:
        print("\n===== ROLETA UNIRPIX =====")
        print("1. Cadastrar usuário")
        print("2. Depositar dinheiro")
        print("3. Realizar aposta")
        print("4. Resgatar saldo")
        print("5. Consultar saldo")
        print("6. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastro.cadastrar_usuario()
        elif opcao == "2":
            deposito.depositar()
        elif opcao == "3":
            aposta.apostar()
        elif opcao == "4":
            resgata.resgatar()
        elif opcao == "5":
            mostrar_saldo()
        elif opcao == "6":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
