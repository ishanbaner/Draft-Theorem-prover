solve=Prover()

#For P o Q, the expression would be ['o','P','Q'] for o being in {'=>','and','or'}
#For not P, the expression would be ['not','P']
#For example
#Assuming P => (Q => R)
#Show: (not R) => (P => (not Q))

solve.lemmas+=[['=>','P',['=>','Q','R']]]
solve.solver(['=>',['not','R'],['=>','P',['not','Q']]])
