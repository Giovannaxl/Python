# Declaração da função exibirMensagem(nome, idade)
def exibirMensagem(nome, idade):
    print(f"Olá,{nome} com {idade} anos!")


def somar(a,b):
    return a + b


def calculadoraAresCirculo(raio):
    area = 3.1415 * raio**2
    return area



#Início do algoritimo
nome = input("Digite o seu nome!: ")
idade = input("Digite a sua idade!: ")
exibirMensagem(nome, idade)  # Exibe a mensagem com o nome e idade do usuário

# Chamando Função com retorno
valorA = int(input("Digite o primeiro número: "))
valorB = int(input("Digite o segundo número: "))
resultado = somar(valorA, valorB)
print(f"O resultado da soma = {resultado}")

# Calcular a área do círculo
print("Área do círculo!!")
raio = float(input("Digite o valor do raio:"))
area = calculadoraAresCirculo(raio)
print(f"A área do círculo : {area:.2f}")  
