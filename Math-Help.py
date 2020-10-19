from tkinter import *
import tkinter as tk
import tkinter.messagebox
from sympy import symbols, Eq, solve
from lineq import Problemr

TITLE_FONT = ('Courier New', 18, 'bold')
SUBTITLE_FONT =('Courier New', 15, 'bold')
APP_FONT = ('Courier New', 12)
FORMAT_FONT = ('Courier New', 18, 'bold')



class App(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('MathHelp')
        self.geometry('600x600+250+50')
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.config(width=400, height=400)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (MathHelp, LinerEQ):#,  math2, math3, math4
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame('MathHelp')
                    
        
        btn_exit = tk.Button(self, text = 'Exit', fg = 'black', bg = 'white', command = exit, font=APP_FONT)
        btn_exit.pack()
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
      
        
class MathHelp(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(self, text = 'Welcome To Math Help', font=TITLE_FONT)
        self.title.pack(side='top', fill='x', pady=10)
        self.select = tk.Label(self, text='Select what you want to solve!', font=SUBTITLE_FONT)
        self.select.pack(side='top', fill='x')
        self.book = tk.Label(self, text='', font=SUBTITLE_FONT)
        self.book.pack(side='top', fill='x')      
        
        self.L1Button = tk.Button(self,text='Linear Equation',bg='lawn green',width=20, height=5,command=lambda: controller.show_frame('LinerEQ'))
        self.L1Button.pack()
'''
        self.L2Button = tk.Button(self,text='Level 2',bg='orange2',command=lambda: controller.show_frame('math2'))
        self.L2Button.pack()

        self.L3Button = tk.Button(self,text='Level 3',bg='OrangeRed3',command=lambda: controller.show_frame('math3'))
        self.L3Button.pack()

        self.L4Button = tk.Button(self,text='Level 4',bg='red3',command=lambda: controller.show_frame('math4'))
        self.L4Button.pack() 
'''        
        
class LinerEQ(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        self.controller = controller
        label = tk.Label(self, text='Type the linear equation in given format', font=TITLE_FONT)
        label.pack(side='top', fill='x', pady=10)
        self. e = Entry(self, width=30)
        self.e.place(x=210, y=60)
        self.b = Button(self, text='Show Answer',bg='green',command=lambda: self.ShowAnswer())
        self.b.place(x=210, y=90)
        self.clr = Button(self, text='Clear Input',bg='red', command=lambda: self.ClearField())
        self.clr.place(x=350, y=90)
        self.btn_mm = tk.Button(self,text='Main Menu',command=lambda: controller.show_frame('MathHelp'))
        self.btn_mm.pack(side='bottom')
        self.p=tk.Label(self, text='Type in this format \n ax+by=c, dx+ey=f\n (You need not to care about spaces)', font=FORMAT_FONT)
        self.p.place(x=60, y=130)
        
    def ClearField(self):
        self.e.delete(0, 'end')
    
    def Problem(self, prb):
        ans = Problemr(prb)
        return ans
    
    def ShowAnswer(self):
        user_input = self.e.get()
        ans = self.Problem(user_input)
        tkinter.messagebox.showinfo('Your answer is', f'x = {ans[0]}\ny = {ans[1]}')    
      
    
            
                

if __name__=='__main__':
    root = App()
    root.mainloop()