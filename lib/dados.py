from datetime import datetime
from nanoid import generate

from lib.arquivos import salvar_arquivo, ler_arquivo
from lib.interface import resumo_da_transação


def adicionar_receita(nome_arquivo, tipo, categoria, descricao, valor):
    alfabeto = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    id_transacao = generate(alfabeto, 8)
    tipo_transacao = tipo.upper()
    categoria_transacao = categoria.upper()
    descricao_transacao = descricao.upper()
    valor_transacao = valor
    data_transacao = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    receita = {
        'id_transacao': id_transacao,
        'tipo_transacao': tipo_transacao,
        'categoria_transacao': categoria_transacao,
        'descricao_transacao': descricao_transacao,
        'valor_transacao': valor_transacao,
        'data_transacao': data_transacao
    }
    dados_receita = list()
    dados_receita.append(receita)
    dados = ler_arquivo(nome_arquivo)
    dados.append(receita)
    salvar_arquivo(nome_arquivo, dados)
    resumo_da_transação(dados_receita)

def adicionar_despesa(nome_arquivo, tipo, categoria, descricao, valor):
    alfabeto = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    id_transacao = generate(alfabeto, 8)
    tipo_transacao = tipo.upper()
    categoria_transacao = categoria.upper()
    descricao_transacao = descricao.upper()
    valor_transacao = valor
    data_transacao = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    despesa = {
        'id_transacao': id_transacao,
        'tipo_transacao': tipo_transacao,
        'categoria_transacao': categoria_transacao,
        'descricao_transacao': descricao_transacao,
        'valor_transacao': valor_transacao,
        'data_transacao': data_transacao
    }
    dados_despesa = list()
    dados_despesa.append(despesa)
    dados = ler_arquivo(nome_arquivo)
    dados.append(despesa)
    salvar_arquivo(nome_arquivo, dados)
    resumo_da_transação(dados_despesa)

def remover_transacao(nome_arquivo, id_transacao):
    dados = ler_arquivo(nome_arquivo)
    dados_filtrados = []
    id_encontrado = False
    dados_exclusao = list()
    for transacao in dados:
        if transacao['id_transacao'] == id_transacao:
            id_encontrado = True
            dados_exclusao.append(transacao)
        if transacao['id_transacao'] != id_transacao:
            dados_filtrados.append(transacao)
    salvar_arquivo(nome_arquivo, dados_filtrados)
    resumo_da_transação(dados_exclusao, busca_id=True)
    return id_encontrado

def ver_saldo(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    saldo = 0
    saldo_receitas = 0
    saldo_despesas = 0
    for dado in dados:
        if dado['tipo_transacao'] == 'RECEITA':
            saldo_receitas += dado['valor_transacao']
            saldo += dado['valor_transacao']
        if dado['tipo_transacao'] == 'DESPESA':
            saldo_despesas += dado['valor_transacao']
            saldo -= dado['valor_transacao']
    return saldo_receitas, saldo_despesas, saldo

def quantidade_por_categoria(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    dados_categorias = {
        'ALIMENTAÇÃO': 0,
        'TRANSPORTE': 0,
        'MORADIA': 0,
        'LAZER': 0,
        'SAUDE': 0,
        'SALARIO': 0,
        'OUTROS': 0
    }
    for dado in dados:
        categoria = dado['categoria_transacao']
        if categoria in dados_categorias:
            dados_categorias[categoria] += 1
    return dados_categorias
