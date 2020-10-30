#Logic by Siddhant Singh
#Debugging, errorhandling and parsing by Debraj Kundu

def GP(prb):
    a = prb.split(',')[0]
    n = prb.split(',')[1]
    r = prb.split(',')[2]
    res = 'invalid'
    if not a.lstrip('-').isdigit() or not n.lstrip('-').isdigit() or not r.lstrip('-').isdigit():
        return res
    a = int(a)
    n = int(n)
    r = int(r)

    if n <=0 :
        return 'invalid n'
    else:
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
