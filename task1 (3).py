### fisrt vide0
print("***************Welcome to the roller coaster ride***************")

height=int(input("Enter your height: "))

ticket=0
if height>120:
    
    print("you can ride the roller coaster    ")
    age= int(input("Enter Your age:"))
    if age<=12:
        ticket+=5
        bill=ticket
        print("Your ticket price is:$"+str(ticket))

    if age>12 and age<18:
         ticket+=10
         bill=ticket
         print("Your ticket price is:$"+str(ticket))
    if age>=18:
         ticket+=15
         bill=ticket
         print("Your ticket price is:$"+str(ticket))

    photo=input("Do you want to take a photo? Y or N:")
    if photo=='y':
           bill+=3
           print(f"Your Total Bill Including Photos: {bill}" )
    else:
        print("You didn't take a photo")  

else:
    print("YOu Can't Ride the Roller Coaster")
