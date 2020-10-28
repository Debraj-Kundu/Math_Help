

def AP(prb):
    a = prb.split(',')[0]
    n = prb.split(',')[1]
    d = prb.split(',')[2]
    res = 'invalid'
    if not a.isdigit() or not n.isdigit() or not d.isdigit():
        return res
    a = int(a)
    n = int(n)
    d = int(d)
    if d < a:
        return res
    total = (n * (2 * a + (n - 1) * d)) / 2
    tn = a + (n - 1) * d
    first_element = a
    ans = list()
    ans.append(str(first_element))

    while(first_element <= tn):

        first_element = first_element+d
        ans.append(str(first_element))
    res =  str(tn)+','+str(total)+','+' '.join(ans)
    return res


