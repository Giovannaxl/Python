# Ferramenta Continue
# A ferramenta continue no python vai interromper o lopp,
# mas vai dar continuedade a ele.

contador = 0

while contador <= 40:
    contador +=1

    # Verifica se o valor de 'contador' é multiplo de 4
    if(contador % 4 == 0):
        print("pim") # Se for multiplo de4,impreme "pim"
        continue #interrompe a interação atual e volta para o inicio do lopp
   
   # Se o número não for multiplo de 4,imprime o valor do contador
    print(contador)
# Após o término do loop, impreme a mensagem de finalização
print("Fim do programa!")
