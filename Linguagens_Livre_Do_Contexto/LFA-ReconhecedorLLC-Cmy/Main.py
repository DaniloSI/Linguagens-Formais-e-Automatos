from Gramatica import Gramatica
from MatrixCmy import MatrixCmy


# Testa se uma palavra eh aceita por uma determinada GLC
class TesteGLC:

    def __init__(self, str_word, *producoes):
        # Cria a gramatica.
        self.gramatica = Gramatica()

        # Quando utiliza-se *producoes, recebido uma lista de argumentos. Eh permitido passar qualquer quantidade de parametros.
        for producao in producoes:
            self.gramatica.set_producao( producao )

        # Cria a matrix Cmy a partir da gramatica.
        self.matrix = MatrixCmy(str_word, self.gramatica)

    def testar(self, resultado_esperado):
        self.matrix.generate_matrix()

        if self.matrix.palavra_valida() == resultado_esperado:
            print("Ok!")

        else:
            print("Wrong!")

def main():

    TesteGLC("abaab",
             "S -> AA",
             "S -> AS",
             "S -> b",
             "A -> AS",
             "A -> AS",
             "A -> SA",
             "A -> a").testar(True)

    TesteGLC("abbabba",
             "S -> SF",
             "S -> a",
             "A -> CC",
             "A -> SS",
             "A -> CS",
             "C-> b",
             "F -> AS").testar(True)

    TesteGLC("abaab",
             "S -> AA",
             "S -> AS",
             "S -> b",
             "A -> AS",
             "A -> SA",
             "A -> a").testar(True)

    TesteGLC("aabbaa",
             "S -> AA",
             "S -> AS",
             "S -> b",
             "A -> AS",
             "A -> SA",
             "A -> a").testar(True)

    TesteGLC("aaabbabaaaabba",
             "S -> SF",
             "S -> a",
             "A->CG",
             "A-> SS",
             "A-> CS",
             "C -> b",
             "F -> AS",
             "G -> CA").testar(False)

    return 0

if __name__ == "__main__":
    main()
