from Gramatica import Gramatica
from MatrixCmy import MatrixCmy


# Testa se uma palavra eh aceita por uma determinada GLC
class TesteGLC:

    def __init__(self, str_word, *producoes):
        # Cria a gramatica.
        self.gramatica = Gramatica()
        self.word = str_word

        # Quando utiliza-se *producoes, recebido uma lista de argumentos. Eh permitido passar qualquer quantidade de parametros.
        for producao in producoes:
            self.gramatica.set_producao( producao )

        # Cria a matrix Cmy a partir da gramatica.
        self.matrix = MatrixCmy(str_word, self.gramatica)

    def testar(self):
        self.matrix.generate_matrix()

        if self.matrix.palavra_valida():
            palavra_valida = "SIM"

        else:
            palavra_valida = "NAO"

        print("--- Gramatica ---")
        print(str(self.gramatica) + "\n")
        print("Palavra lida: " + self.word + "\n")
        print("Palavra valida ? Resposta: " + palavra_valida + "\n\n")


def main():

    TesteGLC("abaab",
             "S -> AA",
             "S -> AS",
             "S -> b",
             "A -> AS",
             "A -> AS",
             "A -> SA",
             "A -> a").testar()

    TesteGLC("abbabba",
             "S -> SF",
             "S -> a",
             "A -> CC",
             "A -> SS",
             "A -> CS",
             "C-> b",
             "F -> AS").testar()

    TesteGLC("abaab",
             "S -> AA",
             "S -> AS",
             "S -> b",
             "A -> AS",
             "A -> SA",
             "A -> a").testar()

    TesteGLC("aabbaa",
             "S -> AA",
             "S -> AS",
             "S -> b",
             "A -> AS",
             "A -> SA",
             "A -> a").testar()

    TesteGLC("aaabbabaaaabba",
             "S -> SF",
             "S -> a",
             "A->CG",
             "A-> SS",
             "A-> CS",
             "C -> b",
             "F -> AS",
             "G -> CA").testar()

    return 0

if __name__ == "__main__":
    main()
