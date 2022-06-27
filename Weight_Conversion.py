import tkinter as tk

def convert():
    result_gram = float(entry_kg.get()) * 1000
    result_pounds = float(entry_kg.get()) * 2.20462
    result_ounce = float(entry_kg.get()) * 35.274


    lbl_gram_display.config(text=str(result_gram))
    lbl_pounds_display.config(text=str(result_pounds))
    lbl_ounce_display.config(text=str(result_ounce))


window = tk.Tk()
window.geometry("400x300")

# Khai bao cac frame tren window
first_frame = tk.Frame(window, pady=10)
first_frame.pack()

second_frame = tk.Frame(window, pady = 10)
second_frame.pack()

third_frame = tk.Frame(window, pady=10)
third_frame.pack()

# Khai bao cac widget con tren window
lbl_enter_kg = tk.Label(first_frame, text="Enter the weight in Kg")
entry_kg = tk.Entry(first_frame)
btn_convert = tk.Button(first_frame, text="Convert", command=convert)

lbl_gram = tk.Label(second_frame, text = "Gram")
lbl_pounds = tk.Label(second_frame, text = "Pounds")
lbl_ounce = tk.Label(second_frame, text="Ounce")

lbl_gram_display = tk.Label(third_frame, text="")
lbl_pounds_display = tk.Label(third_frame, text="")
lbl_ounce_display = tk.Label(third_frame, text="")


# Khai bao vi tri bang grid
lbl_enter_kg.grid(row=0, column=0)
entry_kg.grid(row=0, column=1, padx=10)
btn_convert.grid(row=0, column=2)

lbl_gram.grid(row=1, column=0)
lbl_pounds.grid(row=1, column=1, padx= 70)
lbl_ounce.grid(row=1, column=2)

lbl_gram_display.grid(row=2, column=0,padx=5)
lbl_ounce_display.grid(row=2, column=1, padx=65)
lbl_pounds_display.grid(row=2, column=2,padx=5)

window.mainloop()
