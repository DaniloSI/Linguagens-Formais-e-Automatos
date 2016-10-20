from LibsAF.AFN import AFN
from LibsAF.DFA import DFA


def main():
	
	# Teste 1
	teste = AFN()
	
	palavra = "abaabbaabaaaa"
	
	teste.addEstado( "q0", {"a":set(["q0", "q1"]), "b":set(["q0"])}, stInicial = True)
	teste.addEstado( "q1", {"a":set(["q2"])} )
	teste.addEstado( "q2", {"a":set(["qf"])})
	teste.addEstado( "qf", {}, stFinal = True)
	
	afd = teste.toAFD()
	afd.executaAutomato(palavra)
	
	return 0


if __name__ == "__main__":
	main()
