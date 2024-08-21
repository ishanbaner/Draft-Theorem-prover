# Draft-Theorem-prover
A simple prototype of a theorem prover.

It's a simple and basic structure of a theorem prover that deals with first-order logic. 
Expressions can be plugged in with the help of the solver method.

# Examples
1. P=>(Q=>P)
```
solve=Solver()
solve.solver(['=>','P',['=>','Q','P']])

```
2. Assume: P=>Q , Q=>R
   P=>R
```
solve=Solver()
solve.lemmas+=['=>','P','Q']
solve.lemmas+=['=>','Q','R']
solve.solver(['=>','P','R'])

```

# Improvements to be made
Significant improvements are needed but it's a very basic prototype.
Currently, it lacks important expressions like "for all" and "exists".

The code is not fully functional as in certain scenarios the code doesn't terminate. I will try to fix the problem asap.
