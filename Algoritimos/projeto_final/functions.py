import tabulate

chave_nome = "nome"
chave_av1 = "av1"
chave_av2 = "av2"
chave_media = "media"
chave_aprovado_por_media = "aprovado_por_media"
chave_necessario_na_final = "necessario_na_final"
chave_final = "final"
chave_media_da_final = "media_da_final"
chave_aprovado_pela_final = "aprovado_pela_final"
boletim = []
avaliacoes = [chave_av1, chave_av2, chave_final]

def save_dict_to_file():
    f = open('database.txt','w')
    f.write(str(boletim))
    f.close()

def load_dict_from_file():
    f = open('database.txt','r')
    data = f.read()
    f.close()
    global boletim
    boletim = eval(data)

def adicionarDisciplina(nomeDisciplina):
    chaves = [
        chave_av1,
        chave_av2,
        chave_media,
        chave_aprovado_por_media,
        chave_necessario_na_final,
        chave_final,
        chave_media_da_final,
        chave_aprovado_pela_final,
    ]
    disciplina = {}
    disciplina[chave_nome] = nomeDisciplina
    for chave in chaves:
        disciplina[chave] = ''
    boletim.append(disciplina)
    return boletim

def mostrarBoletim():
    header = [
        chave_nome,
        chave_av1,
        chave_av2,
        chave_media,
        chave_aprovado_por_media,
        chave_necessario_na_final,
        chave_final,
        chave_media_da_final,
        chave_aprovado_pela_final,
    ]
    rows = [x.values() for x in boletim]
    return tabulate.tabulate(rows, header, tablefmt='grid')

def mostrarDisciplinas():
    listaDisciplinas = ''
    for disciplina in boletim:
        listaDisciplinas += (str(boletim.index(disciplina)) + ' - ' + disciplina['nome'] + ':\n ')
    return listaDisciplinas

def mostrarAvaliacoes(disciplina):
    listaAvaliacoes = ''
    for avaliacao in avaliacoes:
        listaAvaliacoes += (str(avaliacoes.index(avaliacao)) + ' - ' + avaliacao + ': ' + boletim[int(disciplina)][avaliacao] + '\n ')
    return listaAvaliacoes

def colocarNota(disciplina, avaliacao, nota):
    boletim[int(disciplina)][avaliacoes[int(avaliacao)]] = nota

def calcularMedias(disciplina):
    av1 = boletim[int(disciplina)][chave_av1]
    av2 = boletim[int(disciplina)][chave_av2]
    final = boletim[int(disciplina)][chave_final]

    if (av1 != '') and (av2 != ''):
        boletim[int(disciplina)][chave_media] = (float(av1) + float(av2))/2
        if float(boletim[int(disciplina)][chave_media]) >= 7.0:
            boletim[int(disciplina)][chave_aprovado_por_media] = 'Aprovado'
        else:
            boletim[int(disciplina)][chave_aprovado_por_media] = 'Reprovado'
            boletim[int(disciplina)][chave_necessario_na_final] = 10 - boletim[int(disciplina)][chave_media]
    else:
        boletim[int(disciplina)][chave_media] = ''
        boletim[int(disciplina)][chave_aprovado_por_media] = ''
        boletim[int(disciplina)][chave_necessario_na_final] = ''
    if (final != '') and (av1 != '') and (av2 != ''):
        (boletim[int(disciplina)][chave_media_da_final]) = (float(boletim[int(disciplina)][chave_media]) + float(boletim[int(disciplina)][chave_final])) / 2
        if float(boletim[int(disciplina)][chave_media_da_final]) >= 5.0:
            boletim[int(disciplina)][chave_aprovado_pela_final] = 'Aprovado'
        else:
            boletim[int(disciplina)][chave_aprovado_pela_final] = 'Reprovado'
    else:
        boletim[int(disciplina)][chave_final] = ''
        boletim[int(disciplina)][chave_media_da_final] = ''
        boletim[int(disciplina)][chave_aprovado_pela_final] = ''

def excluirNota(disciplina, avaliacao):
    boletim[int(disciplina)][avaliacoes[int(avaliacao)]] = ''

def excluirDisciplina(disciplina):
    del(boletim[int(disciplina)])


