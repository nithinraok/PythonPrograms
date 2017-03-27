from Tkinter import *

window=Tk()
def convertKgs():
    kg=float(kgs.get());
    g=kg*1000;
    p=kg*2.20462;
    o=kg*35.274;
    grams.delete('1.0',END)
    pounds.delete('1.0',END)
    ounces.delete('1.0',END)
    grams.insert(END,g);
    pounds.insert(END,p);
    ounces.insert(END,o);
    
    
l1=Label(window,text='Kg');
l1.grid(row=0,column=0);

kgs=StringVar();
e1=Entry(window,textvariable=kgs);
e1.grid(row=0,column=1);

b1=Button(window,text='Convert',command=convertKgs)
b1.grid(row=0,column=2);

grams=Text(window,height=1,width=20)
grams.grid(row=1,column=0)

pounds=Text(window,height=1,width=20)
pounds.grid(row=1,column=1)

ounces=Text(window,height=1,width=20)
ounces.grid(row=1,column=2)

window.mainloop()
