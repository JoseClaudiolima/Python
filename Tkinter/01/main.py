import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def domath():
    miles = entry_int.get() * 1609.34
    String.set(f'{miles:.0f}')

#window = tk.Tk()
window = ttk.Window(themename = 'journal')
window.title('Demo')
window.geometry('300x150')

#title1
title_label = ttk.Label(master=window,text= "Miles to Meters",font='Arial 20 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master=window) #div

entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable= entry_int)

button = ttk.Button(master=input_frame,text = 'Convert', command=domath)

entry.pack(side = 'left',padx = 10)
button.pack(side = 'right')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
String = tk.StringVar()
output = ttk.Label(master=window,
                    text= 'Output',
                      font = 'Arial 20',
                        textvariable=String)
output.pack(pady=5)

#run
window.mainloop()
