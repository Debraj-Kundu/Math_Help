#Required modules
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from lineq import Problemr
from Ap import AP
from Gp import GP

#Font styles
TITLE_FONT = ('Courier New', 18, 'bold')
SUBTITLE_FONT =('Courier New', 15, 'bold')
APP_FONT = ('Courier New', 12)
FORMAT_FONT = ('Courier New', 18, 'bold')


#Main App
class App(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('MathHelp')
        #UI Configurations
        self.geometry('600x600+250+50')
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.config(width=400, height=400)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #Frame Navigation
        self.frames = {} #dictionary to store frame name and properties
        for F in (MathHelp, LinerEQ, Series, ApSeries, GpSeries):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        #Call to raise the passed frame
        self.show_frame('MathHelp')
        #Exit button
        btn_exit = tk.Button(self, text = 'Exit', fg = 'black', bg = 'white', command = exit, font=APP_FONT)
        btn_exit.pack()
    #Show frame function
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
      
#Math frame class      
class MathHelp(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #UI configurations
        self.title = tk.Label(self, text = 'Welcome To Math Help', font=TITLE_FONT)
        self.title.pack(side='top', fill='x', pady=10)
        self.select = tk.Label(self, text='Select what you want to solve!', font=SUBTITLE_FONT)
        self.select.pack(side='top', fill='x')
        self.book = tk.Label(self, text='', font=SUBTITLE_FONT)
        self.book.pack(side='top', fill='x')      
        
        self.L1Button = tk.Button(self,text='Linear Equation',bg='lawn green',width=20, height=5,command=lambda: controller.show_frame('LinerEQ'))
        self.L1Button.pack()

        self.L2Button = tk.Button(self,text='Series',bg='orange2',width=20, height=5, command=lambda: controller.show_frame('Series'))
        self.L2Button.pack()
'''
        self.L3Button = tk.Button(self,text='Level 3',bg='OrangeRed3',command=lambda: controller.show_frame('math3'))
        self.L3Button.pack()

        self.L4Button = tk.Button(self,text='Level 4',bg='red3',command=lambda: controller.show_frame('math4'))
        self.L4Button.pack() 
'''        

#Liner equations frame class    
class LinerEQ(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        self.controller = controller
        #UI configurations
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
    
    #Clear text inside entry widget
    def ClearField(self):
        self.e.delete(0, 'end')
    
    def Problem(self, prb):
        ans = Problemr(prb) #from lineq module calling Problemr function
        return ans # returning to ShowAnswer funtion
    
    #Taking the input from entry widget and calling the logic to solve
    def ShowAnswer(self):
        user_input = self.e.get()
        if user_input != '':
            ans = self.Problem(user_input)
            #Display answer in messagebox
            tkinter.messagebox.showinfo('Your answer is', f'x = {ans[0]}\ny = {ans[1]}')
        #ehcek if the input is empty
        else:
              tkinter.messagebox.showerror('Invalid Input','Enter valid input accorting to fromat specified')

#Series frame class
class Series(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #UI configurations
        self.select = tk.Label(self, text='Select what you want to solve!', font=SUBTITLE_FONT)
        self.select.pack(side='top', fill='x')   
        
        self.L1Button = tk.Button(self,text='AP Series',bg='lawn green',width=20, height=5,command=lambda: controller.show_frame('ApSeries'))
        self.L1Button.pack()

        self.L2Button = tk.Button(self,text='GP Series',bg='orange2',width=20, height=5, command=lambda: controller.show_frame('GpSeries'))
        self.L2Button.pack()

        self.btn_mm = tk.Button(self,text='Main Menu',command=lambda: controller.show_frame('MathHelp'))
        self.btn_mm.pack(side='bottom')


#Ap frame class
class ApSeries(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        self.controller = controller
        #UI configurations
        label = tk.Label(self, text='Enter Values accordingly', font=TITLE_FONT)
        label.pack(side='top', fill='x', pady=10)
        self.l1 = tk.Label(self, text='Enter First Number of an A.P Series: ', font=TITLE_FONT)
        self.l1.pack()
        self.e1 = Entry(self, width=20)
        self.e1.pack()

        self.l2 = tk.Label(self, text='Enter the Total Numbers in this A.P Series: ', font=TITLE_FONT)
        self.l2.pack()
        self.e2 = Entry(self, width=20)
        self.e2.pack()

        self.l3 = tk.Label(self, text='Enter the Common Difference : ', font=TITLE_FONT)
        self.l3.pack()
        self. e3 = Entry(self, width=20)
        self.e3.pack()

        self.b = Button(self, text='Show Answer',bg='green',command=lambda: self.ShowAnswer())
        self.b.pack()

        self.btn_mm = tk.Button(self,text='Previous',command=lambda: controller.show_frame('Series'))
        self.btn_mm.pack(side='bottom')   
    
    def Problem(self, prb):
        ans = AP(prb) #from Ap module calling AP function
        return ans # returning to ShowAnswer funtion
    
    #Taking the input from entry widget and calling the logic to solve
    def ShowAnswer(self):
        user_input = self.e1.get()+','+self.e2.get()+','+self.e3.get()
        if user_input != '':
            ans = self.Problem(user_input)
            ans = ans.split(',')
            #Display answer in messagebox
            tkinter.messagebox.showinfo('Your answer is', f'Last Term of AP Series = {ans[0]}\nSum of AP Series = {ans[1]}\nGenrated series: {ans[2]}')
        #ehcek if the input is empty
        else:
              tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')

#Gp frame class
class GpSeries(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        self.controller = controller
        #UI configurations
        label = tk.Label(self, text='Enter Values accordingly', font=TITLE_FONT)
        label.pack(side='top', fill='x', pady=10)
        self.l1 = tk.Label(self, text='Enter First Number of an G.P Series: ', font=TITLE_FONT)
        self.l1.pack()
        self.e1 = Entry(self, width=20)
        self.e1.pack()

        self.l2 = tk.Label(self, text='Enter the Total Numbers in this G.P Series: ', font=TITLE_FONT)
        self.l2.pack()
        self.e2 = Entry(self, width=20)
        self.e2.pack()

        self.l3 = tk.Label(self, text='Enter the Common Ratio : ', font=TITLE_FONT)
        self.l3.pack()
        self. e3 = Entry(self, width=20)
        self.e3.pack()

        self.b = Button(self, text='Show Answer',bg='green',command=lambda: self.ShowAnswer())
        self.b.pack()

        self.btn_mm = tk.Button(self,text='Previous',command=lambda: controller.show_frame('Series'))
        self.btn_mm.pack(side='bottom')   
    
    def Problem(self, prb):
        ans = GP(prb) #from Ap module calling AP function
        return ans # returning to ShowAnswer funtion
    
    #Taking the input from entry widget and calling the logic to solve
    def ShowAnswer(self):
        user_input = self.e1.get()+','+self.e2.get()+','+self.e3.get()
        if user_input != '':
            ans = self.Problem(user_input)
            ans = ans.split(',')
            #Display answer in messagebox
            tkinter.messagebox.showinfo('Your answer is', f'Sum of GP Series = {ans[0]}\nGenrated series: {ans[1]}')
        #ehcek if the input is empty
        else:
              tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
           
                
#Main loop control 
if __name__=='__main__':
    root = App()
    root.mainloop()