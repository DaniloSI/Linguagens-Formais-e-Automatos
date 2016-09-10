class DFA:
	
	
	
	
	def __init__(self):
		self.estados = set()
		self.alfabeto = set()
		self.transicao = {}
		self.estadoInicial = ""
		self.estadosFinais = set()

	def addEstado(self, nomeEstado, transicao, stInic=0, stFinal=0):
	
		self.estados.add(nomeEstado)
		self.transicao[nomeEstado] = transicao
		simbolos = set( transicao.keys() )
		self.alfabeto = self.alfabeto.union(simbolos)

		if stInic:
			self.estadoInicial = nomeEstado
		if stFinal:
			self.estadosFinais.add(nomeEstado)

	def executaAutomato(self, sentenca):
		 
		if self.estadoInicial == "":
			raise ("Initialization Error", "deve existir um estado inicial")
		if len(self.estadosFinais) == 0:
			raise ("Initialization Error", "deve existir pelo menos um estado final")

		estadoAtual = self.estadoInicial

		for simbolo in sentenca:
			try:
				estadoAtual = self.transicao[estadoAtual][simbolo]
			except KeyError:
				print ("A sentenca '" + sentenca + "' nao foi reconhecida pelo automato.")
				return

		if estadoAtual in self.estadosFinais:
			print ("A sentenca '" + sentenca + "' foi reconhecida pelo automato com estado final " + estadoAtual + ".")
		else:
			print ("A sentenca '" + sentenca + "' nao foi reconhecida pelo automato.")
