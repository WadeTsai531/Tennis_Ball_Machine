import tkinter as tk

window = tk.Tk()
window.title('Test GUI')
window.geometry('640x360')

def Close_Window():
    window.destroy()

def visible():
    label_1.pack_forget()

label_1 = tk.Label(window, text='Page 1')
label_1.pack()

button = tk.Button(window, text='next', command=visible )
button.pack()

close_button = tk.Button(window, text='close', command=Close_Window)
close_button.place(x=550, y=300)

window.mainloop()
