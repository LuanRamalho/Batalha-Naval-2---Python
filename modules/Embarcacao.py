class Embarcacao:
    def __init__(self, tipo):
        self.__atkRecebidos = 0
        self.__maxDanos = getMaxDanos(tipo)
        self.__tamanho = self.__maxDanos
        self.__tipo = tipo
        self.__posicionado = False
        self.__posicoes = []

    def setPosicao(self, posi):
        self.__posicoes.append(posi)

    def removePosicao(self, posi):
        self.__posicoes.remove(posi)

    def setPosicionado(self, posi):
        """ Define a embarcação como posicionada """
        self.__posicionado = posi

    def getPosicoes(self) :
        return self.__posicoes

    def getPosicionado(self):
        """ Retorna se a embarcação está posicionada """
        return self.__posicionado

    def getEstado(self):
        """" Retorna true caso a embarcação não tenha recebido o número máxomo de ataques que podem ser recebidos pela
        mesma e false caso já tenha recebido esse número máximo de ataques. """
        return self.__atkRecebidos >= self.__maxDanos

    def getTamanho(self):
        """ Retorna o tamanho da embarcação """
        return self.__tamanho

    def setAtkRecebido(self):
        """" Incrementa em um o número de ataques recebidos por uma embarcação e retorna true, caso a embarcaação já
        tenha recebido o número máximo de ataques retorna false """
        self.__atkRecebidos += 1
        self.updateStatus()
            
    def updateStatus(self):
        if self.__atkRecebidos == self.__maxDanos:
            self.__posicionado = False

def getMaxDanos(tipo):
    """ Retorna o número máximo de ataques que podem ser recebidos por uma embarcação. """
    NavioAtaques = {"porta_aviao": 4, "cruzador": 3, "submarino": 2}
    return NavioAtaques[tipo]