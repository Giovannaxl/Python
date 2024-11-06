print("Lista numérica\n")

minha_lista = []

for valor in range(5):
    lista= int(input(f"Digite o {valor+1} número inteiro: "))
    minha_lista.append(lista)
print("O maior valor é:",max(minha_lista))
print("O menor valor é:",min(minha_lista))
print("A soma dos elementos é:",sum(minha_lista))
    
   





