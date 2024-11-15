from random import randint
from modules.Embarcacao import Embarcacao

def Posicionar(player, tabuleiro):
    for tipo in player.getFrota():
        for embarcacao in player.getFrota()[tipo]:
            while embarcacao.getPosicionado() == False:
                localinicial = randint(0, (len(tabuleiro) * len(tabuleiro[0]) - 1))
                tamanhoEmbarcacao = embarcacao.getTamanho()
                orientacao = randint(0, 1)
                cord_menos, cord, cord_mais, pontas = [],[],[],[]
                #posicionamento da embarcação é vertical
                if orientacao == 0:
                    if (((localinicial + ((tamanhoEmbarcacao) * 10)) > 99)):
                        cord_menos, cord, cord_mais, pontas = gerarPosicoes(tamanhoEmbarcacao,  localinicial, "baixo-cima")
                    else:
                        cord_menos, cord, cord_mais, pontas = gerarPosicoes(tamanhoEmbarcacao,  localinicial, "cima-baixo")
                    #checa se existe algum True no tabuleiro (indicando que o local para o posicionamento é inadequado)
                    checkresult = checagem(cord_menos, cord, cord_mais, pontas, tabuleiro)
                #posicionamento da embarcação é horizontal
                elif orientacao == 1:                    
                    if encontrarLimite(localinicial, tamanhoEmbarcacao):
                        cord_menos, cord, cord_mais, pontas = gerarPosicoes(tamanhoEmbarcacao, localinicial, "esquerda-direita")
                    else:
                        cord_menos, cord, cord_mais, pontas = gerarPosicoes(tamanhoEmbarcacao, localinicial, "direita-esquerda")
                    #checa se existe algum True no tabuleiro (indicando que o local para o posicionamento é inadequado)
                    checkresult = checagem(cord_menos, cord, cord_mais, pontas, tabuleiro)

                if checkresult:
                    insertMatriz(cord_menos, cord, cord_mais, pontas, tabuleiro)
                    insertGameMatriz(cord, player, embarcacao)
                    embarcacao.setPosicionado(True)

    player.setTab(tabVisivel(player, player.getTabuleiro()))


def gerarPosicoes(tamanhoEmbarcacao, localinicial, sentido):
    """ Função que retorna todas as cordenadas que podem estar em uso caso já exista uma embarcação
    a partir de uma detarminada posição, sentido e tamanho de embarcação. """

    cord_menos = []
    cord = []
    cord_mais = []
    pontas = []

    for i in range(0, tamanhoEmbarcacao):
        temp_cord_menos = []
        temp_cord = []
        temp_cord_mais = []

        if sentido == "baixo-cima":
            if ((localinicial % 10) != 0): 
                for item in list(str(localinicial + (10*(-i)) - 1)):
                    temp_cord_menos.append(int(item))

            for item in list(str(localinicial + (10*(-i)))):
                temp_cord.append(int(item))

            if list(str(localinicial))[1] != "9":
                for item in list(str(localinicial + (10*(-i)) + 1)):
                    temp_cord_mais.append(int(item))

        elif sentido == "cima-baixo":
            t = list(str(localinicial + (10*(+i)) - 1))
            if len(t) == 1:
                t.insert(0, 0)
            if localinicial != 0 and ((localinicial % 10) != 0):
                for item in t:
                    temp_cord_menos.append(int(item))
            
            t = list(str(localinicial + (10*(+i))))
            if len(t) == 1:
                t.insert(0, 0)
            for item in t:
                temp_cord.append(int(item))

            t = list(str(localinicial + (10*(+i)) + 1))
            if len(t) == 1:
                t.insert(0, 0)
                if localinicial != 9:
                    for item in t:
                        temp_cord_mais.append(int(item))
            elif len(t) > 1 and temp_cord[1] != 9:
                for item in t:
                    temp_cord_mais.append(int(item))
        
        elif sentido == "esquerda-direita":
            if localinicial < 10:
                temp_cord.append(0)
            if localinicial >= 10 and localinicial <= 19:
                temp_cord_menos.append(0)
            for item in list(str(localinicial + i)):
                temp_cord.append(int(item))
            if localinicial >= 10:
                for item in list(str((localinicial - 10) + i)):
                    temp_cord_menos.append(int(item))
            if localinicial < 90:
                for item in list(str((localinicial + 10) + i)):
                    temp_cord_mais.append(int(item))

        elif sentido == "direita-esquerda":
            if localinicial < 10:
                temp_cord.append(0)
            if localinicial >= 10 and localinicial <= 19:
                temp_cord_menos.append(0)
            for item in list(str(localinicial - i)):
                temp_cord.append(int(item))
            if localinicial >= 10:
                for item in list(str((localinicial - 10) - i)):
                    temp_cord_menos.append(int(item))
            if localinicial < 90:
                for item in list(str((localinicial + 10) - i)):
                    temp_cord_mais.append(int(item))
        
        if temp_cord_menos != []:
            cord_menos.append(temp_cord_menos)
        if temp_cord != []:
            cord.append(temp_cord)
        if temp_cord_mais != []:
            cord_mais.append(temp_cord_mais)


    if sentido == "cima-baixo":
        if cord[0][0] != 0 :
            pontas.append([cord[0][0] - 1, cord[0][1]])
        pontas.append([tamanhoEmbarcacao + cord[0][0], cord[0][1]])
    if sentido == "baixo-cima":
        if cord[0][0] != 9:
            pontas.append([cord[0][0] + 1, cord[0][1]])
        pontas.append([cord[0][0] - tamanhoEmbarcacao, cord[0][1]])
    if sentido == "esquerda-direita":
        if cord[0][1] != 0:
            pontas.append([cord[0][0], cord[0][1] -1])
        pontas.append([cord[0][0], cord[0][1] + tamanhoEmbarcacao])
    elif sentido == "direita-esquerda":
        if cord[0][1] != 9:
            pontas.append([cord[0][0], cord[0][1] +1])
        pontas.append([cord[0][0], cord[0][1] - tamanhoEmbarcacao])

    return cord_menos, cord, cord_mais, pontas


