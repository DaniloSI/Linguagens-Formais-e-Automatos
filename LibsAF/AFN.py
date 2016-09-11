from LibsAF.DFA import DFA

class AFN:

	
	def __init__(self):
		
		self.estadosCorrentes = set()
		self.alfabeto = set()
		self.estados = set()
		self.estadosFinais = set()
		self.estadoInicial = ""
		self.palavra = ""
		self.palavraInput = self.palavra
		self.transicoes = {}
	
	
	def executaAutomato(self, palavra):
		self.palavraInput = self.palavra = palavra
		
		# Verifica se o autômato tem que parar ou continuar
		while (self.continua()):
			
			# Consome um simbolo da palavra da esquerda para a direita
			simboloLido = self.consomeSimbolo()
			
			# Executa uma transição com o símbolo que foi lido
			self.estadosCorrentes = self.executaTransicao(simboloLido)

		
		# Reconhece se a palavra é válida, caso um dos estados atuais do conjunto estadosCorrentes estiver contido no conjunto estadosFinais
		if (len(self.estadosCorrentes.intersection(self.estadosFinais)) > 0):
			print("A palavra \"" + self.palavraInput + "\" foi reconhecida e o autômato parou nos estados: " + str(self.estadosCorrentes) + ".")
		else:
			print("A palavra \"" + self.palavraInput + "\" não foi reconhecida pelo autômato.")
	
	# A condição para continuar é ainda existir simbolo na palavra para ser consumido e o conjunto de estadosCorrentes possui estados.
	def continua(self):
		if (len(self.palavra) > 0 and len(self.estadosCorrentes) > 0 ):
			return True
		else:
			return False
	

	
	# Retorna um conjunto de estados de transições bem sucedidas.
	def executaTransicao(self, simbolo):
		estadosCorrentesReturn = set()

		# Para cada estado do conjunto estadosCorrentes, tenta fazer a transição com o símbolo lido.
		# Na primeira execução desse método, o conjunto estadosCorrentes só tem um elemento que é o estadoInicial
		while (len(self.estadosCorrentes) > 0):
			estadoPartida = self.estadosCorrentes.pop()
			
			# Tenta fazer a transição. Se for bem sucedida, estadosDestino recebe o conjunto de estados possíveis ao ler tal símbolo.
			# Se não for bem sucedida, estadosDestino recebe um conjunto vazio.
			try:
				estadosDestino = self.transicoes[estadoPartida][simbolo]
			except KeyError:
				estadosDestino = set()
			
			# estadosCorrentesReturn, recebe  uma união sucessiva de si mesmo (começando vazio) com os estados possíveis para cada transição.
			estadosCorrentesReturn = estadosCorrentesReturn.union(estadosDestino)
		
		return estadosCorrentesReturn
	
	
	def consomeSimbolo(self):
		
		# Retorna um símbolo da palavra e sobrescreve palavra com uma nova palavra sem o símbolo lido.
		simbolo = self.palavra[0]
		self.palavra = self.palavra[1:]
		
		return simbolo
	
	def addEstado(self, nomeEstado, transicao, stInicial=False, stFinal=False):
		
		self.estados.add(nomeEstado)
		setSimbolos = set( transicao.keys() )
		self.alfabeto = self.alfabeto.union( setSimbolos )
		self.transicoes[nomeEstado] = transicao

		if stInicial:
			self.estadoInicial = nomeEstado
			self.estadosCorrentes.add(nomeEstado)
		
		if stFinal:
			self.estadosFinais.add(nomeEstado)
	
	
	def toAFD(self):
		
		lstNomes = ["q0"]
		lstEstados = [set(["q0"])]
		afd = DFA()
		
		for setOfEstado in lstEstados:
			transicao = {}
			
			for simbolo in self.alfabeto:
				estadosDestino = set()

				for estado in setOfEstado:
					try:
						estadosDestino = estadosDestino.union(self.transicoes[estado][simbolo])
					except KeyError:
						estadosDestino = estadosDestino.union(set())
					
				
				if estadosDestino not in lstEstados:
					lstNomes.append("q" + str(len(lstEstados)))
					lstEstados.append(estadosDestino)
				
				transicao[simbolo] = lstNomes[lstEstados.index(estadosDestino)]
			
			estadoInicial = setOfEstado == lstEstados[0]
			estadoFinal = len( setOfEstado.intersection(self.estadosFinais) ) > 0
			
			afd.addEstado(lstNomes[lstEstados.index(setOfEstado)], transicao, stInic=estadoInicial, stFinal=estadoFinal)
		
		return afd


	
	
	
	
	
	
	
	
	
	
	
	
