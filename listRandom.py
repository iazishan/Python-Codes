import random
person=['bob','wick','john','swiss','james','bond']

###Select Random person to pay bill

### Pahla tarika
print(random.choice(person))

### Doosra tarika
random_index=random.randint(0,5)
print(person[random_index])

