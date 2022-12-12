import tkinter as tk
import keyboard
import time


root = tk.Tk()


text_box = tk.Entry(root)
text_box.pack()


button = tk.Button(root, text="Simulate Keyboard Input")
button.pack()


def simulate_keyboard_input():

    keyboard.press("alt")
    keyboard.press_and_release("tab")
    keyboard.release("alt")

    time.sleep(0.2) 

    
    text = text_box.get()

    



    keyboard.write(text)


button.config(command=simulate_keyboard_input)


root.mainloop()