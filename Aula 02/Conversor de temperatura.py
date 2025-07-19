temperatura = float(input("Digite a temperatura: "))
escala = input("Informe a escala de origem (C/F): ").upper()
if escala == 'C':

    convertida = (temperatura * 9/5) + 32
    print(f"{temperatura}°C equivalem a {convertida:.1f}°F")
if escala == 'F':

    convertida = (temperatura - 32) * 5/9
    print(f"{temperatura}°F equivalem a {convertida:.1f}°C")
else:
    print("Escala inválida. Por favor, use 'C' para Celsius ou 'F' para Fahrenheit.")