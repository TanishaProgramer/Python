import tkinter

m = tkinter.Tk()

m.title("Student Management System")

button1 = tkinter.Button(m,text ="buy now",command = m.destroy,borderwidth=0,bd = 0, bg = "red",fg ="white",width=30,margin=10)



button1.pack()
m.mainloop()



