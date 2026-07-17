from lib.msgs import msg_erro


def validar_numeros_inteiros(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            msg_erro('Digite um número inteiro válido (apenas números).')

def validar_descricao(msg):
    while True:
        descricao = input(msg).strip()
        if descricao == '':
            msg_erro('Descrição inválida.')
        elif len(descricao) > 40:
            msg_erro('A descrição deve conter no máximo 40 caracteres.')
        elif descricao.isnumeric():
            msg_erro('A descrição não deve conter apenas números.')
        else:
            return descricao

def validar_valor(msg):
    while True:
        entrada_valor = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada_valor)
            if valor <= 0:
                msg_erro('O valor da transação deve ser maior que zero.')
            else:
                return valor
        except ValueError:
            msg_erro('Digite um valor numérico válido.')

def validar_id(msg):
    while True:
        entrada_id = input(msg).strip().upper()
        if entrada_id == '':
            msg_erro('ID inválido.')
        elif len(entrada_id) > 8 or len(entrada_id) < 8:
            msg_erro('IDs tem 8 caracteres apenas.')
        elif len(entrada_id) == 8:
            return entrada_id

def formatar_para_real(valor, despesa = False):
    if despesa:
        valor_formatado = f"R$ -{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    else:
        valor_formatado = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado
