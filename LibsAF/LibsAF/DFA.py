class DFA:
   def __init__(self, processaSimbolo = None):
      self.estados = []
      self.alfabeto = set([])
      self.transicao = {}
      self.estadoInicial = None
      self.estadosFinais = []
      
      if processaSimbolo:
         self.processaSimbolo = processaSimbolo
      else:
         self.processaSimbolo = lambda x: x

   def adiciona_estado(self, nome, transicao, st_inic=0, st_final=0):
      self.estados.append(nome)
      self.transicao[nome] = transicao
      simbolos = set(transicao.keys())
      self.alfabeto = self.alfabeto.union(simbolos)
      
      if st_inic:
         self.estadoInicial = nome
      if st_final:
         self.estadosFinais.append(nome)

   def executa(self, sentenca):
	   
      if not self.estadoInicial:
         raise ("Initialization Error", "deve existir um estado inicial")
      if not self.estadosFinais:
         raise ("Initialization Error", "deve existir pelo menos um estado final")

      estadoAtual = self.estadoInicial

      for simbolo in sentenca:
         simbolo = self.processaSimbolo(simbolo)
         
         try:
            estadoAtual = self.transicao[estadoAtual][simbolo]
         except KeyError:
            print ("A sentenca '" + sentenca + "' nao foi reconhecida pelo automato.")
            return
               
      if estadoAtual in self.estadosFinais:
         print ("A sentenca '" + sentenca + "' foi reconhecida pelo automato com estado final " + estadoAtual + ".")
      else:
         print ("A sentenca '" + sentenca + "' nao foi reconhecida pelo automato.")
