
class Gramatica:

    def __init__(self):
        self.dicionario_producoes = dict()
        self.terminais = set()
        self.variaveis = set()
        self.variavel_partida = str()


    def set_producao(self, str_producao):

        str_producao = str_producao.replace(" ", "").replace("\n", "")

        # Define a primeira variavel das producoes como variavel de partida.
        if len(self.dicionario_producoes) == 0:
            self.variavel_partida = str_producao[0]

        variavel = str_producao.split("->")[0]
        producao = str_producao.split("->")[1]

        if not( self.dicionario_producoes.__contains__(variavel) ):
            self.dicionario_producoes[variavel] = set()

        self.dicionario_producoes[variavel].add(producao)
        self.variaveis.add( variavel )

        if len(producao) == 1:
            self.terminais.add( producao )


    def print_gramatica(self):
        print( "Variaveis: " + str(self.variaveis) )
        print( "Terminais: " + str(self.terminais) )
        print( "Variavel de partida: " + self.variavel_partida )
        print( "Producoes: " + str(self.dicionario_producoes) )

    # Retorna o lado esquerdo da producao a partir uma das producoes do lado direito
    def get_left_side_production(self, str_right_side_production):
        set_left_side_production = set()

        for variavel in self.variaveis:
            if str_right_side_production in self.dicionario_producoes[ variavel ]:
                set_left_side_production.add( variavel )

        return set_left_side_production

    # Retorna a variavel de partida
    def get_variavel_partida(self):
        return self.variavel_partida

