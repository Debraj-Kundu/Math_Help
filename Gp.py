#a = int(input("Please Enter First Number of an G.P Series: : "))
#n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
#r = int(input("Please Enter the Common Ratio : "))

def GP(prb):
    a = int(prb.split(',')[0])
    n = int(prb.split(',')[1])
    r = int(prb.split(',')[2])
    total = 0
    value = a
    ans = list()
    ans.append(str(value))
    for i in range(n):
        total = total + value
        value = value * r
        ans.append(str(value))
    print(total)
    res = str(total)+','+' '.join(ans)
    return res
    
#print("\nThe Sum of Geometric Progression Series = " , total)
#print(GP('1, 6, 2'))
