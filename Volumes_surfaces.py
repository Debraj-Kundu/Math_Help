import math

#Logic and parsing by Sourav
#Debuging and errorhandling by Debraj Kundu
def cube(side):
    if not side.lstrip('-').isdigit() or side == '':
        return 'invalid'
    side=float(side)
    if side < 0:
        return 'negative'
    tsa=6*side                        #tsa=Total surface area
    volume=pow(side,3)
    return(tsa,volume)

def cuboid(l,b,h):
    if not l.lstrip('-').isdigit() or not b.lstrip('-').isdigit() or not h.lstrip('-').isdigit() or l == '' or b == '' or h == '':
        return 'invalid'
    l=float(l)                        #l=Length
    b=float(b)                        #b=Breadth
    h=float(h)                        #h=Height
    if l < 0 or b < 0 or h <0:
        return 'negative'
    tsa=2*(l*b+b*h+h*l)               #tsa=Total surface area
    volume=l*b*h
    return(tsa,volume)

def sphere(r):
    if not r.lstrip('-').isdigit() or r == '':
        return 'invalid'
    r=float(r)     #r=radius  
    if r < 0:
        return 'negative' 
    volume=4*math.pi*pow(r,3)/3
    tsa=4*math.pi*pow(r,2)
    tsa=format(tsa,".2f")             #tsa=Total surface area
    volume=format(volume,".2f")
    return(tsa,volume)

def hollow_sphere(Or,Ir):
    if not Or.lstrip('-').isdigit() or not Ir.lstrip('-').isdigit() or Or == '' or Ir == '':
        return 'invalid'
    Or=float(Or)                      #Or= Outer radius
    Ir=float(Ir)                      #Ir= Inner radius
    if Or < 0 or Ir < 0:
        return 'negative' 
    osa=4*math.pi*pow(Or,2)           #osa = Outer surface area
    isa=4*math.pi*pow(Ir,2)           #isa = Inner surface area
    tsa=osa+isa
    osa=format(osa,".2f") 
    isa=format(isa,".2f") 
    tsa=format(tsa,".2f")             #tsa=Total surface area
    volume=4*math.pi*pow(Or-Ir,3)/3
    volume=format(volume,".2f")       #format function is used for converting the value to 2 decimal points in each function format functionallity is same
    return(osa,isa,tsa,volume)

def cylinder(r,h):
    if not r.lstrip('-').isdigit() or not h.lstrip('-').isdigit() or r == '' or h == '':
        return 'invalid'
    r=float(r)                        # r= radius
    h=float(h)                        # h= Height
    if r < 0 or h < 0:
        return 'negative'
    csa=2*math.pi*r*h                 # csa =Curved surface area
    bsa=math.pi*pow(r,2)*2            # bsa = area of base 
    tsa=csa+bsa                       #tsa=Total surface area
    volume=math.pi*pow(r,2)*h
    tsa=format(tsa,".2f")
    csa=format(csa,".2f")
    volume=format(volume,".2f")
    return(csa,tsa,volume)

def hollow_cylinder(Ir,Or,h):
    if not Ir.lstrip('-').isdigit() or not h.lstrip('-').isdigit() or not Or.lstrip('-').isdigit() or Ir == '' or h == '' or Or == '':
        return 'invalid'
    Ir=float(Ir)                     # Ir= Inner radius
    Or=float(Or)                     # Or = Outer radius
    h=float(h)                       # h = hieght
    if Ir < 0 or h < 0 or Or < 0:
        return 'negative'
    Ocsa=2*math.pi*Or*h              # Ocsa = outer surface area
    Icsa=2*math.pi*Ir*h              # Icsa = Inner surface area
    Rsa=math.pi*pow((Or-Ir),2)*2     # Rsa = ring surface area formed on top and bottom
    tsa=Ocsa+Icsa+Rsa                # tsa = Total surface area
    volume=math.pi*h(pow(Or,2)-pow(Ir,2))
    return(Ocsa,Icsa,tsa,volume)

def cone(h,r):
    if not h.lstrip('-').isdigit() or not r.lstrip('-').isdigit() or h == '' or r == '':
        return 'invalid'
    h=float(h)                       # h= hieght              
    r=float(r)                       # r= radius
    if h < 0 or r < 0:
        return 'negative'
    tsa=math.pi*r*(r+math.sqrt(pow(h,2)+pow(r,2)))  #tsa=Total surface area
    volume=(math.pi*pow(r,2)*h)/3
    return(tsa,volume)

def frustum(h,r,R):
    if not h.lstrip('-').isdigit() or  not r.lstrip('-').isdigit() or not R.lstrip('-').isdigit() or h == '' or R == '':
        return 'invalid'
    h=float(h)                       # h= height
    r=float(r)                       # r= top radius of frustum 
    R=float(R)                       # R = base radius of Frustum
    if h < 0 or r < 0 or R < 0:
        return 'negative'
    l=math.sqrt(pow(h,2)+pow((R-r),2))  # l= slant height of frustum
    lsa=math.pi*l*(R+r)              # lsa = curved surface area of frustum
    rsa=math.pi*pow(r,2)             # rsa = top radius area
    Rsa=math.pi*pow(R,2)             # Rsa = Base radius area
    tsa=lsa+rsa+Rsa                  # tsa = Total surface area
    volume=(math.pi*h*(pow(R,2)+pow(r,2)+R*r))/3
    return(lsa,tsa,volume)             
