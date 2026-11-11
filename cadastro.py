"""Cadastro de usuários."""
from controle_saldo import ARQUIVO_CADASTRO, ler_json, adicionar_registro


def cpf_ja_cadastrado(cpf):
    return any(u["cpf"] == cpf for u in ler_json(ARQUIVO_CADASTRO))


def cadastrar_usuario():
    print("\n--- Cadastro de usuário ---")
    nome = input("Nome: ").strip()
    cpf = input("CPF (somente números): ").strip()

    if not nome or not cpf:
        print("Nome e CPF são obrigatórios.")
        return
    if cpf_ja_cadastrado(cpf):
        print("Esse CPF já está cadastrado.")
        return

    adicionar_registro(ARQUIVO_CADASTRO, {"nome": nome, "cpf": cpf, "saldo": 0.0})
    print(f"Usuário {nome} cadastrado com sucesso!")
