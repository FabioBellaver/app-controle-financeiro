from lib.arquivos import ler_arquivo, criar_arquivo
from lib.interface import menu_principal, menu_categorias, cabecalho_transacoes, listar_dados_transacoes, \
    listar_dados_por_categoria, titulo, titulo_app, separador
from lib.dados import adicionar_receita, adicionar_despesa, ver_saldo, remover_transacao, quantidade_por_categoria
from lib.msgs import msg_erro, msg_alerta, msg_sucesso
from lib.util import validar_numeros_inteiros, validar_descricao, validar_valor, validar_id, formatar_para_real
from lib.cores import cores

titulo_app('App controle financeiro')

nome_arquivo = 'dados/transacoes.json'
criar_arquivo(nome_arquivo)

while True:
    dados = ler_arquivo(nome_arquivo)
    menu_principal()
    opcao = validar_numeros_inteiros('Escolha a opção > ')
    if opcao < 1 or opcao > 7:
        msg_erro('Opção inválida.')
    if opcao == 1:
        titulo('Adicionar receita')
        tipo = "Receita"
        categoria = menu_categorias(principal=True)
        descricao = validar_descricao('Adicionar descrição: ')
        valor = validar_valor('Digite o valor: ')
        adicionar_receita(nome_arquivo, tipo, categoria, descricao, valor)
    elif opcao == 2:
        titulo('Adicionar despesa')
        tipo = "Despesa"
        categoria = menu_categorias(principal=True)
        descricao = validar_descricao('Adicionar descrição: ')
        valor = validar_valor('Digite o valor: ')
        adicionar_despesa(nome_arquivo, tipo, categoria, descricao, valor)
    elif opcao == 3:
        if dados:
            titulo('Lista de transações')
            cabecalho_transacoes()
            listar_dados_transacoes(nome_arquivo)
        else:
            msg_alerta('Não existem transações cadastradas.')
    elif opcao == 4:
        titulo('Saldo atual')
        saldo = ver_saldo(nome_arquivo)
        saldo_receitas = formatar_para_real(saldo[0])
        saldo_despesas = formatar_para_real(saldo[1], despesa=True)
        saldo_formatado = formatar_para_real(saldo[2])
        separador()
        print(f'Saldo de receita: {cores["vd"]}{saldo_receitas}{cores["limpa"]}')
        print(f'Saldo de despesa: {cores["vm"]}{saldo_despesas}{cores["limpa"]}')
        if saldo[2] > 0:
            print(f'Saldo atual: {cores["vd"]}{saldo_formatado}{cores["limpa"]}')
        else:
            print(f'Saldo atual: {cores["vm"]}{saldo_formatado}{cores["limpa"]}')
        separador()
    elif opcao == 5:
        if dados:
            titulo('Relatório por categoria')
            qtd_por_categoria = quantidade_por_categoria(nome_arquivo)
            categoria = menu_categorias(qtd_por_categoria)
            listar_dados_por_categoria(nome_arquivo, categoria)
        else:
            msg_alerta('Não existem transações cadastradas.')
    elif opcao == 6:
        if dados:
            titulo('Remover transação')
            id_transacao = validar_id('Qual o ID da transação para apagar? ')
            id_encontrado = remover_transacao(nome_arquivo, id_transacao)
            if id_encontrado:
                separador()
                msg_sucesso('Transação removida.')
            else:
                separador()
                msg_erro('Transação não encontrada ou ID inválido.')
        else:
            msg_alerta('Não existem transações cadastradas.')
    elif opcao == 7:
        titulo_app('Sistema encerrado.')
        break
