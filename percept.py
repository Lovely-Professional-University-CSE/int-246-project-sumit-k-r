import tkinter as tk
import tkinter.font as tk_fonts
from Parkinsons_Perceptron import *

def perceptron():
    root = tk.Tk()
    percept_main = tk.Frame(root, height=900, width=500, bg="black",highlightthickness=1)
    percept_main.grid(row=0,column=0)
    font_opt = tk_fonts.Font(family="Microsoft Sans Serif", size="15")

    button_bar = tk.Frame(percept_main,bg="black")
    button_bar.pack(fill=tk.X)

    epoch = tk.DoubleVar()
    epoch_label = tk.Label(button_bar,text="Epoch",bg="green",width=20,fg="white",font=font_opt)
    epoch_label.grid(row=0,column=1, padx=10,pady=10)
    epoch_scale = tk.Scale(button_bar,from_=1,to = 500,orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    epoch_scale.grid(row=1,column=1, padx=10,pady=10)

    l_rate = tk.DoubleVar()
    l_rate_label = tk.Label(button_bar,text="Learn Rate",bg="green",width=20,fg="white",font=font_opt)
    l_rate_label.grid(row=0,column=2, padx=10, pady=10)
    l_rate_scale = tk.Scale(button_bar,from_=0.0,to = 1.0,resolution=0.01, orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    l_rate_scale.grid(row=1,column=2, padx=10,pady=10)

    threshold = tk.DoubleVar()
    threshold_label = tk.Label(button_bar,text="Threshold",bg="green",width=20,fg="white",font=font_opt)
    threshold_label.grid(row=0,column=4, padx=10,pady=10)
    threshold_scale = tk.Scale(button_bar,from_=0.0,to = 1.0,resolution=0.01,orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    threshold_scale.grid(row=1,column=4, padx=10,pady=10)

    bias = tk.DoubleVar()
    bias_label = tk.Label(button_bar,text="Bias",bg="green",width=20,fg="white",font=font_opt)
    bias_label.grid(row=0,column=3, padx=10,pady=10)
    bias_scale = tk.Scale(button_bar,from_=0.0,to = 1.0,resolution=0.01,orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    bias_scale.grid(row=1,column=3, padx=10,pady=10)


    epoch_val =0
    l_rate_val = 0.0
    threshold_val = 0.0
    bias_val = 0.0

    def set_value():
        epoch_val = epoch_scale.get()
        l_rate_val = l_rate_scale.get()
        threshold_val = threshold_scale.get()
        bias_val = bias_scale.get()

        print("EPOCH : ",epoch_val)
        print("L_RATE : ",l_rate_val)
        print("BIAS  : ",bias_val)
        print("THRESHOLD : ",threshold_val)
        train_test(epoch_val,bias_val,l_rate_val,threshold_val)
        root.destroy()


    run_sim = tk.Frame(percept_main, bg="black")
    run_sim.pack(fill=tk.X)

    run_sim_button = tk.Button(run_sim,text="Set Values !",bg="green",fg="white",font=font_opt,command=set_value)
    run_sim_button.pack(fill=tk.BOTH, pady=15)

    root.mainloop()
