### Oscilloscope

import serial   ## for serial communication with Arduino
from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.ticker as plticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np ## for mathematical operations
import time
###---------------------------------------------------------
### this function is just to kill the program after closing the window
def quit_me():
    print('Quit')
    root.quit()
    root.destroy()
###---------------------------------------------------------
root = Tk()
root.protocol("WM_DELETE_WINDOW",quit_me)
root.geometry("1000x600+100+50")                ## first appearance of the window
root.title('Oscilloscope By Sarvesh')
display = Label(root, text="DISPLAY", font='Helvetica 18 bold')
display.place(relx=0.2,rely=0, anchor="nw",relwidth=0.3,relheight=0.1)
##root.state('zoomed')                          ## uncommet it if you want to launch in full screen mode
frame = Frame(root, borderwidth=1,bg="#0DBDAB",relief=SUNKEN,bd=10) ## frame for display of the oscilloscope
frame.place(relx=1.0/3,rely=0.5, anchor="center", relwidth=0.60,relheight=0.8) 

#### Frame for buttons-----------------------------------
frame1=Frame(root,bg="#CDD6D8",highlightbackground="#A4A6A7", highlightthickness=10,bd=10,relief=RAISED)
frame1.place(relx=5.0/6,rely=0.5,anchor="center",relwidth=0.3,relheight=0.8)
#### Frame for function buttons
frame2=Frame(frame1,bg="#87A4B3",bd=5)
frame2.pack(side=TOP,fill=BOTH)
### frame for number plate
frame3=Frame(frame1,bg="#5FA8A8",bd=10)
frame3.pack(side=TOP,fill=BOTH)
frame4=Frame(frame1,bg="#87A4B3",bd=10)
frame4.pack(side=TOP,fill=BOTH)

# Arduino serial port and baudrate
ser = serial.Serial('com3', 115200, timeout=5)

xar = [0] ## array to store time axis values
yar = [0] ## array to store y axis values

yy=1      ## limit of y axis, by default 1
tt=50     ## limit of time axis
val=0     ## variable to store value from arduino
ft=0      ## variable for offset on y axis

###-----Start of animation widget------------------------
style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylim(-yy+ft, yy+ft)
line, = ax1.plot(xar, yar, 'r')
ax1.grid(b=True,which='both',axis='both')


def animate(i):
    global val
    ax1.set_xlim(left=max(0,i-tt-1), right=i+1) ## set time axis limit
    ser.flushInput()
    msg=ser.readline()
    cc=msg[0:len(msg)-2].decode("utf-8")
    
    if not cc:               ## if unable to read from arduino
        val=yar[-1]          ## use previous value
    else:
        val=(int(cc)/1024.0)*5
##        val=val-2.5        ## uncomment this line if you adding offset of 2.5 V externally
    ## now append the value into array
    yar.append(round(val,2)) ## roundig off up to two decimal points
    xar.append(i)
    line.set_data(xar,yar)   ## add line to previous plot
    return line,             ## not needed just written for formality

plotcanvas = FigureCanvasTkAgg(fig, frame) 
plotcanvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH,expand=True)
ani = animation.FuncAnimation(fig, animate, interval=100, blit=False)
## interval is time in milisecond after which it will add new line to plot

###--------------G U I STARTS HERE -----------------------------------
##---------------------Axis Buttons ------------------------------####
Grid.columnconfigure(frame2,0, weight=1)
Grid.columnconfigure(frame2,1, weight=1)
Grid.columnconfigure(frame2,2, weight=1)
Grid.columnconfigure(frame2,3, weight=1)

  ## button to change y axis 
def y_limit(button_id):
    global yy
    if button_id==2:            ##  if + button is pressed
        if yy<=0.5:             ## if limit is less than 0.5 V
            yy=round((yy+0.1),2)## increment by just 0.1 V
        else:
            yy=(yy+0.5)         ## else increment by 0.5 V
    elif button_id==1:          ## if  - button is pressed
        if yy<=0.5:             ## if limit is less than 0.5 V
            yy=round((yy-0.1),2)## decrement by just0.1
        else:
            yy=(yy-0.5)         ## decrement by just 0.5 V
    ax1.set_ylim(-yy+ft,yy+ft)  ## y axis limit 
    label_y.configure(text="Y length:"+str(2*yy)) ## show limit values in label

    ##  just to set grid axis no need to understand
    if yy<=1:
        ax1.grid(b=True,axis='both',which='major',alpha=1)
        ax1.grid(b=True,axis='both',which='minor', alpha=0.5)
        loc = plticker.MultipleLocator(base=0.1)
        ax1.yaxis.set_major_locator(loc)
    else:
        ax1.grid(which='minor',axis='both', alpha=0.5)
        ax1.grid(which='major',axis='both', alpha=1)
        loc_M =plticker.MultipleLocator(base=1.0)
        loc_m =plticker.MultipleLocator(base=0.2)
        ax1.yaxis.set_major_locator(loc_M)
        ax1.yaxis.set_minor_locator(loc_m)
        
    ## button to change y axis 
