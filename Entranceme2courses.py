# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:50:45 2018

@author: TIm
"""

import tkinter as tkk
"""Add course here"""
aa = ['Course']
sto = []
def fe(ents):
    f = open('CourseDatabase', 'r+')#studtabasecor is plugin and CourseDatabase is database
    for ent in ents:
        a = ent[0]
        text = ent[1].get()
        if len(sto) < len(aa):
            sto.append(text)
        else :
            sto.clear()
            sto.append(text)
        print('%s: "%s" courses: %s' % (a, text, sto))
    
    for sti in sto[:]:
        f.seek(0, 2)#go to very end of database
        f.write(sti + '\n')
    f.close
"""Find course here."""
def fi(ents):
    f = open('CourseDatabase', 'r+')#studtabasecor is plugin and CourseDatabase is database
    for ent in ents:
        a = ent[0]
        text = ent[1].get()
        if len(sto) < len(aa):
            sto.append(text)
        else :
            sto.clear()
            sto.append(text)
        print('%s: "%s" courses: %s' % (a, text, sto))
    print(':%s' % (sto[0]))
    
    cf = 0
    stostr = sto[0] + "\n"
    for line in f:
        print(line, end = '')
        if line == stostr:
            cf = 1
    
    if cf == 0:
        print('Course not found.')
    elif cf == 1:
        print('Course found!')
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
    tko.title("Enter Completed Courses")
    #add wigits here.
    nts = make(tko, aa)
    tko.bind('<Return>', (lambda event, e=nts: fe(e)))
    b1 = tkk.Button(tko, bg="LightBlue2", relief="flat",  
                    text='addCourse', command=(lambda e=nts: fe(e)))
    b1.pack(side=tkk.LEFT, padx=5, pady=5)
    b2 = tkk.Button(tko, bg="LightBlue2", relief="flat",  
                    text='findCourse', command=(lambda e=nts: fi(e)))
    b2.pack(side=tkk.LEFT, padx=5, pady=5)
    tko.mainloop()
    
