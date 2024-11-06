
numero = int(input("Digite um número para a verificação:"))
#Inicia a variável para verificar se o número é primo
e_primo = True

#Verifica se o número é maior ou menor que 2
if numero < 2:
    e_primo = False
else:
    #Verifica a divisibilidade do número a partir de 2 até a raiz quadrade no número
    for i in range(2,int(numero**0.5) + 1):
        if numero % i == 0:
            e_primo = False
            break # Se o número for divisivel por algum "i" quebra o loop

if e_primo:
    print(f"{numero} É um número primo.")
else:
    print(f"{numero} Não é um número primo.")

    