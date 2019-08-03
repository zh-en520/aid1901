import tkinter

root = tkinter.Tk()

def mouseDown(e):
    print('鼠标按键按下x:',e.x,'y:',e.y,'按键：',e.num)
def mouseUp(e):
    print('鼠标按键抬起')

root.bind('<Button>',mouseDown)
root.bind('<ButtonRelease-1>',mouseUp)

def keyDown(e):
    print('键盘按键按下：',e.keysym)
def keyUp(e):
    print('键盘按键抬起：',e.keysym)

root.bind('<key>',keyDown)
root.bind('<keyRelease>',keyUp)

root.mainloop()