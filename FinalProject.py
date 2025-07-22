#### rock paper scissors game 
## 1 for rock 
## 2 for paper
## 3 for scissors
import random

print("***********************Welcome to the Rock, Paper, Scissors Game!***********************")
def game():
  cpu=['rock', 'paper', 'scissors']
  choice=int(input("Press 1 for rock, 2 for paper, and 3 for scissors: "))

  if choice==1:
    print("You chosse: Rock")
    CPU=random.choice(cpu)
    print("CPU choose:", CPU)
    if CPU=='rock':
        print("It,s a tie. Try Again")
        game()
    if CPU=='paper':
       print("You Lose, Try Again")
       game()
    if CPU=='scissors':
       print("You WIn")
       game()


  if choice==2:
    print('Your choose: Paper')
    CPU=random.choice(cpu)
    print("Cpu choose:",CPU)
    if CPU=='Paper':
        print("It,s a tie. Try Again")
        game()
    if CPU=='rock':
       print("You Win")
       game()
    if CPU=='scissors':
       print("You Loose, Try Again")
       game()





  if choice==3:
    print('Your choose: Scissors')
    CPU=random.choice(cpu)
    print("Cpu choose:",CPU)
    if CPU=='scissors':
        print("It,s a tie. Try Again")
        game()
    if CPU=='paper':
       print("You Win")
       game()
    if CPU=='rock':
       print("You Loose, Try Again")
       game()

  else:
       print("Invalid choice! Please select 1, 2, or 3.")       

game()

################ After GUI


import random
import tkinter as tk
from tkinter import messagebox

def play(choice):
   cpu = ['rock', 'paper', 'scissors']
   user_choice = ['rock', 'paper', 'scissors'][choice-1]
   cpu_choice = random.choice(cpu)

   result = ""
   if user_choice == cpu_choice:
      result = f"Both chose {user_choice}. It's a tie!"
   elif (user_choice == 'rock' and cpu_choice == 'scissors') or \
       (user_choice == 'paper' and cpu_choice == 'rock') or \
       (user_choice == 'scissors' and cpu_choice == 'paper'):
      result = f"You chose {user_choice}, CPU chose {cpu_choice}. You win!"
   else:
      result = f"You chose {user_choice}, CPU chose {cpu_choice}. You lose!"

   messagebox.showinfo("Result", result)

def main():
   root = tk.Tk()
   root.title("Rock, Paper, Scissors Game")

   tk.Label(root, text="Welcome to the Rock, Paper, Scissors Game!", font=("Arial", 14)).pack(pady=10)
   tk.Label(root, text="Choose your move:", font=("Arial", 12)).pack(pady=5)

   btn_frame = tk.Frame(root)
   btn_frame.pack(pady=10)

   tk.Button(btn_frame, text="Rock", width=10, command=lambda: play(1)).grid(row=0, column=0, padx=5)
   tk.Button(btn_frame, text="Paper", width=10, command=lambda: play(2)).grid(row=0, column=1, padx=5)
   tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play(3)).grid(row=0, column=2, padx=5)

   root.mainloop()

if __name__ == "__main__":
   main()
