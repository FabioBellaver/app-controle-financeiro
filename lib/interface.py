from lib.arquivos import ler_arquivo
from lib.msgs import msg_erro, msg_alerta, msg_sucesso
from lib.util import validar_numeros_inteiros, formatar_para_real
from lib.cores import cores


def titulo_app(txt):
    print(f'{cores["cz"]}~{cores["limpa"]}' * 120)
    print(f'{cores["az"]}{txt.center(120).upper()}{cores["limpa"]}')
    print(f'{cores["cz"]}~{cores["limpa"]}' * 120)

def titulo(txt):
    print(f'{cores["az"]}{txt.center(120).upper()}{cores["limpa"]}')

def separador():
    print(f'{cores["cz"]}~{cores["limpa"]}' * 120)

def menu_principal():
    titulo('Menu principal')
    itens_menu = [
        'Adicionar receita',
        'Adicionar despesa',
        'Listar transações',
        'Ver saldo atual',
        'Relatório por categoria',
        'Remover transação',
        'Sair'
    ]
    for item, valor in enumerate(itens_menu):
        print(f'{cores["negrito"]}[ {item + 1} ]{cores["limpa"]} {valor}')
    separador()

def menu_categorias(qtd_por_categorias = '', principal=False):
    titulo('Selecione a categoria')
    dados_categorias = qtd_por_categorias
    if principal:
        itens_menu = [
            'Alimentação',
            'Transporte',
            'Moradia',
            'Lazer',
            'Saúde',
            'Salário',
            'Outros'
        ]
    else:
        itens_menu = [
            f'Alimentação ({dados_categorias["ALIMENTAÇÃO"]})',
            f'Transporte ({dados_categorias["TRANSPORTE"]})',
            f'Moradia ({dados_categorias["MORADIA"]})',
            f'Lazer ({dados_categorias["LAZER"]})',
            f'Saúde ({dados_categorias["SAUDE"]})',
            f'Salário ({dados_categorias["SALARIO"]})',
            f'Outros ({dados_categorias["OUTROS"]})'
        ]
    categorias = [
        'ALIMENTAÇÃO',
        'TRANSPORTE',
        'MORADIA',
        'LAZER',
        'SAUDE',
        'SALARIO',
        'OUTROS'
    ]
    for item, valor in enumerate(itens_menu):
        print(f'{cores["negrito"]}[ {item + 1} ]{cores["limpa"]} {valor}')
    separador()
    while True:
        opcao = validar_numeros_inteiros('Selecione a opção > ')
        if opcao < 1 or opcao > 7:
            msg_erro('Opção inválida.')
        else:
            break
    for item, valor in enumerate(categorias):
        if opcao == item + 1:
            categoria = valor
    return categoria.upper()

def cabecalho_transacoes():
    separador()
    print(f'{cores["negrito"]}{"ID":<10}{"TIPO":<10}{"CATEGORIA":<15}{"DESCRICAO":<45}{"VALOR":<20}{"DATA":<20}{cores["limpa"]}')
    separador()

def listar_dados_transacoes(nome_arquivo):
    dados = ler_arquivo(nome_arquivo)
    for chave, valor in enumerate(dados):
        print(f'{valor["id_transacao"]:<10}',end='')
        if valor["tipo_transacao"] == "RECEITA":
            print(f'{cores["vd"]}{valor["tipo_transacao"]:<10}{cores["limpa"]}',end='')
        else:
            print(f'{cores["vm"]}{valor["tipo_transacao"]:<10}{cores["limpa"]}', end='')
        print(f'{valor["categoria_transacao"]:<15}',end='')
        print(f'{valor["descricao_transacao"]:<45}',end='')
        if valor["tipo_transacao"] == "RECEITA":
            print(f'{cores["vd"]}{formatar_para_real(valor["valor_transacao"]):<20}{cores["limpa"]}',end='')
        else:
            print(f'{cores["vm"]}{formatar_para_real(valor["valor_transacao"], despesa=True):<20}{cores["limpa"]}', end='')
        print(f'{valor["data_transacao"]:<20}')
    separador()

def listar_dados_por_categoria(nome_arquivo, categoria):
    dados = ler_arquivo(nome_arquivo)
    valor_gasto = 0
    valor_recebido = 0
    cabecalho_transacoes()
    for chave, valor in enumerate(dados):
        if categoria == valor["categoria_transacao"]:
            print(f'{valor["id_transacao"]:<10}', end='')
            if valor["tipo_transacao"] == "RECEITA":
                print(f'{cores["vd"]}{valor["tipo_transacao"]:<10}{cores["limpa"]}', end='')
            else:
                print(f'{cores["vm"]}{valor["tipo_transacao"]:<10}{cores["limpa"]}', end='')
            print(f'{valor["categoria_transacao"]:<15}', end='')
            print(f'{valor["descricao_transacao"]:<45}', end='')
            if valor["tipo_transacao"] == "RECEITA":
                print(f'{cores["vd"]}{formatar_para_real(valor["valor_transacao"]):<20}{cores["limpa"]}', end='')
                valor_recebido += valor["valor_transacao"]
            else:
                valor_gasto += valor["valor_transacao"]
                print(f'{cores["vm"]}{formatar_para_real(valor["valor_transacao"], despesa=True):<20}{cores["limpa"]}',
                      end='')
            print(f'{valor["data_transacao"]:<20}')
    separador()
    if valor_gasto == 0 and valor_recebido == 0:
        msg_alerta(f'Sem transações para exibir.')
    else:
        print(f'Valor gasto: {cores["vm"]}{formatar_para_real(valor_gasto, despesa=True)}{cores["limpa"]}')
        print(f'Valor recebido: {cores["vd"]}{formatar_para_real(valor_recebido)}{cores["limpa"]}')

def resumo_da_transação(dados, busca_id=False):
    titulo('Resumo da transação')
    cabecalho_transacoes()
    for dado in dados:
        print(f'{dado["id_transacao"]:<10}',end='')
        if dado["tipo_transacao"] == "RECEITA":
            print(f'{cores["vd"]}{dado["tipo_transacao"]:<10}{cores["limpa"]}',end='')
        else:
            print(f'{cores["vm"]}{dado["tipo_transacao"]:<10}{cores["limpa"]}', end='')
        print(f'{dado["categoria_transacao"]:<15}',end='')
        print(f'{dado["descricao_transacao"]:<45}',end='')
        if dado["tipo_transacao"] == "RECEITA":
            print(f'{cores["vd"]}{formatar_para_real(dado["valor_transacao"]):<20}{cores["limpa"]}',end='')
        else:
            print(f'{cores["vm"]}{formatar_para_real(dado["valor_transacao"], despesa=True):<20}{cores["limpa"]}', end='')
        print(f'{dado["data_transacao"]:<20}')
    if not busca_id:
        separador()
        msg_sucesso('Transação adicionada.')
