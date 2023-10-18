import tkinter as tk
from tkinter import messagebox
window= tk.Tk()
window.title("Car Loan Calculator")
def calculate_monthly_payment():
    try:
        price=float(entry_price.get())
        down_payment=float(entry_down_payment.get())
        rate=float(entry_rate.get())
        years=float(entry_num_years.get())
        i=rate/1200
        n=years*12
        monthly_payment=((price-down_payment)*i*(1+i) **n)/((1+i)**n-1)
        result_label.config(text="Monthly Payment: $ {:.2f}".format(monthly_payment))
    except ValueError:
        messagebox.showerror("Please enter valid numbers.")
tk.Label(window,text="Price of Car(price):").grid(row=0, column=0,)
entry_price=tk.Entry(window)
entry_price.grid(row=0, column=1)
tk.Label(window, text="Down Payment(down_payment): ").grid(row=1,column=0)
entry_down_payment=tk.Entry(window)
entry_down_payment.grid(row=1,column=1)
tk.Label(window, text="Annual Percentage Rate(R):").grid(row=2, column=0)
entry_rate=tk.Entry(window)
entry_rate.grid(row=2,column=1)
tk.Label(window, text="Number of Years(Years):").grid(row=3, column=0)
entry_num_years=tk.Entry(window)
entry_num_years.grid(row=3, column=1)
calculate_button=tk.Button(window, text="Calculate", command=calculate_monthly_payment)
calculate_button.grid(row=4,column=0)
result_label=tk.Label(window, text="")
result_label.grid(row=5, column=0)
window.mainloop()