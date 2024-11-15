from modules.Escolha import Escolha
from modules.Jogador import Jogador
from modules.Partida import partida

def MenuPrincipal():
    """ Menu principal do jogo, a partir dele é possível carregar um jogo salvo ou iniciar um novo jogo. """

    #------------------------------------------------ Funçoes do Menu -------------------------------------------------#

    def gamemodeSelect():
        """ Permite ao jogador escolher, o modo de jogo retorna true para player vs player e false player vs bot """

        print("\nEscolha o modo de jogo.\n\n"
              "[1] - Player vs Player\n"
              "[2] - Player vs Bot\n")

        gamemode = input(">> ")
        try:
            gamemode = int(gamemode)
            assert gamemode in [1, 2]
            if gamemode == 1:
                return True
            return False

        except ValueError:
            print("\nInforme um número inteiro !\n")
        except AssertionError:
            print("\nOpção indisponível !\nTente novamente.")
        except Exception:
            raise Exception

    def NovoJogo(modo):
        """ A função novo jogo é responsável por iniciar uma nova partida, se houverem arquivos de jogos salvos
         eles são substituidos por novos arquivos gerados pelo jogo """

        n1 = input("\nInforme o nome do Player 1: ")
        
        print("\nEscolha de frota ["+str(n1)+"]" )
        player1 = Jogador(Escolha(), n1)
        player2 = None

        if modo == False:
            player2 = Jogador(Escolha(True), "Bot", "bot")
        else:
            n2 = input("\nInforme o nome do Player 2: ")
            print("\nEscolha de frota ["+str(n2)+"]")
            player2 = Jogador(Escolha(), n2)

        #após a escolha das frotas é possível escolher
        partida(player1, player2)

    #------------------------------------------------ Menu Principal -------------------------------------------------#

    print("\n                                              \n"
        "          ____| |_____| |___,                     \n"
        "    _____/__________________ \\_________.-/       \n"
        "    \\         NAVAL BATTLE              /        \n"
        "~~~~~\\_________________________________/~~~~~/\\~\n"
        "~~/\\ ~~~~~~~~~~~~~~~~/\\ ~~~~~~~~~~~/\\~~~~~~~~~~\n"
        "~~~~~~~~~~~~~~~/\\~~~~~~~~~~~~~~~~~~~~~~/\\~~~~~~~\n")

    continuar = True
    while continuar:
        print("\nBem-vindo ao jogo de batalha naval.\n\n"
                "[1] - Iniciar uma nova partida\n"
                "[2] - Finalizar o jogo\n")
        option = input(">> ")
        try:
            option = int(option)
            assert option in [1, 2, 3]

            if option == 1:
                pvp = gamemodeSelect()
                if pvp:
                    NovoJogo(pvp)           #se emviar true os dois jogadores são pessoas
                elif pvp == False:
                    NovoJogo(False)         #se enviar false apenas o player1 é uma pessoa
            if option == 2:
                continuar = False
                
        except ValueError:
            print("\nInforme um número inteiro !\n")
        except AssertionError:
            print("\nOpção indisponível !\nTente novamente.")
MenuPrincipal()