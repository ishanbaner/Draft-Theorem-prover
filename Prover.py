from collections import deque

class Prover:
    
    def __init__(self):
        self.vals={}
        self.vals[True]=True
        self.vals[False]=False
        self.lemmas=[]
        
    def And(self,a,b):
        if a not in self.vals.keys() and b not in self.vals.keys():
            return('IC')
        if a==False or b==False:
            return(False)
        if self.vals[a] and self.vals[b]:
            return(True)
        return(False)
    
    def Or(self, a,b):
        if a not in self.vals.keys() or b not in self.vals.keys():
            return('IC')
        if self.vals[a] or self.vals[b]:
            return(True)
        return(False)

    def Implies(self,a,b):
        if a not in self.vals.keys() or b not in self.vals.keys():
            return('IC')
        return not self.vals[a] or self.vals[b]    

    def Not(self,a):
        if a not in self.vals.keys():
            return('IC')
        if a==False:
            return(True)
        elif a==True:
            return(False)
        if self.vals[a]==True:
            return(False)
        else:
            return(True)
    
    def assumeTrue(self,v):
        print("Assumption",v)
        if type(v)!=list:
            self.vals[v]=True
        else:
            if v[0]=='and':
                if type(v[1])!=list:
                    self.vals[v[1]]=True
                if type(v[1])!=list:
                    self.vals[v[2]]=True
            elif v[0]=='not':
                print(v[1],"is False")
                self.vals[v[1]]=False
            elif v[0]=='=>':
                if type(v[1])!=list:
                    if v[1] in self.vals.keys():
                        if self.vals[v[1]]:
                            if type(v[2])!=list:
                                self.vals[v[2]]=True
                            else:
                                self.assumeTrue(v[2])
                    
                elif type(v[1])==list:
                    if self.solver(v[1])==True:
                        if type(v[2])!=list:
                            self.vals[v[2]]==True
                        else:
                            self.assumeTrue(v[2])
                if type(v[2])!=list:
                    if v[2] in self.vals.keys():
                        if self.vals[v[2]]==False:
                            if type(v[1])!=list:
                                self.vals[v[1]]=False
                            else:
                                self.assumeFalse(v[1])
                elif type(v[2])==list:
                    if self.solver(v[2])==True:
                        if type(v[1])!=list:
                            self.vals[v[1]]==True
                        else:
                            self.assumeTrue(v[1])

                    elif self.solver(v[2])==False:
                        if type(v[1])!=list:
                            self.vals[v[1]]=False
                        else:
                            self.assumeFalse(v[1])

    def assumeFalse(self,v):
        self.vals[v]=False

    def remove_spaces(self,s):
        su=""
        for ch in s:
            if ch!=' ' and ch!='':
                su+=ch
        return(su)
    
    def is_reachable_bfs(self,graph, start, target):
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            if node not in visited:
                visited.add(node)
                queue.extend(graph.get(node, []))
        
        return False
    
    def variables(self,l):
        vari=[]
        for i in range(1,len(l)):
            if type(l[i])!=list:
                vari+=[l[i]]
            else:
                vari+=self.variables(l[i])
        return(vari)

    def solveAssumption(self,g,t):
        lemmas=self.lemmas
        '''
        contr=False
        if t:
            print("Say ",g," is False")
            self.assumeFalse(g)
        elif t==False:
            print("Say ",g," is True")
            self.assumeTrue(g)

        for l in lemmas:
            if g not in self.variables(l):
                self.assumeTrue(l)
            else:
                if (self.solver(l))==False:
                    print(self.solver(l))
                    contr=True
        if contr:
            print("Proved by contradiction")
        else:
            print("Wrong Assumption")
    
        #if (self.vals[g])==t:
        #    print('Done')
        '''
        for l in lemmas:
            if g not in self.variables(l):
                self.assumeTrue(l)
        for l in lemmas:
            if g in self.variables(l):
                self.assumeTrue(l)
        if (self.vals[g])==t:
            print('Done')
        

    def solver(self,exp):
        if type(exp)!=list:
            if exp in self.vals.keys():
                if self.vals[exp]:
                    print("Done")
                else:
                    print("Wrong assumption")

        if exp[0]=='=>':
            print(exp)
            if type(exp[2])!=list :
                if exp[2] in self.vals.keys():
                    if self.vals[exp[2]]==True:
                    
                        print('Done')
                        return(True) 
                    
                if (exp[1] in self.vals.keys()) and (exp[2] in self.vals.keys()):
                    print(exp)
                    if self.Implies(exp[1][-1],exp[2][-1]):
                        print("Done") 
                        return(True)
                    else:
                        print("Wrong assumption")
                        return(False)
                else:
                    self.assumeTrue(exp[1])
                    self.solver(exp[2])
            else:
                self.assumeTrue(exp[1])
                self.solver(exp[2])
        
        elif exp[0]=='and':
            print(exp)
            if exp[1]==False or exp[2]==False:
                print("Wrong assumption ")
                return(False)
            elif exp[1]==True and exp[2]==True:
                print('Done')
                return(False)
            elif type(exp[1])!=list and type(exp[2])!=list: 
                if (exp[1] in self.vals.keys()) and (exp[2] in self.vals.keys()):
                    print(exp)
                    if self.And(exp[1][-1],exp[2][-1]):
                        print("Done") 
                        return(True)
                    else:
                        print("Wrong assumption")
                        return(False)
            elif type(exp[1])!=list and type(exp[2])==list: 
                if (exp[1] in self.vals.keys()):
                    print(exp)
                    if self.vals[exp[1]]==False:
                        print("Wrong assumption")
                        return(False)
                    else:
                        return(self.solver(exp[2]))
            elif type(exp[1])==list and type(exp[2])!=list: 
                if (exp[2] in self.vals.keys()):
                    print(exp)
                    if self.vals[exp[2]]==False:
                        print("Wrong assumption")
                        return(False)
                    else:
                        return(self.solver(exp[1]))
            else:
                print(self.And(self.solver(exp[1]),self.solver(exp[2])))
                return(self.And(self.solver(exp[1]),self.solver(exp[2])))
            
        elif exp[0]=='not':
            print(exp)
            if exp[1]==True:
                print("Wrong assumption")
                return(False)
            elif (exp[1] in self.vals.keys()):
                if self.Not(exp[1]):
                    print("Done") 
                    return(True)
                else:
                    print("Wrong assumption")
                    return(False)
            else:
                #print("To show",exp[1],"is false")
                state=self.Not(self.solver(exp[1]))
                if state=='IC':
                    self.solveAssumption(exp[1],False)
                return(state)
            
        elif exp[0]=='or':
            print(exp)
            if exp[1]==False and exp[2]==False:
                print("Wrong assumption")
                return(False)
            elif (exp[1][-1] in self.vals.keys()) and (exp[2][-1] in self.vals.keys()):
                if self.Or(exp[1][-1],exp[2][-1]):
                    print("Done") 
                    return(True)
                else:
                    print("Wrong assumption")
                    return(False)
            else:
                return(self.Or(self.solver(exp[1]),self.solver(exp[2])))
            
        else:
            self.solveAssumption(exp,True)

solve=Prover()
## A few examples:

#solve.assumeFalse('a')
#solve.solver(['and','a',['not','a']])

#solve.solver(['=>','P',['=>','Q','P']])

#solve.lemmas+=[['=>','P',['=>','Q','R']]]
#solve.solver(['=>',['not','R'],['=>','P',['not','Q']]])

#solve.lemmas+=[['=>','P','Q']]
#solve.lemmas+=[['=>','R',['not','Q']]]
#solve.lemmas+=[['=>','R','S']]
#solve.solver(['=>','P',['not','R']])

#solve.lemmas+=[['=>','P','Q']]
#solve.lemmas+=[['=>','Q','R']]
#solve.solver(['=>','P','R'])
