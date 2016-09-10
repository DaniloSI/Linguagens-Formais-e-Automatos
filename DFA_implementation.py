from DFA import DFA

dfa = DFA()

dfa.adiciona_estado('1', {'a':'2', 'b':'3'}, st_inic=1)
dfa.adiciona_estado('2', {'a':'2', 'b':'2'}, st_final=1)
dfa.adiciona_estado('3', {'a':'2'})

dfa.executa("bbabababababababababababababababab")
