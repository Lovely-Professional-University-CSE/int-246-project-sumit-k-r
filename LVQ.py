import tkinter as tk
import tkinter.font as tk_fonts
from Parkinson_LvQ import *

def LVQ_train_test():

    root = tk.Tk()
    LVQ_main = tk.Frame(root, height=900, width=500, bg="black",highlightthickness=1)
    LVQ_main.grid(row=0,column=0)
    font_opt = tk_fonts.Font(family="Microsoft Sans Serif", size="15")

    button_bar = tk.Frame(LVQ_main,bg="black")
    button_bar.pack(fill=tk.X)

    
    epoch_label = tk.Label(button_bar,text="Epoch",bg="green",width=20,fg="white",font=font_opt)
    epoch_label.grid(row=0,column=1, padx=10,pady=10)
    n_epochs_scale = tk.Scale(button_bar,from_=1,to = 100,orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    n_epochs_scale.grid(row=1,column=1, padx=10,pady=10)

   
    l_rate_label = tk.Label(button_bar,text="Learn Rate",bg="green",width=20,fg="white",font=font_opt)
    l_rate_label.grid(row=0,column=2, padx=10, pady=10)
    learn_rate_scale = tk.Scale(button_bar,from_=0.0,to = 1.0,resolution=0.01, orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    learn_rate_scale.grid(row=1,column=2, padx=10,pady=10)

    
    n_folds_label = tk.Label(button_bar,text="Folds",bg="green",width=20,fg="white",font=font_opt)
    n_folds_label.grid(row=0,column=4, padx=10,pady=10)
    n_folds_scale = tk.Scale(button_bar,from_=1,to = 20,orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    n_folds_scale.grid(row=1,column=4, padx=10,pady=10)

  
    n_codebooks_label = tk.Label(button_bar,text="Rows in each fold",bg="green",width=20,fg="white",font=font_opt)
    n_codebooks_label.grid(row=0,column=3, padx=10,pady=10)
    n_codebooks_scale = tk.Scale(button_bar,from_=0,to = 20,orient=tk.HORIZONTAL,length=230,bg="#00f5dc",font=font_opt)
    n_codebooks_scale.grid(row=1,column=3, padx=10,pady=10)


    n_epochs = 0
    learn_rate = 0.0
    n_codebooks = 0
    n_folds = 0

    def set_value():
        n_epochs = n_epochs_scale.get()
        learn_rate = learn_rate_scale.get()
        n_codebooks = n_codebooks_scale.get()
        n_folds = n_folds_scale.get()

        print("EPOCH : ",n_epochs)
        print("L_RATE : ",learn_rate)
        print("FOLDS  : ",n_folds)
        print("ROWS in each fold  : ",n_codebooks)
        LVQ_train(n_folds, n_codebooks, learn_rate, n_epochs)
        root.destroy()


    run_sim = tk.Frame(LVQ_main, bg="black")
    run_sim.pack(fill=tk.X)

    run_sim_button = tk.Button(run_sim,text="Set Values !",bg="green",fg="white",font=font_opt,command=set_value)
    run_sim_button.pack(fill=tk.BOTH, pady=15)

    root.mainloop()
