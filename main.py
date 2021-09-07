from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
root = Tk()
root.title('algorithm vislualiser ')
root.maxsize(900,600)
root.config(bg='black')

selected_alg=StringVar()
data =[]





def drawdata(data,colorArray):
    canvas.delete("all")
    c_height =300
    c_width=600
    x_wid=c_width/(len(data)+1)
    offset=30
    spacing =10
    normalizedata=[i/max(data) for i in data]
    for i , height in enumerate(normalizedata):
        x0=i*x_wid+offset+spacing
        y0=c_height-height*250
        x1=(1+i)*x_wid+offset
        y1=c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
    root.update_idletasks()

def Generate ():

    global data

    minval=int(minEntry.get())
    maxval=int(maxEntry.get())
    size= int(sizeEntry.get())




    data=[]
    for _ in range(size):
        data.append(random.randrange(minval,maxval+1))
    drawdata(data,['red' for x in range(len(data))])

def startalgorithm():
    global data
    bubble_sort(data, drawdata,speedscale.get())



#ui
UI_frame=Frame(root,width=600,height =200,bg='grey')
UI_frame.grid(row=0,column=0,padx=10,pady=5)

canvas=Canvas(root,width=600,height =300,bg='white')
canvas.grid(row=1,column=0,padx=10,pady=5)

#user int row 0
Label(UI_frame,text="algorithm:",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)
algoMenu=ttk.Combobox(UI_frame,textvariable=selected_alg, values=['Bubble sort','Merge sort'])
algoMenu.grid(row=0,column=1,padx=5,pady=5)
algoMenu.current(0)
speedscale=Scale(UI_frame,from_=0.1,to=2.0,length=200,digits=2,resolution=0.2,orient=HORIZONTAL,label="select speed [s]")
speedscale.grid(row=0,column=2,padx=5,pady=5)
Button(UI_frame,text='Start',command=startalgorithm , bg='red').grid(row=0,column=3,padx=5,pady=5)

#row1
sizeEntry=Scale(UI_frame,from_=3,to=25,resolution=1,orient=HORIZONTAL,label="data size")
sizeEntry.grid(row=1,column=0,padx=5,pady=5)


minEntry=Scale(UI_frame,from_=0,to=10,resolution=1,orient=HORIZONTAL,label="min value")
minEntry.grid(row=1,column=1,padx=5,pady=5)

maxEntry=Scale(UI_frame,from_=10,to=100,resolution=1,orient=HORIZONTAL,label="max value")
maxEntry.grid(row=1,column=2,padx=5,pady=5)
Button(UI_frame,text='Generate',command=Generate , bg='white').grid(row=1,column=3,padx=5,pady=5)
root.mainloop()