def checagem(cord_menos, cord, cord_mais, pontas, tabuleiro):
    """ Recebe um grupo de coordenadas e um tabuleiro, transfere todos os dados do tabuleiro 
    referente as coordenadas para um vetor, todas as posições vazias devem ter False, caso
    não encontre algum item no vetor igual a True retorna False indicando que todas as pos """

    truecheck = []
    for item in cord_menos:
        truecheck.append(tabuleiro[item[0]][item[1]])
    for item in cord:
        truecheck.append(tabuleiro[item[0]][item[1]])
    for item in cord_mais:
        truecheck.append(tabuleiro[item[0]][item[1]])
    for item in pontas:
        truecheck.append(tabuleiro[item[0]][item[1]])
    if not(True in truecheck):
        return True
    return False


def insertMatriz(cord_menos, cord, cord_mais, pontas, tabuleiro):
    """ Recebe um tabuleiro e um grupo de coordenadas existentes nesse tabuleiro, nas posições
    das coordenadas marca como True informando que ali há é espaço ocupado por uma embarcação.  """

    for item in cord_menos:
        tabuleiro[item[0]][item[1]] = True
    for item in cord:
        tabuleiro[item[0]][item[1]] = True
    for item in cord_mais:
        tabuleiro[item[0]][item[1]] = True
    for item in pontas:
        tabuleiro[item[0]][item[1]] = True


def insertGameMatriz(cord, player, embarcacao):
    """ Insere uma embarcação no tabuleiro visível ao jogador, fazendo com que os locais onde está a embarcação
    referenciem a mesma."""
    try:
        assert embarcacao.getPosicionado() == False
        for item in cord:            
            embarcacao.setPosicao([item[0], item[1]])
            player.updateTabuleiro(item[0], item[1], embarcacao)
    except AssertionError:
        print("Aviso: Erro ao posicionar a embarvação")


def encontrarLimite(localinicial, tamanho):
    """ Retorna false caso o local inicial somado ao tamanho resulte em um número pertinente a uma dezena que
    diferente do local inicial ex: local inicial = 43 (dezena 40)."""
    #padrao esquerda - > direita
    #retorna false caso ultrapasse
    if localinicial < 10:
        limite_maior = 10
        limite_menor = 0
    else:
        limite_menor = 10 * int(list(str(localinicial))[0])
        limite_maior = limite_menor + 9

    if (localinicial + tamanho + 1) > limite_maior:
        return False
    return True

def tabVisivel(player, tabuleiro):
    """ Cria e retorna uma string contendo dados do tabuleiro do jogador. """

    tabStr =("\n _________________________________________________________________\n"
            "|     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |\n"
            "|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|")

    for i in range(len(tabuleiro)):
        tabStr += "\n|  "+str(i)+"  |"
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] in ["     ", "  X  ", ".\\w/."]:
                tabStr += ""+str(tabuleiro[i][j])+"|"
            elif type(tabuleiro[i][j]) == Embarcacao:
                tabStr += "     |"
        if i != 9:
            tabStr += "\n|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|"
    tabStr += "\n|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|\n"

    return tabStr
