from Gramatica import Gramatica
from MatrixCmy import MatrixCmy


# Testa se uma palavra eh aceita por uma determinada GLC
class TesteGLC:

    def __init__(self, str_word, str_gramatica):
        # Cria a gramatica.
        self.gramatica = Gramatica(str_gramatica)

        # Cria a matrix Cmy a partir da gramatica.
        self.matrix = MatrixCmy(str_word, self.gramatica)

    def testar(self, resultado_esperado):
        self.matrix.generate_matrix()

        if self.matrix.palavra_valida() == resultado_esperado:
            print("Ok!")

        else:
            print("Wrong!")

def main():

    TesteGLC("abaab", "{S -> AA | AS | b, A -> AS | AS | SA | a}").testar(True)
    TesteGLC("abbabba", "{S -> SF | a, A -> CC | SS | CS, C-> b, F -> AS}").testar(True)
    TesteGLC("abaab", "{S -> AA | AS | b, A -> AS | SA | a}").testar(True)
    TesteGLC("aabbaa", "{S -> AA | AS | b, A -> AS | SA | a}").testar(True)

    TesteGLC("aaabbabaaaabba", "S->SF|a, A->CG|SS|CS, C -> b, F -> AS, G -> CA").testar(False)

    return 0

if __name__ == "__main__":
    main()
