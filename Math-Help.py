#Required modules
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from lineq import Problemr
from Ap import AP
from Gp import GP
from Qudratic_Eqution import Quadratic_eqation                                                            # added by sourav
from Volumes_surfaces import cube,cone,cuboid,sphere,hollow_sphere,cylinder,hollow_cylinder,frustum       # added by sourav

#UI credits goes to Sourav
#Error Handling and UX by Debraj Kundu
#Logic and planning by all members


#Font styles
TITLE_FONT = ('Times New Roman', 25, 'italic bold')                              # font style changed to 'Times new roman' from 'Courier New' by Sourav 
TITLE_FONT = ('Courier New', 18, 'bold')
SUBTITLE_FONT =('Courier New', 15, 'bold')
APP_FONT = ('Courier New', 12)
FORMAT_FONT = ('Courier New', 18, 'bold')
INSTRUCTION_FONT=('Arial',10,'bold')
SERIES_FONT=('times new roman',12)


# Main App by Debraj Kundu
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
        for F in (MathHelp, LinerEQ,Quadratic_eqations,volume_area,Series,ApSeries,GpSeries):
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
      
#Math frame class by Debraj Kundu 
class MathHelp(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #UI configurations
        self.title = tk.Label(self, text = 'Math Help',fg='maroon' ,font=('times new roman',32,'italic bold'))
        self.title.place(x=190,y=40)
        self.book = tk.Label(self, text='Welcome to Math Help..! A Program to ease your math \ncalculations.Get solutions of Quadratic Eqations,Linear Equations,\nVolumes & Areas and Series.',fg='red',font=('Times new roman',12,'bold'))       
        self.book.place(x=40,y=120)                   # added by sourav  
        self.select = tk.Label(self, text='Select what you want to solve!', fg='green',font=('arial',14,'bold'))
        self.select.place(x=155,y=200)     
        
        self.L1Button = tk.Button(self,text='Linear Equation',bg='sky blue',width=20, height=5,command=lambda: controller.show_frame('LinerEQ'))
        self.L1Button.place(x=120,y=250)
# buttons modified and introduced by Sourav
        self.L2Button = tk.Button(self,text='Quadratic Equations',bg='sky blue',width=20, height=5,command=lambda: controller.show_frame('Quadratic_eqations'))
        self.L2Button.place(x=320,y=250)
        self.L3Button = tk.Button(self,text='Volume & Surface area',bg='sky blue',width=20, height=5,command=lambda: controller.show_frame('volume_area'))
        self.L3Button.place(x=120,y=390)
        self.L4Button = tk.Button(self,text='Series',bg='sky blue',width=20, height=5,command=lambda: controller.show_frame('Series'))
        self.L4Button.place(x=320,y=390)       
# till here by sourav  [buttons only] 
       

#Liner equations frame class by Debraj Kundu
class LinerEQ(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        self.controller = controller
        #UI configurations
        tittle=tk.Label(self,text='Linear Equation Solver',font=('times new roman',30,'italic bold'),fg='maroon')
        tittle.place(x=80,y=50)
        label = tk.Label(self,fg='green' ,text='Here you can solve Linear Equations in two variables.\nEnter two equations of 2 variables and click on [Show Answer].\n\n *Note = For refrence look at example below.', font=('arial',11,'bold'))   # font & context changed to instructon font from tittle font by sourav
        label.place(x=50,y=150)
        equation = tk.Label(self, text='Equations :', font=INSTRUCTION_FONT)   # font changed to instructon font from tittle font by sourav
        equation.place(x=90,y=280)
        self.e = Entry(self, width=40)               #widhth changed to 40 from 30 by sourav
        self.e.place(x=180, y=280)
        self.b = Button(self, text='Show Answer',bg='green',fg='white',command=lambda: self.ShowAnswer()) #fg chnged to white
        self.b.place(x=200, y=330)
        self.clr = Button(self, text='Clear Input',bg='red',fg='white',command=lambda: self.ClearField()) #fg changed to white
        self.clr.place(x=300, y=330)
        self.btn_mm = tk.Button(self,text='Main Menu',bg='light green',command=lambda: controller.show_frame('MathHelp'))   #bg changed to light green
        self.btn_mm.pack(side='bottom')
        self.p=tk.Label(self, text='Type in this format:--> \nExamples: ax+by=c, dx+ey=f\n (You do not need to care about spaces)', font=('times new roman',15))
        self.p.place(x=110, y=400)    #some formating in text and style made by sourav
    
    #Clear text inside entry widget
    def ClearField(self):
        self.e.delete(0, 'end')
    
    def Problem(self, prb):
        ans = Problemr(prb) #from lineq module calling Problemr function
        return ans # returning to ShowAnswer funtion
    
    #Taking the input from entry widget and calling the logic to solve
    def ShowAnswer(self):
        user_input = self.e.get()
        ans = self.Problem(user_input)
        if user_input != '' and ans != 'invalid' and ans != 'coma' and ans != 'eq': 
            #Display answer in messagebox
            tkinter.messagebox.showinfo('Your answer is', f'x = {ans[0]}\ny = {ans[1]}')
        #ehcek if the input is empty
        else:
            if ans == 'coma':
                tkinter.messagebox.showerror('Invalid Input','Put a comma in between the equations')
            elif ans == 'eq':
                tkinter.messagebox.showerror('Invalid Input','You need to have an equality operator for it to be an equation')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input accorting to fromat specified')

#Series frame class by Siddhant Singh and Debraj Kundu
class Series(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #UI configurations
        self.select = tk.Label(self, text='Series Solver',fg='maroon' ,font=('times new roman',35,'italic bold'))
        self.select.place(x=150,y=50) 
        self.select = tk.Label(self,fg='dark green' ,text='Welcome to Series Solver!\n The program can help you solve \n Arithmetic Progressions and Geomertic Progressions', font=('times new roman',13,'bold'))
        self.select.place(x=70,y=150)                 
        self.select = tk.Label(self, fg='forest green',text='Select what you want to solve!', font=('arial',15,'bold'))
        self.select.place(x=130,y=270)   
        
        self.L1Button = tk.Button(self,text='AP Series',bg='sky blue',width=20, height=5,command=lambda: controller.show_frame('ApSeries'))
        self.L1Button.place(x=100,y=350)

        self.L2Button = tk.Button(self,text='GP Series',bg='sky blue',width=20, height=5, command=lambda: controller.show_frame('GpSeries'))
        self.L2Button.place(x=320,y=350)

        self.btn_mm = tk.Button(self,text='Main Menu',bg='light green',command=lambda: controller.show_frame('MathHelp'))
        self.btn_mm.pack(side='bottom')


#Ap frame class Siddhant Singh and Debraj Kundu
class ApSeries(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        self.controller = controller
        #UI configurations
        tittle=tk.Label(self,text='Arithmetic Progressions\nSolver',font=('times new roman',28,'italic bold'),fg='maroon')
        tittle.place(x=80,y=50)
        label = tk.Label(self,fg='green', text=' Solve for the Sum of Arithmetic Progressions\nGet the Sum of N terms of an A.P,Last term and \nGenerated Series\n\nEnter Values Accordingly.', font=('arial',12,'bold'))
        label.place(x=90,y=190)
        self.l1 = tk.Label(self, text='Enter First Number of an A.P : ', font=SERIES_FONT)
        self.l1.place(x=50,y=330)
        self.e1 = Entry(self, width=20)
        self.e1.place(x=350,y=330)

        self.l2 = tk.Label(self, text='Enter the Total Numbers in this A.P : ', font=SERIES_FONT)
        self.l2.place(x=50,y=370)
        self.e2 = Entry(self, width=20)
        self.e2.place(x=350,y=370)

        self.l3 = tk.Label(self, text='Enter the Common Difference : ', font=SERIES_FONT)
        self.l3.place(x=50,y=410)
        self. e3 = Entry(self, width=20)
        self.e3.place(x=350,y=410)

        self.b = Button(self, text='Show Answer',width=18,height=2,fg='white',bg='green',command=lambda: self.ShowAnswer())
        self.b.place(x=225,y=465)

        self.btn_mm = tk.Button(self,width=10,bg='light green',text='Previous',command=lambda: controller.show_frame('Series'))
        self.btn_mm.pack(side='bottom')   
    
    def Problem(self, prb):
        ans = AP(prb) #from Ap module calling AP function
        return ans # returning to ShowAnswer funtion
    
    #Taking the input from entry widget and calling the logic to solve
    def ShowAnswer(self):
        user_input = self.e1.get()+','+self.e2.get()+','+self.e3.get()
        ans = self.Problem(user_input)
        if user_input != '' and ans != 'invalid' and ans != 'invalid n':
            ans = ans.split(',')
            #Display answer in messagebox
            tkinter.messagebox.showinfo('Your answer is', f'Last Term of AP Series = {ans[0]}\nSum of AP Series = {ans[1]}\nGenrated series: {ans[2]}')
        #ehcek if the input is empty
        else:
            if ans == 'invalid n':
                tkinter.messagebox.showerror('Invalid Input','Number of elements should be greater than 0')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')

#Gp frame class Siddhant Singh and Debraj Kundu
class GpSeries(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        self.controller = controller
        #UI configurations
        tittle=tk.Label(self,text='Geometric Progressions\nSolver',font=('times new roman',28,'italic bold'),fg='maroon')
        tittle.place(x=80,y=50)        
        label = tk.Label(self,fg='green', text=' Solve for the Sum of Geometric Progressions\nGet the Sum of N terms of an G.P and Generated Series.\n\nEnter Values Accordingly.', font=('arial',12,'bold'))
        label.place(x=60,y=190)
        self.l1 = tk.Label(self, text='Enter First Number of an G.P : ', font=SERIES_FONT)
        self.l1.place(x=50,y=330)
        self.e1 = Entry(self, width=20)
        self.e1.place(x=350,y=330)

        self.l2 = tk.Label(self, text='Enter the Total Numbers in this G.P : ', font=SERIES_FONT)
        self.l2.place(x=50,y=370)
        self.e2 = Entry(self, width=20)
        self.e2.place(x=350,y=370)

        self.l3 = tk.Label(self, text='Enter the Common Ratio : ', font=SERIES_FONT)
        self.l3.place(x=50,y=410)
        self. e3 = Entry(self, width=20)
        self.e3.place(x=350,y=410)

        self.b = Button(self, text='Show Answer',width=18,height=2,fg='white',bg='green',command=lambda: self.ShowAnswer())
        self.b.place(x=225,y=465)

        self.btn_mm = tk.Button(self,width=10,bg='light green',text='Previous',command=lambda: controller.show_frame('Series'))
        self.btn_mm.pack(side='bottom')   
    
    def Problem(self, prb):
        ans = GP(prb) #from Ap module calling AP function
        return ans # returning to ShowAnswer funtion
    
    #Taking the input from entry widget and calling the logic to solve
    def ShowAnswer(self):
        user_input = self.e1.get()+','+self.e2.get()+','+self.e3.get()
        ans = self.Problem(user_input)
        if user_input != '' and ans != 'invalid' and ans != 'invalid n':
            ans = ans.split(',')
            #Display answer in messagebox
            tkinter.messagebox.showinfo('Your answer is', f'Sum of GP Series = {ans[0]}\nGenrated series: {ans[1]}')
        #Chcek if the input is empty
        else:
            if ans == 'invalid n':
                tkinter.messagebox.showerror('Invalid Input','Number of elements should be greater than 0')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')

# classes introduced by sourav 
class Quadratic_eqations(tk.Frame):    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller 
        tittle=tk.Label(self,text="Quadratic Equation Solver",foreground='maroon',font=TITLE_FONT)
        tittle.place(x=80,y=60)
        equation=tk.Label(self,text="Equation : Ax^2+Bx+C = 0",foreground='green',font=('Times new roman',14,'bold'))
        equation.place(x=180,y=160)
        instruction=tk.Label(self,text="Instruction : Please enter the values of A,B,C to solve the euation.\n\n( A = Coefficient of x^2, B = Coefficient of x and C = Constant )",font=INSTRUCTION_FONT)
        instruction.place(x=70,y=210)
        A=tk.Label(self,text="A :",font=INSTRUCTION_FONT)      #A is display label and self.A is entry widget for A
        A.place(x=190,y=290)
        self.A=Entry(self,width=20)
        self.A.place(x=220,y=290)
        B=tk.Label(self,text="B :",font=INSTRUCTION_FONT)      #B is display label and self.A is entry widget for B
        B.place(x=190,y=320)
        self.B=Entry(self,width=20)
        self.B.place(x=220,y=320)
        C=tk.Label(self,text="C :",font=INSTRUCTION_FONT)       #C is display label and self.A is entry widget for C
        C.place(x=190,y=350)
        self.C=Entry(self,width=20)
        self.C.place(x=220,y=350) 

        self.bttn =tk.Button(self, text='Solve',bg= 'sky blue',width=16,height=2,command=lambda: self.Display())  # callling Display function on clicking 
        self.bttn.place(x=228,y=410)  
        self .clr =tk.Button(self, text='Clear all Input',foreground='white',bg='red', command=lambda: self.ClearField()) #calling ClearField function on clicking
        self.clr.place(x=250,y=470)
        self.btn_mm = tk.Button(self,text='Main Menu',bg='light green',command=lambda: controller.show_frame('MathHelp')) # button to go on home page
        self.btn_mm.pack(side='bottom')             
            
    def ClearField(self):
            self.A.delete(0, 'end')   #clearing input values present in entry widgets present in A,B,C
            self.B.delete(0, 'end') 
            self.C.delete(0, 'end')
    def quadratic(self,in1,in2,in3):
        answers=Quadratic_eqation(in1,in2,in3) # calling Quadratic_equation function from Quadratic_Equtions.py preveoisly imported in this module 
        return answers                         # this function acts as logical parameter it calculates and returns 2 strings stating equation and nature of roots and two roots of equation
    def Display(self):
        a=self.A.get()               # getting values present in entry widgets present in A,B,c
        b=self.B.get()
        c=self.C.get()
        answers= self.quadratic(a,b,c) # calling local function present in class named quadratic
        if a != '' and b != '' and c != '' and answers != 'invalid' and answers != 'a is 0':
            tkinter.messagebox._show("Results:",f'{answers[0]}\n\nRoots = {answers[1]} and {answers[2]}\n\nNature of roots: {answers[3]}')  #to show results using message box
        else:
            if answers == 'a is 0':
                tkinter.messagebox.showerror('Invalid Input','Coefficient of x^2 cannot be 0 for quadratic equations')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter Valid values')

 
class volume_area(tk.Frame):
    def __init__(self,parent,controller):
       # buttons 1 to 8 are diffrent buttons to perform sub operations on clicking any button it will display its labels and entry widgets and buttons to perform 
       # each button calls a local function present in class 
        tk.Frame.__init__(self,parent)
        self.controller=controller
        tittle=tk.Label(self,text="Volume And Surface Area \nCalculator",font=TITLE_FONT,fg='maroon')
        tittle.place(x=80,y=20)
        instruction=tk.Label(self,text="Instructions : Click on the desired 3D shape.\n To select the shape for selecting another click on [Solve Another] first.",fg='green',font=INSTRUCTION_FONT)
        instruction.place(x=50,y=130)
        self.bttn1 =tk.Button(self, text='Cube',bg='sky blue',width=20,height=2,command=lambda:self.Cube())           #calling Cube function present in class
        self.bttn1.place(x=125,y=200) 
        self.bttn2 =tk.Button(self, text='Cuboid',bg='sky blue',width=20,height=2,command=lambda:self.Cuboid())       #calling Cuboid function present in class
        self.bttn2.place(x=300,y=200) 
        self.bttn3 =tk.Button(self, text='Sphere',bg='sky blue',width=20,height=2,command=lambda:self.Sphere() )       #calling Sphere function present in class
        self.bttn3.place(x=125,y=255) 
        self.bttn4 =tk.Button(self, text='Hollow Sphere',bg='sky blue',width=20,height=2,command=lambda:self.Hollow_Sphere() )   #calling Hollow_sphere function present in class
        self.bttn4.place(x=300,y=255) 
        self.bttn5 =tk.Button(self, text='Cylinder',bg='sky blue',width=20,height=2,command=lambda:self.Cylinder() )     #calling Cylinder function present in class
        self.bttn5.place(x=125,y=310) 
        self.bttn6 =tk.Button(self, text='Hollow Cylinder',bg='sky blue',width=20,height=2,command=lambda:self.Hollow_Cylinder() )  #calling Hollow_cylinder function present in class
        self.bttn6.place(x=300,y=310) 
        self.bttn7 =tk.Button(self, text='Cone',bg='sky blue',width=20,height=2,command=lambda:self.Cone() )             #calling Cone function present in class
        self.bttn7.place(x=125,y=365) 
        self.bttn8 =tk.Button(self, text='Frustum',bg='sky blue',width=20,height=2,command=lambda:self.Frustum() )       #calling Frustum function present in class
        self.bttn8.place(x=300,y=365) 
        self.btn_mm = tk.Button(self,text='Main Menu',bg='light green',command=lambda: controller.show_frame('MathHelp'))   #to return to home page 
        self.btn_mm.pack(side='bottom') 
    def clearer1(self,e1,e2,btn,bttn,ins):  # function to remove labels and entry widgets of only one parameter of function (function require only one entry widget) 
        e1.destroy()
        e2.destroy()
        bttn.destroy()
        ins.destroy()        
        btn.destroy()
    def clearer2(self,e1,e12,e2,e22,btn,bttn,ins):  # function to remove labels and entry widgets of 2 parameter of function (function require two entry widget)
        e1.destroy()
        e2.destroy()
        e12.destroy()
        e22.destroy()        
        btn.destroy()
        bttn.destroy()        
        ins.destroy()        
    def clearer3(self,e1,e12,e2,e22,e3,e32,btn,bttn,ins): # function to remove labels and entry widgets of 3 parameter of function (function require 3 entry widget)
        e1.destroy()
        e2.destroy()
        e3.destroy()
        e12.destroy()
        e22.destroy()
        e32.destroy()
        ins.destroy()        
        bttn.destroy()                
        btn.destroy()       
    def solver_cube(self):
        value=self.e1.get()  # getting value from entry widgets and passing it in cube function as parameter 
        answers=cube(value)  # calling imported funtion cube(parameter) from Volume_surfaces.py gets two values after calling 
        if answers != 'invalid' and answers != 'negative':
            tkinter.messagebox._show("Results:",f'Total Surface Area : {answers[0]}\n\nVolume :{answers[1]}') # for displaying
        else:
            if answers == 'negative':
                tkinter.messagebox.showerror('Invalid Input','Value cannot be negative')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
    def Cube(self):                                 # gettting widgets on screen for cube 
        instruction=tk.Label(self,text="Enter the Side value and click on 'Get Details'.Click on [Solve Another ] \nbutton to calcute for other shapes.",font=INSTRUCTION_FONT)
        instruction.place(x=50,y=430)
        self.e1=Entry(self,width=20)
        self.e1.place(x=130,y=490)
        e2=tk.Label(self,text="Side : ",font=INSTRUCTION_FONT)
        e2.place(x=80,y=490)        

        self.bttn =tk.Button(self, text='Get Details',fg='white',bg='green',command=lambda: self.solver_cube())  #calling solver_cube present in class
        self.bttn.place(x=320,y=488)
        self.btn_clear_frame = tk.Button(self,text='Solve Another',fg='white',bg='orange3',command=lambda:self.clearer1(self.e1,e2,self.btn_clear_frame,self.bttn,instruction))
        self.btn_clear_frame.place(x=420,y=488)     # delets every label and widgets present in this fuction to clear the screen
    def solver_cuboid(self):
        a=self.e1.get()   # gets values present in the entry widgets and passes them to cuboid funcyion as arguments 
        b=self.e2.get()
        c=self.e3.get()
        answers=cuboid(a,b,c)   # calling imported function cuboid from Volume_surfaces.py which returns 2 things 
        if answers != 'invalid' and answers != 'negative':
            tkinter.messagebox._show("Results:",f'Total Surface Area : {answers[0]}\n\nVolume :{answers[1]}')
        else:
            if answers == 'negative':
                tkinter.messagebox.showerror('Invalid Input','Value cannot be negative')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
    def Cuboid(self):                               # gettting widgets on screen for Cuboid 
    
        instruction=tk.Label(self,text="Enter the Required values and click on 'Get Details'.Click on [Solve Another ] \nbutton to calcute for other shapes.",font=INSTRUCTION_FONT)
        instruction.place(x=30,y=430) 
       
        self.e1=Entry(self,width=10)
        self.e1.place(x=120,y=480)
        e1=tk.Label(self,text="Length :",font=INSTRUCTION_FONT)
        e1.place(x=50,y=480)

        self.e2=Entry(self,width=10)
        self.e2.place(x=290,y=480)
        e2=tk.Label(self,text="Breadth :",font=INSTRUCTION_FONT)
        e2.place(x=220,y=480)

        self.e3=Entry(self,width=10)
        self.e3.place(x=460,y=480) 
        e3=tk.Label(self,text="Height :",font=INSTRUCTION_FONT)
        e3.place(x=400,y=480)
 
        self.bttn =tk.Button(self, text='Get Details',foreground='white',bg='green',command=lambda: self.solver_cuboid()) #calling local function solver_cube
        self.bttn.place(x=160,y=530)
        self.btn_clear_frame = tk.Button(self,text='Solve Another',bg='orange3',foreground='white',command=lambda:self.clearer3(self.e1,e1,self.e2,e2,self.e3,e3,self.btn_clear_frame,self.bttn,instruction))
        self.btn_clear_frame.place(x=360,y=530)           #deletes every label entry widgets and buutons which is in this function
    def solver_sphere(self):
        value=self.e1.get()                                   # getting values present in entry widget and passes them in sphere function
        answers=sphere(value)                                 # calling imported function sphere() from Volume_surfaces.py 
        if answers != 'invalid' and answers != 'negative':
           tkinter.messagebox._show("Results:",f'Total Surface Area : {answers[0]}\n\nVolume :{answers[1]}')
        else:
            if answers == 'negative':
                tkinter.messagebox.showerror('Invalid Input','Value cannot be negative')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
    def Sphere(self):                               # gettting widgets on screen for sphere
        instruction=tk.Label(self,text="Enter the Radius value and click on 'Get Details'.Click on [Solve Another ] \nbutton to calcute for other shapes.",font=INSTRUCTION_FONT)
        instruction.place(x=50,y=430)
        self.e1=Entry(self,width=20)
        self.e1.place(x=130,y=490)
        e2=tk.Label(self,text="Radius:",font=INSTRUCTION_FONT)
        e2.place(x=80,y=490)

        self.bttn =tk.Button(self, text='Get Details',bg='green',foreground='white',command=lambda: self.solver_sphere()) #calling local function solver_sphere 
        self.bttn.place(x=320,y=488)
        self.btn_clear_frame = tk.Button(self,text='Solve Another',bg='orange3',foreground='white',command=lambda:self.clearer1(self.e1,e2,self.btn_clear_frame,self.bttn,instruction))
        self.btn_clear_frame.place(x=420,y=488)      # deletes every label entry widgets buttons in this function           
    def solver_hollow_sphere(self):       
        a=self.e1.get()    #gets values present in entry widgets and passes them in hollow_sphere function
        b=self.e2.get()
        answers=hollow_sphere(a,b)  # calling imported function hollow_sphere from volume_surface.py
        if answers != 'invalid' and answers != 'negative':
            tkinter.messagebox._show("Results:",f'Outer Surface Area : {answers[0]}\n\nInner Surface Area : {answers[1]}\n\nTotal Surface Area : {answers[2]}\n\nVolume : {answers[3]} ')
        else:
            if answers == 'negative':
                tkinter.messagebox.showerror('Invalid Input','Value cannot be negative')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
    def Hollow_Sphere(self):                        # gettting widgets on screen for Hollow_sphere 
        instruction=tk.Label(self,text="Enter the Required values and click on 'Get Details'.Click on [Solve Another ] \nbutton to calcute for other shapes.",font=INSTRUCTION_FONT)
        instruction.place(x=30,y=430)
        self.e1=Entry(self,width=15)
        self.e1.place(x=160,y=485)
        e1=tk.Label(self,text="Outer Radius :",font=INSTRUCTION_FONT)
        e1.place(x=50,y=485)

        self.e2=Entry(self,width=15)
        self.e2.place(x=410,y=485)
        e2=tk.Label(self,text="Inner Radius :",font=INSTRUCTION_FONT)
        e2.place(x=300,y=485)

        self.bttn =tk.Button(self, text='Get Details',foreground='white',bg='green',command=lambda: self.solver_hollow_sphere())  # calling local function solver_hollow_sphere
        self.bttn.place(x=160,y=530)
        self.btn_clear_frame = tk.Button(self,text='Solve Another',bg='orange3',foreground='white',command=lambda:self.clearer2(self.e1,e1,self.e2,e2,self.btn_clear_frame,self.bttn,instruction))
        self.btn_clear_frame.place(x=360,y=530)      # deletes every widget and buttons in this function from screen        
    def solver_cylinder(self):
        a=self.e1.get()
        b=self.e2.get()
        answers=cylinder(a,b)
        if answers != 'invalid' and answers != 'negative':
            tkinter.messagebox._show("Results:",f'Curved Surface Area : {answers[0]}\n\nTotal Surface Area : {answers[1]}\n\nVolume : {answers[2]}\n\n ')
        else:
            if answers == 'negative':
                tkinter.messagebox.showerror('Invalid Input','Value cannot be negative')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
    def Cylinder(self):                             # gettting widgets on screen for Cylinder 
        instruction=tk.Label(self,text="Enter the Required values and click on 'Get Details'.Click on [Solve Another ] \nbutton to calcute for other shapes.",font=INSTRUCTION_FONT)
        instruction.place(x=30,y=430)
       
        self.e1=Entry(self,width=20)
        self.e1.place(x=120,y=485)
        e1=tk.Label(self,text="Radius :",font=INSTRUCTION_FONT)
        e1.place(x=50,y=485)

        self.e2=Entry(self,width=20)
        self.e2.place(x=380,y=485)
        e2=tk.Label(self,text="Height :",font=INSTRUCTION_FONT)
        e2.place(x=300,y=485)

        self.bttn =tk.Button(self, text='Get Details',foreground='white',bg='green',command=lambda: self.solver_cylinder()) #calling local function solver_cylinder
        self.bttn.place(x=160,y=530)       
        self.btn_clear_frame = tk.Button(self,text='Solve Another',bg='orange3',foreground='white',command=lambda:self.clearer2(self.e1,e1,self.e2,e2,self.btn_clear_frame,self.bttn,instruction))
        self.btn_clear_frame.place(x=360,y=530)   # deletes every widget and buttons in this function from screen      
    def solver_hollow_cylinder(self):
        a=self.e1.get()          # getting values from entry widgets and passing them as arguments in hollow_cylinder function
        b=self.e2.get() 
        c=self.e3.get()
        answers=hollow_cylinder(a,b,c)   # calling imported function hollow_cylinder from volume_surfaces.py
        if answers != 'invalid' and answers != 'negative':
            tkinter.messagebox._show("Results:",f'Outer Curved Surface Area : {answers[0]}\n\nInner Curved Surface Area : {answers[1]}\n\nTotal Surface Area : {answers[2]}\n\nVolume : {answers[3]} ')
        else:
            if answers == 'negative':
                tkinter.messagebox.showerror('Invalid Input','Value cannot be negative')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
    def Hollow_Cylinder(self):                      # gettting widgets on screen for Hollow_cylinder 
        instruction=tk.Label(self,text="Enter the Required values and click on 'Get Details'.Click on [Solve Another ] \nbutton to calcute for other shapes.",font=INSTRUCTION_FONT)
        instruction.place(x=30,y=430)

        self.e1=Entry(self,width=8)
        self.e1.place(x=150,y=485)
        e1=tk.Label(self,text="Inner Radius:",font=INSTRUCTION_FONT)
        e1.place(x=50,y=485)

        self.e2=Entry(self,width=8)
        self.e2.place(x=330,y=485)
        e2=tk.Label(self,text="Outer Radius:",font=INSTRUCTION_FONT)
        e2.place(x=220,y=485)

        self.e3=Entry(self,width=8)
        self.e3.place(x=470,y=485) 
        e3=tk.Label(self,text="Height:",font=INSTRUCTION_FONT)
        e3.place(x=410,y=485)

        self.bttn =tk.Button(self, text='Get Details',foreground='white',bg='green',command=lambda: self.solver_hollow_cylinder()) # calling local function solver_hollow_cylinder
        self.bttn.place(x=160,y=530)
        self.btn_clear_frame = tk.Button(self,text='Solve Another',bg='orange3',foreground='white',command=lambda:self.clearer3(self.e1,e1,self.e2,e2,self.e3,e3,self.btn_clear_frame,self.bttn,instruction))
        self.btn_clear_frame.place(x=360,y=530)    # deletes every widget and buttons in this function from screen 
    def solver_cone(self):
        a=self.e1.get()          # getting values from entry widgets and passing them as arguments in cone function
        b=self.e2.get() 
        answers=cone(a,b)         # calling imported function cone from volume_surfaces.py
        if answers != 'invalid' and answers != 'negative':
            tkinter.messagebox._show("Results:",f'Total Surface Area : {answers[0]}\n\nVolume :{answers[1]}')
        else:
            if answers == 'negative':
                tkinter.messagebox.showerror('Invalid Input','Value cannot be negative')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
    def Cone(self):                                 # gettting widgets on screen for Cone 
        instruction=tk.Label(self,text="Enter the Required values and click on 'Get Details'.Click on [Solve Another ] \nbutton to calcute for other shapes.",font=INSTRUCTION_FONT)
        instruction.place(x=30,y=430)

        self.e1=Entry(self,width=20)
        self.e1.place(x=120,y=485)
        e1=tk.Label(self,text="Height :",font=INSTRUCTION_FONT)
        e1.place(x=50,y=485)

        self.e2=Entry(self,width=20)
        self.e2.place(x=380,y=485)
        e2=tk.Label(self,text="Radius :",font=INSTRUCTION_FONT)
        e2.place(x=300,y=485)
        
        self.bttn =tk.Button(self, text='Get Details',foreground='white',bg='green',command=lambda: self.solver_cone()) # calling local function solver_cone
        self.bttn.place(x=160,y=530)
        self.btn_clear_frame = tk.Button(self,text='Solve Another',bg='orange3',foreground='white',command=lambda:self.clearer2(self.e1,e1,self.e2,e2,self.btn_clear_frame,self.bttn,instruction))
        self.btn_clear_frame.place(x=360,y=530)        # deletes every widget and buttons in this function from screen 
    def solver_frustum(self):
        a=self.e1.get()         # getting values from entry widgets and passing them as arguments in frustum function
        b=self.e2.get()
        c=self.e3.get()
        answers=frustum(a,b,c)  # calling imported function frustum from volume_surfaces.py
        if answers != 'invalid' and answers != 'negative':
            tkinter.messagebox._show("Results:",f'Lateral Surface Area : {answers[0]}\n\nTotal Surface Area : {answers[1]}\n\nVolume : {answers[2]} ')
        else:
            if answers == 'negative':
                tkinter.messagebox.showerror('Invalid Input','Value cannot be negative')
            else:
                tkinter.messagebox.showerror('Invalid Input','Enter valid input in all fields')
    def Frustum(self):                              # gettting widgets on screen for Frustum 
        instruction=tk.Label(self,text="Enter the Required values and click on 'Get Details'.Click on [Solve Another ] \nbutton to calcute for other shapes.",font=INSTRUCTION_FONT)
        instruction.place(x=30,y=430)
       
        self.e1=Entry(self,width=8)
        self.e1.place(x=110,y=485)
        e1=tk.Label(self,text="Height:",font=INSTRUCTION_FONT)
        e1.place(x=50,y=485)

        self.e2=Entry(self,width=8)
        self.e2.place(x=300,y=485)
        e2=tk.Label(self,text="Top Radius:",font=INSTRUCTION_FONT)
        e2.place(x=200,y=485)

        self.e3=Entry(self,width=8)
        self.e3.place(x=480,y=485) 
        e3=tk.Label(self,text="Base Radius:",font=INSTRUCTION_FONT)
        e3.place(x=380,y=485)

        self.bttn =tk.Button(self, text='Get Details',foreground='white',bg='green',command=lambda: self.solver_frustum())   # calling local function solver_frustum
        self.bttn.place(x=160,y=530)
        self.btn_clear_frame = tk.Button(self,text='Solve Another',bg='orange3',foreground='white',command=lambda:self.clearer3(self.e1,e1,self.e2,e2,self.e3,e3,self.btn_clear_frame,self.bttn,instruction))
        self.btn_clear_frame.place(x=360,y=530)      # deletes every widget and buttons in this function from screen 
       
# classes and functions introduced till here are from Sourav.
# modification of GUI in series module,AP sub module and GP sub module made by sourav

if __name__=='__main__':
    root = App()
    root.mainloop()