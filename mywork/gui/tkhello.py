import tkinter as tk

def main():
    root = tk.Tk()

    root.geometry("500x75+400-200")
    root.maxsize(width=600, height=200)
    root.minsize(width=350, height=60)

    root.title("Hello World")

    lab_hello = tk.Label(
        root, 
        text="Hello, UMBC World",
        fg="red",
        font=("Times", 42
        ),
    )
    lab_hello.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

