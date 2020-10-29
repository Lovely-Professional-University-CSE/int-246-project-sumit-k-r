import tkinter as tk
import tkinter.font as tk_font


root = tk.Tk()
root.title("Parkinson's Disease")
root.geometry("1380x920")
root.config(background="#000000")
root.resizable(height="false", width="false")
fonts = tk_font.Font(family="Bahnschrift SemiBold", size="30")
font_opt = tk_font.Font(family="Microsoft Sans Serif", size="15")

canvas = tk.Canvas(root, height=960, width=420, bg="black", highlightthickness=1,highlightbackground="black")
canvas.grid(row=0, column=0, padx=10, pady=5)

canvas_line = tk.Canvas(root, bg="white", highlightthickness=1,highlightbackground="black",width=1,height=880)
canvas_line.grid(row=0, column=1, pady=5)

canvas_photo = tk.Canvas(root, height=890, width=900, bg="black", highlightthickness=1,highlightbackground="black")
canvas_photo.grid(row=0, column=2, padx=15, pady=5)

menu_text1 = tk.Label(canvas, text="Parkinson's Disease ", font=fonts,
                      fg="#ffffff", bg="black")
menu_text1.grid(row=0, column=3, padx=20, pady=20)

menu_text2 = tk.Label(canvas, text=" classification using ", font=fonts,
                      fg="#ffffff", bg="black")
menu_text2.grid(row=2, column=3, padx=20, pady=20)

space_men = tk.Label(canvas, pady=30, background="black")
space_men.grid(row=4, column=3, pady=15)

space_men = tk.Label(canvas, pady=30, background="black")
space_men.grid(row=5, column=3, pady=15)

per = tk.Button(canvas, text="Perceptron", width=30,
                font=font_opt, fg="#ffffff", bg="#078a42")
per.grid(row=6, column=3, pady=15)

svm = tk.Button(canvas, text="SVM ( Support Vector Machine )", width=30,
                font=font_opt, fg="#ffffff", bg="#078a42")
svm.grid(row=7, column=3, pady=15)

lvq = tk.Button(canvas, text="LVQ ( Linear Vector Quantization )", width=30,
                font=font_opt, fg="#ffffff", bg="#078a42")
lvq.grid(row=8, column=3, pady=15)

som = tk.Button(canvas, text="SOM ( Self-Organizing Map )", width=30,
                font=font_opt, fg="#ffffff", bg="#078a42")
som.grid(row=9, column=3, pady=15)

space_men = tk.Label(canvas, pady=20, background="black")
space_men.grid(row=10, column=3, pady=15)

exit_app = tk.Button(canvas, text="Quit", width=30, font=font_opt,
                     command=root.destroy, fg="#ffffff", bg="#078a42")
exit_app.grid(row=11, column=3, pady=30)

root.mainloop()
