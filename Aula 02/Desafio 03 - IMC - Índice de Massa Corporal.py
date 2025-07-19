print("Calculadora de IMC (Índice de Massa Corporal)")

# Entrada de dados
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
if 18.5 <= imc < 25:
    classificacao = "Peso normal"
if 25 <= imc < 30:
    classificacao = "Sobrepeso"
if 30 <= imc < 35:
    classificacao = "Obesidade Grau I"
if 35 <= imc < 40:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

# Resultado
print(f" Seu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")