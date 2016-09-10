from LibsAF.AFN import AFN
from LibsAF.FileReadAF import FileReadAF


def main():
	
	# Teste 1
	teste = AFN()
	
	palavra = "abaabaaabaaa"
	
	teste.addEstado( "q0", {"a":set(["q0", "q1"]), "b":set(["q0"])}, stInicial = True)
	teste.addEstado( "q1", {"a":set(["q2"])} )
	teste.addEstado( "q2", {"a":set(["qf"])})
	teste.addEstado( "qf", {}, stFinal = True)
	
	teste.executaAutomato(palavra)



	# Teste 2
	leitor = FileReadAF("teste.txt", FileReadAF.AFN)
	
	leitor.getAF().executaAutomato("abababbaaabababaaaaababbaaaabaaa")
	
	
	return 0
	
if __name__ == "__main__":
	main()
