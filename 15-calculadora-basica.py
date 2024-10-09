#Declaração de variáveis 
opcao = 0
resultado = 0

#Início do código 
while (opcao != 6):
    print("CALCULADORA DAS OPERAÇÕES BÁSICAS:\n")
    print("Menu de escolha:\n")
    print("1. Soma\n")
    print("2. Subtração\n")
    print("3. Multiplicação\n")
    print("4. Divisão\n")
    print("5. Resto da Divisão\n")
    print("6. Sair\n")
    opcao = int(input("Digite a sua opção: ")) 
    
    if (opcao == 1):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 + n2
        print(f"A soma é = {resultado}")



    elif  (opcao == 2):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 - n2
        print(f"A subtração = {resultado}")

    elif (opcao == 3):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 * n2
        print(f"A multiplicação é = {resultado}")
    
    elif (opcao == 4):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 / n2
        print(f"A divisão é = {resultado}")

    elif (opcao == 5):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 // n2
        print(f" A divisão inteira é = {resultado}")
        
    elif (opcao == 6):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 % n2
        print(f" O resto da divisão é = {resultado}")

    elif (opcao == 7):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 ** n2
        print(f" A exponenciação é = {resultado}")



    elif (opcao == 8): 
        print("Finalizando o código!\n")

   