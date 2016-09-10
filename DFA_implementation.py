from LibsAF.DFA import DFA

dfa = DFA()

dfa.addEstado('1', {'a':'2', 'b':'3'}, stInic=True)
dfa.addEstado('2', {'a':'2', 'b':'2'}, stFinal=True)
dfa.addEstado('3', {'a':'2'})

dfa.executaAutomato("babababababababababababababababab")
