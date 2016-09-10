from LibsAF.AFN import AFN
from LibsAF.FileReadAF import FileReadAF

def main():
	
	alfabeto = set(["a", "b"])
	estados = set(["q0", "q1", "q2", "qf"])
	estadosFinais = set(["qf"])
	estadoInicial="q0"
	palavra="abaabaaa"
	transicoes={"q0":{"a":set(["q0", "q1"]), "b":set(["q0"])}, "q1":{"a":set(["q2"])}, "q2":{"a":set(["qf"])}}
	
	teste = AFN(alfabeto, estados, estadosFinais, estadoInicial, palavra, transicoes)
	
	teste.executaAutomato()
	
	leitor = FileReadAF("teste.txt", FileReadAF.AFN)
	
	leitor.getAF().executaAutomato()
	
	
	return 0
	
if __name__ == "__main__":
	main()
