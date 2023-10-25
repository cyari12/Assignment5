import tkinter as tk
def calculate_bmi():
    weight=float(weight_entry.get())
    height=float(height_entry.get())
    bmi=(weight * 703)/(height**2)
    bmi_label.config(text=f"Your BMI is:{bmi:2f}")
    if bmi<18.5:
        status_label.config(text="You are underweight.")
    elif 18.5<=bmi<25:
        status_label.config(text="You have an optimal weight.")
    else:
        status_label.config(text="You are overweight.")
window=tk.Tk()
window.title("BMI Calculator")
weight_label = tk.Label(window, text="Enter your weight in pounds:")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1)


height_label = tk.Label(window, text="Enter your height in inches:")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1)


bmi_label = tk.Label(window, text="")
bmi_label.grid(row=2, column=0, columnspan=2)


status_label = tk.Label(window, text="")
status_label.grid(row=3, column=0, columnspan=2)


calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=4, column=0, columnspan=2)


window.mainloop()