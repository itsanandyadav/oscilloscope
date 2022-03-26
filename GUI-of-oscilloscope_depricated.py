## just GUI of the oscilloscope
from tkinter import *

root = Tk()
root.geometry("1000x600+100+50")
root.title('This is my root window')
##root.state('zoomed')
#### Frame for display
display = Label(root, text="DISPLAY", font='Helvetica 18 bold')
display.place(relx=0.2,rely=0, anchor="nw",relwidth=0.3,relheight=0.1)

frame = Frame(root, borderwidth=1,bg="#0DBDAB",relief=SUNKEN,bd=10)
frame.place(relx=1.0/3,rely=0.5, anchor="center", relwidth=0.60,relheight=0.8)
#### Frame for buttons----------------------------------------
frame1=Frame(root,bg="#CDD6D8",highlightbackground="#A4A6A7", highlightthickness=10,bd=10,relief=RAISED)
frame1.place(relx=5.0/6,rely=0.5,anchor="center",relwidth=0.3,relheight=0.8)
#### Frame for axis buttons
frame2=Frame(frame1,bg="#87A4B3",bd=5)
frame2.pack(side=TOP,fill=BOTH)
frame3=Frame(frame1,bg="#5FA8A8",bd=10)
frame3.pack(side=TOP,fill=BOTH)
frame4=Frame(frame1,bg="#87A4B3",bd=10)
frame4.pack(side=TOP,fill=BOTH)


#### Buttons 5FA8A8
##-----------------------------------------------------

##Grid.rowconfigure(frame2,1, weight=1)
Grid.columnconfigure(frame2,0, weight=1)
Grid.columnconfigure(frame2,1, weight=1)
Grid.columnconfigure(frame2,2, weight=1)
Grid.columnconfigure(frame2,3, weight=1)

label_y = Label(frame2, text="Unit Y")
label_y.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=5,pady=0)

i_y = Button(frame2, text="+",font='Helvetica 14 bold',relief=RAISED,bd=5)
i_y.grid(row=1,column=0,sticky="nsew",padx=(5,0),pady=(1))
d_y = Button(frame2, text="-",font='Helvetica 14 bold',relief=RAISED,bd=5)
d_y.grid(row=1,column=1,sticky="nsew",padx=(0,5),pady=(1))

label_t = Label(frame2, text="Unit T")
label_t.grid(row=0,column=2,columnspan=2,sticky="ew",padx=5,pady=0)

i_t = Button(frame2, text="+",font='Helvetica 14 bold',relief=RAISED,bd=5)
i_t.grid(row=1,column=2,sticky="ew",padx=(5,0),pady=(1))
d_t = Button(frame2, text="-",font='Helvetica 14 bold',relief=RAISED,bd=5)  
d_t.grid(row=1,column=3,sticky="ew",padx=(0,5),pady=(1))

e1 = Entry(frame2)
e1.grid(row=2,columnspan=4,sticky="ew",padx=(0,1),pady=1)
stop = Button(frame2, text="STOP",font='Helvetica 12 bold',relief=RAISED,bd=5)  
stop.grid(row=3,column=0,columnspan=2,sticky="ew")
save = Button(frame2, text="SAVE",font='Helvetica 12 bold',relief=RAISED,bd=5)  
save.grid(row=3,column=2,columnspan=2,sticky="ew")
##-----------------------------------------------------

Grid.columnconfigure(frame4,0, weight=1)
Grid.columnconfigure(frame4,1, weight=1)
Grid.columnconfigure(frame4,2, weight=1)
Grid.columnconfigure(frame4,3, weight=1)

offset_lbl2 = Label(frame4, text="Y axis Offset",font='Helvetica 11 bold')
offset_lbl2.grid(row=0,column=1,columnspan=2,sticky="ew",padx=5,pady=1)
offset_lbl3 = Label(frame4, text="Unit T")
offset_lbl3.grid(row=1,column=1,columnspan=2,sticky="ew",padx=5,pady=0)
i_offset = Button(frame4, text="+",font='Helvetica 14 bold',relief=RAISED,bd=5)
i_offset.grid(row=2,column=1,sticky="ew",padx=(5,0),pady=(1,5))
d_offset = Button(frame4, text="-",font='Helvetica 14 bold',relief=RAISED,bd=5)  
d_offset.grid(row=2,column=2,sticky="ew",padx=(0,5),pady=(1,5))

###-------------------------------------------------------------------
Grid.columnconfigure(frame3,0, weight=1)
Grid.columnconfigure(frame3,1, weight=1)
Grid.columnconfigure(frame3,2, weight=1)
##Grid.columnconfigure(frame3,3, weight=1)

#### Numerical buttons
name=["one","two","three","four","five","six","seven","eight","nine","star","zero","hash"]
textvar=["1","2","3","4","5","6","7","8","9","*","0","#"]
j=0
for i in range(12):
    name[1]=Button(frame3,text=textvar[i],font='Helvetica 11 bold',relief=RAISED,bd=5)
    name[1].grid(row=int(i/3),column=j,sticky="ew",padx=5,pady=5)
    if j>=2:
        j=0
    else:
        j=j+1
##--------------------------------

mainloop()
