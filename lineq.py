from sympy import symbols, Eq, solve


def Problemr(prb):
        x, y = symbols('x y')
        inp = prb.split(',')
        #Storing equations one and two
        string_1 = inp[0]
        string_2 = inp[1]
        #Storing LHS of equation
        lhs = string_1.split('=')[0]
        lhs2 = string_2.split('=')[0]

        #Inserting multiplication operator b/w coefficient and variable
        lhs = lhs.split('x')[0]+'*'+'x'+lhs.split('x')[1].split('y')[0]+'*'+'y'
        lhs2 = lhs2.split('x')[0]+'*'+'x'+lhs2.split('x')[1].split('y')[0]+'*'+'y'

        #Passing RHS and LHS as argument
        eq1 = Eq(eval(lhs), int(string_1.split('=')[-1]))
        eq2 = Eq(eval(lhs2), int(string_2.split('=')[-1]))
        #Solving
        solve((eq1,eq2), (x, y))
        sol_dict = solve((eq1,eq2), (x, y))

        return (sol_dict[x], sol_dict[y])
