def AP(prb):
    a = int(prb.split(',')[0])
    n = int(prb.split(',')[1])
    d = int(prb.split(',')[2])
    total = (n * (2 * a + (n - 1) * d)) / 2
    tn = a + (n - 1) * d
    first_element = a
    ans = list()
    ans.append(str(first_element))
    #print("\nLast Term of Arithmetic Progression Series = " , tn)
    #print("The Sum of Arithmetic Progression Series : ")
    while(first_element <= tn):
        #if(first_element != tn):
            #print("%d + " %first_element, end = " ")
        #else:
            #print("%d = %d" %(first_element, total))
        first_element = first_element+d
        ans.append(str(first_element))
    res =  str(tn)+','+str(total)+','+' '.join(ans)
    return res

#print(AP('7,6,3'))
