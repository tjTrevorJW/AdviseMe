# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:50:45 2018

@author: TIm
"""

#from tkinter import ttk
import tkinter as tkk
aa = ['User Name', 'Password']
sto = []#student account

"""Find student here."""
def fi(ents):
    f = open('StudentDatabase', 'r+')#studtabasestu is plugin and StudentDatabase is database
    f.seek(0, 0)#go to very begining of database
    for ent in ents:
        a = ent[0]
        text = ent[1].get()
        if len(sto) < len(aa):
            sto.append(text)
        else :
            sto.clear()
            sto.append(text)
        print('%s: "%s" \n account: %s' % (a, text, sto))
    print('%s:%s' % (sto[0], sto[1]))
    
    sf = 0
    un = 0
    stostr0 = sto[0] + "\n"
    stostr1 = sto[1] + "\n"
    for line in f:
        print(line, end = '')
        if line == stostr0:
            un = 1
        if line == stostr1:
            if un == 1 :
                sf = 1
        
    if sf == 0:
        print('Student not found.')
    elif sf == 1:
        print('Student found!')
        """insert entrance to AdviseMe system here"""
    f.close


def make(rt, aa):
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
    nts = make(tko, aa)
    tko.bind('<Return>', (lambda event, e=nts: fi(e)))
    b1 = tkk.Button(tko, bg="LightBlue2", relief="flat",  
                    text='Sign In', command=(lambda e=nts: fi(e)))
    b1.pack(side=tkk.LEFT, padx=5, pady=5)
    tko.mainloop()
    
''' need to exit at entry'''