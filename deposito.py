"""Depósitos."""
from controle_saldo import (adicionar_registro, atualizar_saldo,
                            consultar_saldo, ler_valor)

ARQUIVO_DEPOSITOS = "depositos.json"


def depositar():
    print("\n--- Depósito ---")
    cpf = input("CPF: ").strip()
    saldo = consultar_saldo(cpf)
    if saldo is None:
        print("Usuário não encontrado.")
        return

    valor = ler_valor("Valor do depósito: R$ ")
    if valor is None:
        return
    if valor <= 0:
        print("O valor do depósito deve ser maior que zero.")
        return

    atualizar_saldo(cpf, saldo + valor)
    adicionar_registro(ARQUIVO_DEPOSITOS, {"cpf": cpf, "valor_deposito": valor})
    print(f"Depósito realizado! Novo saldo: R$ {saldo + valor:.2f}")
