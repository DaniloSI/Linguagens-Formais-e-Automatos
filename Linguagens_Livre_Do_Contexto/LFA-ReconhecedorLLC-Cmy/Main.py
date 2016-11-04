from Gramatica import Gramatica
from MatrixCmy import MatrixCmy


# Testa se uma palavra eh aceita por uma determinada GLC
class TesteGLC:

    def __init__(self, str_word, list_producoes):
        # Cria a gramatica.
        self.gramatica = Gramatica()
        self.word = str_word

        # Quando utiliza-se *producoes, recebido uma lista de argumentos. Eh permitido passar qualquer quantidade de parametros.
        for producao in list_producoes:
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


def read_file_productions(str_file):
    list_producoes = list()
    
    arquivo = open(str_file, 'r')
    
    producao = arquivo.readline()
    while producao != "":
        list_producoes.append( producao.strip("\n") )
        
        producao = arquivo.readline()
    
    return list_producoes
    
    

def main():

    word = input("Entre com a palavra: ")
    path_file = input("Entre com o caminho completo do arquivo incluindo o arquivo: ")
    
    TesteGLC(word, read_file_productions(path_file) ).testar()

    return 0

if __name__ == "__main__":
    main()
