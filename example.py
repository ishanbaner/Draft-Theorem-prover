solve=Prover()

#Assuming P => (Q => R)
#Show: (not R) => (P => (not Q))

solve.lemmas+=[['=>','P',['=>','Q','R']]]
solve.solver(['=>',['not','R'],['=>','P',['not','Q']]])
