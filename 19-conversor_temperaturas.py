#Menu de Conversão de Temperaturas

def menu():
    print("CONVERSÃO DE TEMPERATURAS:\n")
    print("Menu de escolha:\n")
    print("1. Converta Fahrenheit para Kelvin")
    print("2. Converta Farenheit para Celsius")
    print("3. Converta Kelvin para Farenheit")
    print("4. Converta Kelvin pra Celsius")
    print("5. Converta Celsius para Fahrenheit")
    print("6. Converta Celsius para Kelvin")
    print("7. Saindo do programa\n")
   


def converter_fahrenheit_kelvin(f):
    return (f-32) * 5/9 + 273


def converter_Fahrenheit_celsius(f):
    return (f - 32) * 5/9

def converter_Kelvin_Fahrenheit(k):
    return (k-273) * 9/5 + 32

def converter_Kelvin_Celcius(k):
    return k-273

def converter_Celcius_Fahrenheit(c):
    return c* 9/5 + 32

def converter_Celcius_Kelvin(c):
    return c + 273


#Declaração de variáveis 
opcao = 0
conversao = 0

 
   

#Início do código 
while (opcao != 7):
    menu() 
    opcao = int(input("Digite a sua opção: ")) 
   
    

    if (opcao == 1):
        f = float(input("Digite a temperatura em Fahrenheit: "))
        conversao = converter_fahrenheit_kelvin(f)
        print(f" A temperatura em Kelvin é = {conversao:.3f}")

    elif  (opcao == 2):
        f = float(input("Digite a temperatura em Fahrenheit: "))
        conversao = converter_Fahrenheit_celsius(f)
        print(f" A temperatura em Celcius é = {conversao:.3f}")

    elif (opcao == 3):
        k = float(input("Digite a temperatura em Kelvin: "))
        conversao =  converter_Kelvin_Fahrenheit(k)
        print(f" A temperatu em Fahrenheit é = {conversao:.3f}")
    
    elif (opcao == 4):
        k = float(input("Digite a temperatura em Kelvin: "))
        conversao = converter_Kelvin_Celcius(k)
        print(f"A temperatura em Celsius é = {conversao:.3f}")

    elif (opcao == 5):
        c = float(input("Digite a temperatura em Celcius: "))
        conversao =  converter_Celcius_Fahrenheit(c)
        print(f" A temperatura em fahrenheit é = {conversao:.3f}")

        
    elif (opcao == 6):
        c = float(input("Digite a temperatura em Celsius: "))
        conversao = converter_Celcius_Kelvin(c)
        print(f" A temperatura em Kelvin é = {conversao:.3f}")

    elif (opcao == 7): 
        print("Saindo do programa\n")
    
    else:
        print("Opção inválida\n")
