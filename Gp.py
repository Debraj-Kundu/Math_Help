from tkinter import *
import tkinter as tk
import tkinter.messagebox

def GP(prb):
    a = prb.split(',')[0]
    n = prb.split(',')[1]
    r = prb.split(',')[2]
    res = 'invalid'
    if not a.isdigit() or not n.isdigit() or not r.isdigit():
        return res
    a = int(a)
    n = int(n)
    r = int(r)

    if r == 0 or a == 0 or r < a:
        return res
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
