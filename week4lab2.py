# *******************************No Parameters******************************************************************

def print_Name():
    for i in range(10):
      print("Zishan")







print_Name()
# *********************************Parameters****************************************************************


def print_Name(X,Y):
      for i in range(X,Y):
       print(i ,end="'")
      print("izhar")



print_Name(1,5)
# ***********************************Staric me variable lazmi**************************************************************      

def print_Name(*,X,Y):
      for i in range(X,Y):
       print(i ,end="'")
      print("fahad")




print_Name(Y=6,X=10)
 # ***********************************Backspace me no variables**************************************************************     

def print_Name(X,Y,/):
      for i in range(X,Y):
       print(i ,end="'")
      print("kailo")







print_Name(1,5)  
#**********************jitny marzi argument dee orbitary argument//tuple recieve hoty hn*********************************************

def print_name(*x):
    for i in range (x):
        print(i , end = ' ')
        print("Marwat")


print_name(1,2,3,4,5,6,7,8,9,10)



def print_name(*x):
    print("Mawat")
    for i in range (len(x)):
        print(type(x))
        print(i , end = ' ')










