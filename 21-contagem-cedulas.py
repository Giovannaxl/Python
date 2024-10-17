# cédulas disponíveis
cedulas = [50, 20, 10, 5, 1]

valor = int(input("digite o valor total a ser pago (ou 0 para sair): "))

ingresso = valor
print(f"\npara pagar o valor de R$ {ingresso}, serão necessárias:")

for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            print(f"R$ {cedula}: {quantidade} cédula(s)")
            valor %= cedula
        else:
            print(f"R$ {cedula}: 0 cédula(s)")

print("\npagamento concluído.\n")
