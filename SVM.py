import tkinter as tk
import tkinter.font as tk_fonts
from Parkinsons_SVM import *
def SVM():
    root = tk.Tk()
    SVM_main = tk.Frame(root, height=900, width=300, bg="black",highlightthickness=1)
    SVM_main.grid(row=0,column=0)
    font_opt = tk_fonts.Font(family="Microsoft Sans Serif", size="15")

    button_bar = tk.Frame(SVM_main,bg="black")
    button_bar.pack(fill=tk.X)

    c_val = tk.DoubleVar()
    c_label = tk.Label(button_bar,text="Range of C",bg="green",width=20,fg="white",font=font_opt)
    c_label.grid(row=0,column=1, padx=10,pady=10)
    c_scale = tk.Scale(button_bar,from_=1,to = 500,orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    c_scale.grid(row=1,column=1, padx=10,pady=10)

    c_setval = 0
    def set_cval():
        c_setval = c_scale.get()
        print("Range of C :", c_setval)
        SVM_train(c_setval)
        root.destroy()
    
    run_sim = tk.Frame(SVM_main, bg="black")
    run_sim.pack(fill=tk.X)

    run_sim_button = tk.Button(run_sim,text="Set Values !",bg="green",fg="white",font=font_opt,command=set_cval)
    run_sim_button.pack(fill=tk.BOTH, pady=15)
