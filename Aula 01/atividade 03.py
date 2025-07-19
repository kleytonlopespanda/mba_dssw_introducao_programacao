valor_produto = float(input('valor do produto: '))
desconto = float(input('desconto: '))

valor_desconto = (valor_produto + desconto) / 100
valor_final = valor_produto - valor_desconto

print(f'0 valor final é {valor_final:.2f}')