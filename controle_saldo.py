"""Funções de saldo e utilitários de leitura/escrita de JSON."""
import json
import os

ARQUIVO_CADASTRO = "cadastro.json"


def ler_json(caminho):
    """Lê uma lista de registros de um JSON. Retorna [] se o arquivo não existir."""
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return []


def salvar_json(caminho, dados):
    """Grava a lista de registros no arquivo JSON (criando-o se necessário)."""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def adicionar_registro(caminho, registro):
    """Adiciona um registro ao final da lista, mantendo os anteriores."""
    dados = ler_json(caminho)
    dados.append(registro)
    salvar_json(caminho, dados)


def ler_valor(mensagem):
    """Pede um valor numérico ao usuário. Retorna None se for inválido."""
    texto = input(mensagem).strip().replace(",", ".")
    try:
        return round(float(texto), 2)
    except ValueError:
        print("Valor inválido.")
        return None


def consultar_saldo(cpf):
    """Retorna o saldo do usuário com o CPF informado, ou None se não existir."""
    for usuario in ler_json(ARQUIVO_CADASTRO):
        if usuario["cpf"] == cpf:
            return usuario["saldo"]
    return None


def atualizar_saldo(cpf, novo_saldo):
    """Atualiza o saldo do usuário. Retorna True se conseguiu, False se não achou."""
    usuarios = ler_json(ARQUIVO_CADASTRO)
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario["saldo"] = round(novo_saldo, 2)
            salvar_json(ARQUIVO_CADASTRO, usuarios)
            return True
    return False
