"""Apostas na roleta (números de 0 a 10)."""
import random

from controle_saldo import (adicionar_registro, atualizar_saldo,
                            consultar_saldo, ler_valor)

ARQUIVO_APOSTAS = "apostas.json"


def apostar():
    print("\n--- Aposta ---")
    cpf = input("CPF: ").strip()
    saldo = consultar_saldo(cpf)
    if saldo is None:
        print("Usuário não encontrado.")
        return

    valor = ler_valor("Valor da aposta: R$ ")
    if valor is None:
        return
    if valor <= 0:
        print("O valor da aposta deve ser maior que zero.")
        return
    if valor > saldo:
        print(f"Saldo insuficiente. Seu saldo é R$ {saldo:.2f}.")
        return

    try:
        escolhido = int(input("Escolha um número entre 0 e 10: "))
    except ValueError:
        print("Número inválido.")
        return
    if not 0 <= escolhido <= 10:
        print("O número deve estar entre 0 e 10.")
        return

    sorteado = random.randint(0, 10)
    print(f"Número sorteado: {sorteado}")

    if escolhido == sorteado:
        resultado = "ganhou"
        valor_obtido = round(valor * 10, 2)
        novo_saldo = saldo - valor + valor_obtido
        print(f"Parabéns, você ganhou R$ {valor_obtido:.2f}!")
    else:
        resultado = "perdeu"
        valor_obtido = 0.0
        novo_saldo = saldo - valor
        print(f"Você perdeu R$ {valor:.2f}.")

    atualizar_saldo(cpf, novo_saldo)
    adicionar_registro(ARQUIVO_APOSTAS, {
        "cpf": cpf,
        "valor_apostado": valor,
        "numero_apostado": escolhido,
        "numero_sorteado": sorteado,
        "resultado": resultado,
        "valor_obtido": valor_obtido,
    })
    print(f"Saldo atual: R$ {novo_saldo:.2f}")
