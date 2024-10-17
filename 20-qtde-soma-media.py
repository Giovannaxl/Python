#Declaração das variáveis
soma = 0
quantidade = 0
while True:# lopp infinito
    num = int(input("Digite um número(0 para sair): "))
    if num == 0:
     break
    soma += num
    quantidade +=1

if quantidade > 0 : #If fora do while
    media = soma / quantidade
    print(f'Quantidade de números digitados: {quantidade}')
    print(f"Soma do números digitados: {soma}")
    print(f"A media é: {media:.2f}")
else:
   print("Nenhum número foi digitado:")
   
        



