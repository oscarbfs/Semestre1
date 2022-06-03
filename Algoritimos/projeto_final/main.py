import functions
continuar_rodando = True
functions.load_dict_from_file()

while continuar_rodando:
    comando = int(input('\nOlá! O que deseja fazer? (1, 2 ou 3)\n 1 - Adicionar uma disciplina\n 2 - Adicionar/editar uma nota\n 3 - Mostrar Boletim\n 4 - Excluir nota ou disciplina\n 5 - Sair\n '))

    # 1
    if comando == 1:
        nomeDisciplina = input('Qual é o nome da disciplina?\n ')
        print(functions.adicionarDisciplina(nomeDisciplina))
        print('Disciplina ' + nomeDisciplina + ' adicionada com sucesso!\n ')
    # 2
    elif comando == 2:
        disciplina = input('Qual é a disciplina que quer adicionar/editar nota?\n ' + functions.mostrarDisciplinas())
        avaliacao = input('Qual é avaliacao que você deseja adicionar/editar?\n ' + functions.mostrarAvaliacoes(disciplina))
        nota = input('Qual é a nota?\n ')
        functions.colocarNota(disciplina, avaliacao, nota)
        functions.calcularMedias(disciplina)
    # 3
    elif comando == 3:
        print('mostrar boletim')
        print(functions.mostrarBoletim())
    # 4
    elif comando == 4:
        ordem = int(input('O que deseja fazer?\n 1 - Excluir disciplina\n 2 - Excluir nota\n'))
        if ordem == 1:
            disciplinaExcluir = input('Qual é a avaliação que deseja excluir?\n ' + functions.mostrarDisciplinas())
            functions.excluirDisciplina(disciplinaExcluir)
        elif ordem == 2:
            notaDisciplinaExcluir = input('Qual é a avaliação que deseja excluir uma nota?\n ' + functions.mostrarDisciplinas())
            notaExcluir = input('Qual é a avaliação que deseja excluir?\n ' + functions.mostrarAvaliacoes(notaDisciplinaExcluir))
            functions.excluirNota(notaDisciplinaExcluir, notaExcluir)
            functions.calcularMedias(notaDisciplinaExcluir)
    # 5
    elif comando == 5:
        functions.save_dict_to_file()
        continuar_rodando = False