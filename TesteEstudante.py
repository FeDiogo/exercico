if __name__ == "__main__":
    nome = input("Digite o nome do estudante: ")

    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota do {i+1}º bimestre: "))
        notas.append(nota)

    aluno = Estudante(nome, notas)
    media = aluno.calcularMedia()

    print(f"\nA média de {aluno.nome} é {media:.2f}")