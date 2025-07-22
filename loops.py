def count(x):
    c = 0
    for a in x:
        c = c + 1
    return c
def sum(x): #[1,2,[3,4],5,6]
    c = 0
    for a in x:
        if type(a) is list:
            sum(a)
            #for b in a:
            #    c = c + b
        else:
            c = c + a
    return c
def cr2e(a,c=0):
    if a == []:
        return c
    elif type(a[0]) is list:
        c1 = cr2e(a[0])
        return cr2e(a[1:],c+c1)
    else:
        return cr2e(a[1:],c+1)
print (cr2e([1,[[2]],3,4,5]))
if not []:
    print("empty")
input = "i need rest"
split = input.split()
print(split)
