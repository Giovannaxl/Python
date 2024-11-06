alunos = []

for i in range(5):
    nome= input(f"Digite o nome do {i+1} aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome,nota))

print("\n Lista de alunos e suas notas: ")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, Nota: {aluno[1]}")

   