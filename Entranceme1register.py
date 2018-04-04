# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:50:45 2018

@author: TIm
"""

#from tkinter import ttk
import tkinter as tkk
aa = ['User Name', 'Password'
, 'Institution', 'Major']
sto = []#student account

"""Add student here"""
def fe(ents):
    f = open('StudentDatabase', 'r+')#studtabasestu is plugin and StudentDatabase is database
    f.seek(0, 2)#go to very end of database
    f.write('Student account: \n')
    for ent in ents:
        a = ent[0]
        text = ent[1].get()
        if len(sto) < len(aa):
            sto.append(text)
        else :
            sto.clear()
            sto.append(text)
        print('%s: "%s" \n account: %s' % (a, text, sto))
    
    for sti in sto[:]:
        f.seek(0, 2)
        f.write(sti + '\n')
    f.write(':end student account.\n \n')
    print('Student registered!')
    f.close


def make1(rt, aa):
    ents = []
    for a in aa:
        row = tkk.Frame(rt)
        lbl = tkk.Label(row, background="#fff", width=15, text=a, anchor='w')
        ent = tkk.Entry(row, highlightbackground="SteelBlue2", 
                        highlightcolor="SteelBlue2", highlightthickness=1)
        row.pack(side=tkk.TOP, fill=tkk.X, padx=5, pady=5)
        lbl.pack(side=tkk.LEFT)
        ent.pack(side=tkk.RIGHT, expand=tkk.YES, fill=tkk.X)
        ents.append((a, ent))
    return ents

if __name__ == '__main__':
    tko = tkk.Tk()    
    #change background here.
    tko.configure(background="#fff")
    tko.title("EntranceMe/RegisterMe")
    #add wigits here.
    nts = make1(tko, aa)
    tko.bind('<Return>', (lambda event, e=nts: fe(e)))
    b1 = tkk.Button(tko, bg="LightBlue2", relief="flat",  
                    text='RegisterMe', command=(lambda e=nts: fe(e)))
    b1.pack(side=tkk.LEFT, padx=5, pady=5)
    tko.mainloop()
    