def t_limit(button_id):
    global tt
    if button_id==2:        ##  if + button is pressed
        if tt<10:
            tt=round((tt+1))
        else:
            tt=(tt+5)
    elif button_id==1:      ##  if - button is pressed
        if tt<=5:           ## if time limit is less than 5
            tt=tt           ## do not change it further
        else:
            tt=(tt-5)
    label_t.configure(text="Time length:"+str(tt)+"s")

 ## label to show y axis limit
label_y = Label(frame2,text="Y Limit:"+str(2*yy))
label_y.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=5,pady=0)

 ## button to change Y axis parameters
i_y = Button(frame2, text="+",font='Helvetica 14 bold',relief=RAISED,bd=5, command=lambda:y_limit(2))       ## increment button
i_y.grid(row=1,column=0,sticky="nsew",padx=(5,0),pady=(1,5))    
d_y = Button(frame2, text="-",font='Helvetica 14 bold',relief=RAISED,bd=5, command=lambda:y_limit(1))       ## decrement button
d_y.grid(row=1,column=1,sticky="nsew",padx=(0,5),pady=(1,5))

 ## label to show y axis limit
label_t = Label(frame2,text="Time length:"+str(tt)+"s")
label_t.grid(row=0,column=2,columnspan=2,sticky="ew",padx=5,pady=0)

 ## button to change Y axis parameters
i_t = Button(frame2, text="+",font='Helvetica 14 bold',relief=RAISED,bd=5,command=lambda:t_limit(2))        ## decrement button
i_t.grid(row=1,column=2,sticky="ew",padx=(5,0),pady=(1,5))
d_t = Button(frame2, text="-",font='Helvetica 14 bold',relief=RAISED,bd=5,command=lambda:t_limit(1))        ## decrement button
d_t.grid(row=1,column=3,sticky="ew",padx=(0,5),pady=(1,5))

###------------------------------------------------------
###--------pause and save functions----------------------
## function to pause plots
## if runnig it will show stop, if paused it will show run
def stop_function():
    if(stop1["text"]=="STOP"):
        stop1.configure(text="RUN")
        ani.event_source.stop()
    else:
        stop1.configure(text="STOP")
        ani.event_source.start()
## function to save plots in .png format
def save_image():
    plt.savefig(e1.get()+".png")
    return None

e1 = Entry(frame2) ## for entry of the name of plot to be saved
e1.grid(row=2,columnspan=4,sticky="ew",padx=(0,1),pady=1) 
stop1 = Button(frame2,text="STOP",font='Helvetica 10 bold',relief=RAISED,bd=5,command=lambda:stop_function())  
stop1.grid(row=3,column=0,columnspan=2,sticky="ew")
save1 = Button(frame2, text="SAVE",font='Helvetica 10 bold',relief=RAISED,bd=5,command=lambda:save_image())  
save1.grid(row=3,column=2,columnspan=2,sticky="ew")
##----------------- Functions end---------------------------
## ---------------Number pad--------------------------------
Grid.columnconfigure(frame3,0, weight=1)
Grid.columnconfigure(frame3,1, weight=1)
Grid.columnconfigure(frame3,2, weight=1)

 ## Numerical buttons under 
name=["one","two","three","four","five","six","seven","eight","nine","star","zero","hash"]
textvar=["1","2","3","4","5","6","7","8","9","*","0","#"]
j=0
for i in range(12):
    name[1]=Button(frame3,text=textvar[i],font='Helvetica 11 bold',relief=RAISED,bd=5,)
    name[1].grid(row=int(i/3),column=j,sticky="ew",padx=5,pady=5)
    if j>=2:
        j=0
    else:
        j=j+1
###---------------Number pad ends---------------------------
###---------------------------------------------------------
## Offset button
     ## this part is explained in y limit function
def offset(button_id):
    global ft,yy
    if button_id==2:
        if ft<0.5:
            ft=round((ft+0.1),2)
        else:
            ft=(ft+0.5)
    elif button_id==1:
        if ft<=0.5:
            ft=round((ft-0.1),2)
        else:
            ft=(ft-0.5)
    ax1.set_ylim(-yy+ft,yy+ft)
    offset_lbl3.configure(text="Offset:"+str(ft)+"V")

Grid.columnconfigure(frame4,0, weight=1)
Grid.columnconfigure(frame4,1, weight=1)
Grid.columnconfigure(frame4,2, weight=1)
Grid.columnconfigure(frame4,3, weight=1)

offset_lbl2 = Label(frame4, text="Y axis Offset",font='Helvetica 11 bold')
offset_lbl2.grid(row=0,column=1,columnspan=2,sticky="ew",padx=5,pady=1)
offset_lbl3 = Label(frame4, text="Offset:"+str(ft)+"V")
offset_lbl3.grid(row=1,column=1,columnspan=2,sticky="ew",padx=5,pady=0)
i_offset = Button(frame4, text="+",font='Helvetica 14 bold',relief=RAISED,bd=5,command=lambda:offset(2))
i_offset.grid(row=2,column=1,sticky="ew",padx=(5,0),pady=(1,5))
d_offset = Button(frame4, text="-",font='Helvetica 14 bold',relief=RAISED,bd=5,command=lambda:offset(1))  
d_offset.grid(row=2,column=2,sticky="ew",padx=(0,5),pady=(1,5))

###-------Button ends---------------------------------------
root.mainloop()

