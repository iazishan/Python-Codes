print("***********Welcome TO The Treasure Island************")
print("Your mission is to find the treasure.")

choice=input("You are corssing a river. Type left or right to go forward: ")
if choice=="left":
    ch2=input("you are at lake now. Type swim or wait:")    
    if ch2=="wait":
        ch3=input("Your at now a door.Type Red,Blue and Yellow to move forward")
        if ch3=="Red":
            print("Game Over")
        elif ch3=="Blue":
            print("Game Over")
        elif ch3=="yellow":
            print("You Win")
        else:
            print("You chose a wrong door")
    else:
        print("Game Over")
else:
    print("Game Over")



    ########## After GUI

    import tkinter as tk
from tkinter import messagebox

def start_game():
    def river_choice():
        choice = river_var.get().lower()
        if choice == "left":
            lake_choice()
        else:
            messagebox.showinfo("Result", "Game Over")

    def lake_choice():
        lake_win = tk.Toplevel(root)
        lake_win.title("Lake Choice")
        tk.Label(lake_win, text="You are at a lake. Type swim or wait:").pack()
        lake_var = tk.StringVar()
        tk.Entry(lake_win, textvariable=lake_var).pack()
        def next():
            ch2 = lake_var.get().lower()
            if ch2 == "wait":
                lake_win.destroy()
                door_choice()
            else:
                lake_win.destroy()
                messagebox.showinfo("Result", "Game Over")
        tk.Button(lake_win, text="Next", command=next).pack()

    def door_choice():
        door_win = tk.Toplevel(root)
        door_win.title("Door Choice")
        tk.Label(door_win, text="You are now at a door. Type Red, Blue or Yellow to move forward:").pack()
        door_var = tk.StringVar()
        tk.Entry(door_win, textvariable=door_var).pack()
        def finish():
            ch3 = door_var.get().lower()
            if ch3 == "red":
                door_win.destroy()
                messagebox.showinfo("Result", "Game Over")
            elif ch3 == "blue":
                door_win.destroy()
                messagebox.showinfo("Result", "Game Over")
            elif ch3 == "yellow":
                door_win.destroy()
                messagebox.showinfo("Result", "You Win")
            else:
                door_win.destroy()
                messagebox.showinfo("Result", "You chose a wrong door")
        tk.Button(door_win, text="Finish", command=finish).pack()

    game_win = tk.Toplevel(root)
    game_win.title("Treasure Island")
    tk.Label(game_win, text="You are crossing a river. Type left or right to go forward:").pack()
    river_var = tk.StringVar()
    tk.Entry(game_win, textvariable=river_var).pack()
    tk.Button(game_win, text="Next", command=lambda: [game_win.destroy(), river_choice()]).pack()

root = tk.Tk()
root.title("Treasure Island Game")
tk.Label(root, text="***********Welcome TO The Treasure Island************").pack()
tk.Label(root, text="Your mission is to find the treasure.").pack()
tk.Button(root, text="Start Game", command=start_game).pack()
root.mainloop()