import tkinter as tk
import tkinter.font as tk_font


root = tk.Tk()
# root.geometry("300x100")
font_opt = tk_font.Font(family="Microsoft Sans Serif", size="10")
can_per = tk.Canvas(root,height=100,width=200)
can_per.grid(row=0,column=0)

value =0

def set_epoch(self):
    self.value = int(epoch_value.get())

epoch_value = tk.Entry(can_per)
epoch_value.grid(row=1,column=0)

set_epoch = tk.Button(can_per,text="Set Epoch",command=set_epoch)
set_epoch.grid(row=2,column=0)

def print_va(self):
    print(self.value)

root.mainloop()



