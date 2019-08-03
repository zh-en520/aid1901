
import tkinter
root = tkinter.Tk()

label1 = tkinter.Label(root,bg='red',text='Label1')
label2 = tkinter.Label(root,bg='blue',text='Label2')
label3 = tkinter.Label(root,bg='green',text='Label3')

label1.pack()
label2.pack(side=tkinter.LEFT)
label3.pack(side=tkinter.RIGHT)
#label3.pack(side='bottom',fill=tkinter.Y,expand=1)


root.mainloop()