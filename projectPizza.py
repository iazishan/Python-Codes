print("                                                                                                                           ")
print("************************welcome to the delivery pizza Service**************************")

bill=0
size=input("What size pizza do you want? S, M, L: ")
if size=='S':
    bill+=15
if size=='M':
    bill+=20
if size=='L':
    bill+=30
mio=input("Do you want Mionesse on pizza? Y/N: ")
if size=='S' and mio=='Y':
    bill+=2
if size=='M' and mio=='Y':
    bill+=3
    
if size=='L' and mio=='Y':
    bill+=5
cheese=input("Do you want cheese on pizza? Y/N: ")
if cheese=='Y':
    bill+=3 
    print(f"Your total Bill= {bill}")
else:
    print(f"Your total Bill= {bill}")