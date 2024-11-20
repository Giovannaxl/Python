def exibirMensagem (nome, idade, filme, total_pagantes):
    print(f"Olá {nome}, se divirta assistindo {filme}. Alem disso, será/serão {total_pagantes} pessoa(s) que irá/irão pagar o ingresso.")

nome = input("Qual seu nome: \n\n")
idade = input("\nQual a sua idade: \n\n")
filme = input("\nQual filme que você deseja assistir: \n\n")
total_pagantes = int(input("\nDigite a quantidade total de ingressos: \n\n"))
valor_total = float(input("\nQual o valor total que você pagou? \n\n"))
valor_inteira = float(input("\nDigite o valor da inteira: \n\n"))
valor_meia = float(input("\n Digite o valor da meia: \n\n"))

x = (valor_total - valor_meia * total_pagantes) / (valor_inteira - valor_meia)
y = total_pagantes - x

exibirMensagem(nome, idade, filme, total_pagantes)
print(f"Pagantes Inteira: {x}")
print(f"Pagantes meia: {y}")