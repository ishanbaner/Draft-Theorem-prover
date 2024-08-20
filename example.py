solve=Prover()
solve.lemmas+=[['=>','P',['=>','Q','R']]]
solve.solver(['=>',['not','R'],['=>','P',['not','Q']]])
