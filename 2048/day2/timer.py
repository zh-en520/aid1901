import tkinter

root = tkinter.Tk()

def onTimer():
    print('启动定时器')
    global timer_id
    timer_id = root.after(1000,onTimer)

timer_id = root.after(1000,onTimer)

def stoptimer():
    root.after_cancel(timer_id)

btn = tkinter.Button(root,text='取消定时',command=stoptimer)
btn.pack()

root.mainloop()