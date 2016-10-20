from Gramatica import Gramatica

class MatrixCmy:

    def __init__(self, word, gramatica):
        self.word = word
        self.gramatica = gramatica

    # Gera a matriz utilizando o algoritmo de Cmy
    def generate_matrix(self):
        self.matrix = list()

        # Cria a primeira linha da matriz com as variaveis que geram seus respectivos terminais
        self.matrix.append( list() )
        for j in range( len(self.word) ):
            terminal = self.word[j]
            variaveis = self.gramatica.get_left_side_production( terminal )

            self.matrix[0].append( variaveis )


        # Nesse loop, a variavel i vai da segunda linha da matriz ate a ultima.
        for i in range(1, len(self.word)):
            self.matrix.append( list() )

            for j in range( len(self.word) - i ):
                self.matrix[i].append( set() )

                for k in range(i):
                    # cartesian_product eh um produto cartesiano da concatenacao entre dois conjuntos de variaveis
                    # Por definicao do algoritmo, o k deve ir de 1 ate i-1. Como k inicia em 0, definimos k + 1 para normalizar.
                    cartesian_product = self.generate_product_cartesian( self.matrix[k][j], self.matrix[i - (k + 1)][ j + (k + 1)] )

                    # Para cada concatenacao de variaveis, eh feita uma uniao sucessiva.
                    # O resultado dessas unioes eh um conjunto de variveis que consegue-se chegar a uma dessas concatenacoes.
                    for right_side_production in cartesian_product:
                        variaveis = self.gramatica.get_left_side_production( right_side_production )

                        self.matrix[i][j] = self.matrix[i][j].union( variaveis )


    def palavra_valida(self):

        if self.gramatica.get_variavel_partida() in self.matrix[len(self.word) - 1][0]:
            return True
        else:
            return False

    def generate_product_cartesian(self, set_variaveis_one, set_variaveis_two):
        cartesian_product = list()

        if len(set_variaveis_one) == 0 or len(set_variaveis_two) == 0:
            return set_variaveis_one.union( set_variaveis_two )

        for variavel_one in set_variaveis_one:
            for variavel_two in set_variaveis_two:
                cartesian_product.append( variavel_one + variavel_two )

        return cartesian_product
