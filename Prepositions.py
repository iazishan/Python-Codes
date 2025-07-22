def negation(p):
    if p == 0:
        return 1
    else:
        return 0

####def bijection(p, q):
   ### if (p == 1 and q == 1) or (p == 0 and q == 0):
   ###     return 1
   #### else:
    ###    return 0

def disjunction(p, q):
    if p == 1:
        return 1
    elif q == 1:
        return 1
    else:
        return 
    
def conjunction(p, q):
            if p == 1 and q == 1:
                return 1
            else:
                return 0

def implication(p, q):
    if p == 1 and q == 0:
        return 0
    else:
        return 1




p = 1
q = 0


print("Negation Of P:", negation(p))
print("Conjunction Of P and q:", conjunction(p, q))
print("Disjunction Of P and q:", disjunction(p, q))

print("Implication Of P and q:", implication(p, q))



