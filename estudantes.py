estudantes = {
    1: { 'nome': 'Joana', 'idade': 45, 'curso': 'Programação' },
    2: { 'nome': 'Ivan', 'idade': 60, 'curso': 'Matemática' },
    3: { 'nome': 'Maria', 'idade': 22, 'curso': 'Programação' }
}

cursos = { 'Programação', 'Matemática', 'Fisíca' }

estudantes_cursos = {
    'Programação': { 1, 3},
    'Matemática': { 2 }
}

def adiconarEstudante(matricula, nome, idade, curso):
    pessoa = { 'nome': nome, 'idade': idade, 'curso': curso }
    estudantes[matricula] = pessoa
    if curso not in estudantes_cursos:
        estudantes_cursos[curso] = set()
    estudantes_cursos[curso].add(matricula)

print(estudantes_cursos)
adiconarEstudante(4, 'Pedro', 28, 'Engenheiro de Software')
print(estudantes_cursos)
adiconarEstudante(5, 'Nathalia', 24, 'Programação')
print(estudantes_cursos)        