import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        total_bill = float(entry_bill.get())
        tip_percent = float(entry_tip.get())
        people = int(entry_people.get())
        tip_amount = (tip_percent / 100) * total_bill
        total_with_tip = total_bill + tip_amount
        per_person = round(total_with_tip / people, 2)
        label_result.config(text=f"Each Person Should Pay: ${per_person}")
    except Exception as e:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Tip Calculator")

tk.Label(root, text="Total Bill ($):").grid(row=0, column=0, padx=10, pady=5)
entry_bill = tk.Entry(root)
entry_bill.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Tip Percentage (e.g. 10, 12, 15):").grid(row=1, column=0, padx=10, pady=5)
entry_tip = tk.Entry(root)
entry_tip.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Number of People:").grid(row=2, column=0, padx=10, pady=5)
entry_people = tk.Entry(root)
entry_people.grid(row=2, column=1, padx=10, pady=5)

btn_calc = tk.Button(root, text="Calculate", command=calculate)
btn_calc.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()