import tkinter
root = tkinter.Tk()
btn1 = tkinter.Button(root,text='姓名')
btn1.grid(rowspan=2,column=0)

btn2 = tkinter.Button(root,text='张三')
btn2.grid(row=1,columnspan=2)

btn3 = tkinter.Button(root,text='李四')
btn3.grid(row=2,columnspan=2)
root.mainloop()