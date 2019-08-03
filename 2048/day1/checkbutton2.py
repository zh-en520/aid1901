import tkinter
root = tkinter.Tk()


def kanshu():
    print('看书按钮被按下')
    print('看书按钮的值是：',v.get())

#创建一个关联变量，关联check_btn
ｖ = tkinter.IntVar(root,value=0)

check_btn = tkinter.Checkbutton(root,text='看书',command=kanshu,variable=v)
check_btn.pack()

root.mainloop()