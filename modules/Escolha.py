from modules.Embarcacao import Embarcacao

def Escolha(bot = False):
    """ Função que permite ao usuário escolher a frota de embarcaçoes, retorna um dicionário tendo o nome das
    embarcações como chave e o número de embarcações selecionadas, caso o Player seja um bot as embarcações são
    escolhidas automaticamente."""

    embarcacoesUsadas = {"porta_aviao": 0, "cruzador": 0, "submarino": 0}
    embarcacoesDispo = {"porta_aviao": 1, "cruzador": 2, "submarino": 3}
    embarcacoesEscolhidas = {"porta_aviao": [], "cruzador": [], "submarino": []}

    if bot == False:
        def exibirOpcoes(embarcacoesdispo):
            """ Exibe na tela do jogador as embarcações disponívels para escolha de frota, o jogado pode no mínimo
            escolher uma embarcação de qualquer tipo """

            if embarcacoesdispo["porta_aviao"] > 0:
                print('\n[1] Porta-avião\n * Ocupa 4 células\n * Resiste a 3 ataques')
            if embarcacoesdispo["cruzador"] > 0:
                print('\n[2] Cruzador\n * Ocupa 3 células\n * Resiste a 2 ataques')
            if embarcacoesdispo["submarino"] > 0:
                print('\n[3] Submarino\n * Ocupa 2 células\n * Resiste a 1 ataque')
            if (embarcacoesUsadas["porta_aviao"] + embarcacoesUsadas["cruzador"] + embarcacoesUsadas["submarino"]) > 0:
                print("\n[4] Finalizar Seleção\n * Usa como frota as embarcações já selecionadas")

        def escolherEmbarcacao(embarcacoesusadas, embarcacoesdispo):
            """ Recebe um dicionário de dados com as embarcações já usadas, outro com as embarcações disponíveis para
            escolha e permite que o jogador escolha uma embarcação por fim após escolha retorna os dois dicionários
            com as embarcações usadas e disponíveis atualizados """

            try:
                assert (embarcacoesdispo["porta_aviao"] + embarcacoesdispo["cruzador"] + embarcacoesdispo["submarino"]) > 0
                exibirOpcoes(embarcacoesdispo)
                embarcacaoEscolhida = input("\n>> ")
                embarcacaoEscolhida = int(embarcacaoEscolhida)

                if (embarcacaoEscolhida == 1) and (embarcacoesdispo["porta_aviao"] > 0):
                    embarcacoesEscolhidas["porta_aviao"].append(Embarcacao("porta_aviao"))
                    embarcacoesusadas["porta_aviao"] += 1
                    embarcacoesdispo["porta_aviao"] -= 1

                elif (embarcacaoEscolhida == 2) and (embarcacoesdispo["cruzador"] > 0):
                    embarcacoesEscolhidas["cruzador"].append(Embarcacao("cruzador"))
                    embarcacoesusadas["cruzador"] += 1
                    embarcacoesdispo["cruzador"] -= 1

                elif (embarcacaoEscolhida == 3) and (embarcacoesdispo["submarino"] > 0):
                    embarcacoesEscolhidas["submarino"].append(Embarcacao("submarino"))
                    embarcacoesusadas["submarino"] += 1
                    embarcacoesdispo["submarino"] -= 1

                elif (embarcacaoEscolhida == 4) and ((embarcacoesusadas["porta_aviao"] + embarcacoesusadas["cruzador"] + embarcacoesusadas["submarino"]) > 0):
                    for embarcacao in embarcacoesdispo:
                        embarcacoesdispo[embarcacao] = 0

                else:
                    print("\nA embarcação escolhida não está disponível.\n")

                return embarcacoesusadas, embarcacoesdispo

            except AssertionError:
                raise Exception("Nenhuma embarcação disponível")
            except ValueError:
                print("\nA opção escolhida deve ser um número inteiro, \nTente novamente.\n\n")

        while (embarcacoesDispo["porta_aviao"] + embarcacoesDispo["cruzador"] + embarcacoesDispo["submarino"]) > 0:
            embarcacoesUsadas, embarcacoesDispo = escolherEmbarcacao(embarcacoesUsadas, embarcacoesDispo)
    else:
        # Caso o Player seja um bot as embarcações são escolhidas automaticamente
        embarcacoesEscolhidas = {"porta_aviao": [], "cruzador": [], "submarino": []}
        embarcacoesEscolhidas["porta_aviao"].append(Embarcacao("porta_aviao"))
        embarcacoesEscolhidas["cruzador"].append(Embarcacao("cruzador"))
        embarcacoesEscolhidas["cruzador"].append(Embarcacao("cruzador"))
        embarcacoesEscolhidas["submarino"].append(Embarcacao("submarino"))
        embarcacoesEscolhidas["submarino"].append(Embarcacao("submarino"))
        embarcacoesEscolhidas["submarino"].append(Embarcacao("submarino"))

    return embarcacoesEscolhidas

