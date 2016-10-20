
class Gramatica:

    def __init__(self, str_producoes):
        self.dicionario_producoes = {}
        self.terminais = set()
        self.variaveis = set()
        self.variavel_partida = ""
        self.str_producoes = ""

        # Retira o {} da string recebida e retira espaços em branco ou \n, caso tenha.
        str_producoes = str_producoes.strip("{ }").replace(" ", "").replace("\n", "")
        self.str_producoes = str_producoes

        # Define a primeira variavel das producoes como variavel de partida.
        self.variavel_partida = str_producoes[0]

        for producao in str_producoes.split(","):
            variavel = producao.split("->")[0]
            producoes = set( producao.split("->")[1].split("|") )

            # Como esta na forma de chomsky, a gramatica esta simplificada e toda variavel gera um terminal.
            self.variaveis.add( variavel )

            for simbolo in producoes:
                if simbolo == simbolo.lower():
                    self.terminais.add( simbolo )

            self.dicionario_producoes[variavel] = producoes

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

