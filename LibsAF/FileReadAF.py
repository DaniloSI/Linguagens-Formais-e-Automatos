from LibsAF.AFN import AFN
from LibsAF.DFA import DFA



class FileReadAF:
	
	# Arquivo que contém o autômato
	afFilePath = ""
	
	# Opções sendo AFD para Autômato Finito Deterministico e AFN para Autômato Finito Não Deterministico.
	AFD = 1
	AFN = 2
	
	afType = 0
	
	# Autômato em formato de string do jeito que foi lido do arquivo.
	strAF = ""
	
	
	# Seta o caminho do autômato e o tipo.
	def __init__(self, afFilePath = "", afType = 0):
		
		self.afFilePath = afFilePath
		self.afType = afType

	# Retorna o autômato lido do arquivo baseado no tipo.
	def getAF(self):
		
		self.readAF()
		
		if (self.afType == self.AFN):
			return self.generateAFN()
		
		else:
			return self.generateAFD()
	
	
	def readAF(self):
		try:
			fileAF = open(self.afFilePath, 'r')
		except IOError:
			print("Arquivo inválido")
		
		self.strAF = fileAF.read()
		
		fileAF.close()

	# Gera um AFN.
	def generateAFN(self):
		
		afn = AFN()
		
		listParts = self.strAF.split("\n")
		
		# Não pode existir o caractere espaço (" ") no arquivo. Abaixo, um exemplo de entrada válida:
		'''
		q0
		qf
		q0,a-q0-q1,b-q0
		q1,a-q2
		q2,a-qf
		abababbaaabababaaaaababbaaaabaaa
		'''
		
		# A primeira linha do arquivo é o estado inicial
		estadoInicial = listParts[0]
		
		# A segunda linha do arquivo são os estados finais
		estadosFinais = set(listParts[1].split(","))
		
		# Da teceira linha até a penúltima, são as transições
		# Para cada linha que contém uma transição, uma chave que é o nome do estado e os valores que são transições para cada símbolo.
		for transicao in listParts[2:-1]:
			partsTransicao = transicao.split(",")
			
			# O primeiro elemento é o estado de partida e é uma chave para o dicionário de transições.
			transicoes = {}
			
			# st são as transições separadas por "-". O primeiro elemento de st é um símbolo e os demais são estados.
			for st in partsTransicao[1:]:
				
				sEstados = st.split("-")
				simbolo = sEstados[0]
				transicoes[simbolo] = set(sEstados[1:])

			nomeEstado = partsTransicao[0]
			afn.addEstado(nomeEstado, transicoes, nomeEstado == estadoInicial, nomeEstado in estadosFinais)


		# Retorna o AFN.
		return afn
