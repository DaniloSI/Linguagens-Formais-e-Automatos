
class Gramatica:

    def __init__(self):
        self.producoes = dict()
        self.terminais = set()
        self.variaveis = set()
        self.variavel_partida = str()


    def set_producao(self, str_producao):

        str_producao = str_producao.replace(" ", "").replace("\n", "")

        # Define a primeira variavel das producoes como variavel de partida.
        if len(self.producoes) == 0:
            self.variavel_partida = str_producao[0]

        variavel = str_producao.split("->")[0]
        producao = str_producao.split("->")[1]

        if not(self.producoes.__contains__(variavel)):
            self.producoes[variavel] = set()

        self.producoes[variavel].add(producao)
        self.variaveis.add( variavel )

        if len(producao) == 1:
            self.terminais.add( producao )


    # Retorna o lado esquerdo da producao a partir uma das producoes do lado direito
    def get_left_side_production(self, str_right_side_production):
        set_left_side_production = set()

        for variavel in self.variaveis:
            if str_right_side_production in self.producoes[ variavel]:
                set_left_side_production.add( variavel )

        return set_left_side_production

    # Retorna a variavel de partida
    def get_variavel_partida(self):
        return self.variavel_partida
		

    def __str__(self):
        return ( "Variaveis: " + str(self.variaveis) +
                 "\nTerminais: " + str(self.terminais) +
                 "\nVariavel de partida: " + self.variavel_partida +
                 "\nProducoes: " + str(self.producoes) )

