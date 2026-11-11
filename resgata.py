"""Resgate (saque) de saldo."""
from controle_saldo import (adicionar_registro, atualizar_saldo,
                            consultar_saldo, ler_valor)

ARQUIVO_SAQUES = "saques.json"


def resgatar():
    print("\n--- Resgate ---")
    cpf = input("CPF: ").strip()
    saldo = consultar_saldo(cpf)
    if saldo is None:
        print("Usuário não encontrado.")
        return

    valor = ler_valor("Valor do resgate: R$ ")
    if valor is None:
        return
    if valor <= 0:
        print("O valor do resgate deve ser maior que zero.")
        return
    if valor > saldo:
        print(f"Saldo insuficiente. Seu saldo é R$ {saldo:.2f}.")
        return

    atualizar_saldo(cpf, saldo - valor)
    adicionar_registro(ARQUIVO_SAQUES, {"cpf": cpf, "valor_saque": valor})
    print(f"Resgate realizado! Novo saldo: R$ {saldo - valor:.2f}")
