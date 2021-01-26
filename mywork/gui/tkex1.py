#!/usr/bin/env python3
import tkinter as tk

def main():
    def get_values():
        try:
            value1 = float(entry_first_number.get())
            value2 = float(entry_second_number.get())
        except ValueError as err:
            tk.

        return value1, value2

    def display_answer(value):
        answer_text.set(str(value))
        print(value)

    def add_values():
        value1, value2 = get_values()
        display_answer(value1 + value2)

    def multiply_values():
        value1, value2 = get_values()
        display_answer(value1 * value2)



    root = tk.Tk()
    root.title("Lame Calculator")

    tk.Label(root, text="Enter first number").pack()
    entry_first_number = tk.Entry(root)
    entry_first_number.pack()
    tk.Label(root, text="Enter second number").pack()
    entry_second_number = tk.Entry(root)
    entry_second_number.pack()
    tk.Label(root, text="Answer").pack()

    answer_text = tk.StringVar()

    entry_answer = tk.Entry(root, textvariable=answer_text)
    entry_answer.pack()


    button_add = tk.Button(text="ADD", command=add_values)
    button_add.pack()

    button_multiply = tk.Button(text="MULT", command=multiply_values)
    button_multiply.pack()

    button_exit = tk.Button(text="exit", command=quit)
    button_exit.pack()




    tk.mainloop()

if __name__ == "__main__":
    main()