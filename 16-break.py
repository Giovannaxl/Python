# Ferramenta Break
# É uma ferramenta para intemrromper e encerrar um loop.
# Isso quer dizer que vamos parar o loop naquele momente e vamos sair dele.
# Execute o código abaixo e explique o que ele faz

while True:
    nome = input('Digite o seu nome ou escreva "sair": ')

    if nome == 'sair':
        break # para a execução do while, sai do loop de repetição
      
    print(f'Seu nome é {nome}')

print('acabou')

