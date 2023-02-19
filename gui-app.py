import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame1, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame1, text="Test button", font=40)
button.place(relx=0.7, relwidth=0.3, relheight=1)

# frame2 = tk.Frame(root, bg='#80c1ff')
# frame2.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.5)

# label = tk.Label(frame, text="This is a Label", bg='yellow', fg='red')
# label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)

# entry = tk.Entry(frame, bg='green')
# entry.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)

root.mainloop()