import json
import os

from lib.msgs import msg_sucesso, msg_erro


def criar_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=4, ensure_ascii=False)
            msg_sucesso('Arquivo criado.')

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_arquivo = json.load(arquivo)
            return dados_arquivo
    except FileNotFoundError:
        msg_erro('Arquivo não encontrado.')
        return []
    except json.decoder.JSONDecodeError:
        msg_erro('Arquivo JSON inválido ou vazio.')
        return []

def salvar_arquivo(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    except Exception as erro:
        msg_erro(f'Erro ao salvar arquivo: {erro}')
