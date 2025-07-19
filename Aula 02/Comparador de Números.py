numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Comparação
if numero1 > numero2:
    print(f"O primeiro número ({numero1}) é maior que o segundo número ({numero2}).")
if numero2 > numero1:
    print(f"O segundo número ({numero2}) é maior que o primeiro número ({numero1}).")
else:
    print(f"Os números são iguais ({numero1}).")