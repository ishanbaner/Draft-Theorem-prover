# Draft-Theorem-prover
A simple prototype of a theorem prover.

It's a simple and basic structure of a theorem prover that deals with first-order logic. 
Expressions can be plugged in with the help of the solver method.

If the theorem is proved, the end output must be "Done", otherwise, for a wrong assumption, the end output will be "Wrong Assumption".

# Examples
1. Prove: P=>(Q=>P)
```python
solve=Solver()
solve.solver(['=>','P',['=>','Q','P']])

```
Output:
```
['=>', 'P', ['=>', 'Q', 'P']]
Assumption P
['=>', 'Q', 'P']
Done
```
2. Assume: P=>Q , Q=>R
   Prove: P=>R
```python
solve=Solver()
solve.lemmas+=['=>','P','Q']
solve.lemmas+=['=>','Q','R']
solve.solver(['=>','P','R'])

```
Output:
```
['=>', 'P', 'R']
Assumption P
Assumption ['=>', 'P', 'Q']
Assumption ['=>', 'Q', 'R']
Done
```
3. Prove: (a and b) => (b and (not a))
```python
solve=Solver()
solve.solver(['=>',['and','a','b'],['and','b',['not','a']]])
```
Output:
```
['=>', ['and', 'a', 'b'], ['and', 'b', ['not', 'a']]]
Assumption ['and', 'a', 'b']
['and', 'b', ['not', 'a']]
['and', 'b', ['not', 'a']]
['not', 'a']
Wrong assumption
```
# Improvements to be made
1. Significant improvements are needed to handle more complex cases as it's a very basic prototype.
2. Currently, it lacks important expressions like "for all" and "exists".
3. The code is not fully functional as in certain scenarios the code doesn't terminate. I will try to fix the problem asap.
4. Complex writing structure is definitely a problem that I will soon fix.
