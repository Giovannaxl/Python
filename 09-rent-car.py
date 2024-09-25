#09-rent-car.py = Escreva um programa que pergunte a quantidade de km
#percorrido por um carro alugado pelo usuário
#assim como a quantidade de dias pelos quais o carro foi alugado
#caucule o preço a pagar, sabendo que o
#carro custa R$ 60 por dia e R$ 0,15 por Km rodado


#Variáveis
quilometros = float(input("Digite a quantidade de quilometros rodados: "))
dias = int(input("Digite a quantidade de dias alugados: "))

total =  (quilometros*60)+(dias*0.15)
print(f"O valor total a pagar é R${total:.2f}")