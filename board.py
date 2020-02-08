from tkinter import *
import tkinter
root = Tk()
labelReference = []
whiteList = ['\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u2657', '\u2658', '\u2656']
blackList = ['\u265C', '\u265E', '\u265D', '\u265B', '\u265A', '\u265D', '\u265E', '\u265C']
previousColor = 'gray'
for i in range(8):
    ls = []       
    if i % 2==1:
        previousColor='gray'
    else:   
        previousColor='white'
    for j in range(8):        
        if previousColor == 'gray': 
            l1 = Label(root, bg="gray",height=4, width=7)
            l1.grid(row=i+1,column=j+1)
            ls.append(l1)        
            previousColor = 'white'
        else:
            l2 = Label(root, bg="white",height=4, width=7)
            l2.grid(row=i+1,column=j+1)
            ls.append(l2)
            previousColor = 'gray'
    labelReference.append(ls)

# Printing Black Pieces
# for i in range(8):
#     labelReference[0][i]['text'] = blackList[i]
for i in range(8):
    labelReference[1][i]['image'] = tkinter.PhotoImage(file = './soldier.png')

# Printing White Pieces
# for i in range(8):
#     labelReference[7][i]['image'] = whiteList[i]
# for i in range(8):
#     labelReference[6][i]['text'] = '\u2659'

# Bind Every label with double click mouse event
metaLabel={}
index = 1
for i in range(8):
    for j in range(8):
        metaLabel[index] = (i,j)
        index += 1

def onDoubleClick(event):
    labelName = str(event.widget)
    if event.widget['text'] is not '':
        val = labelName[7:]
        print(str(event.widget['text']))
        print(metaLabel[int(val)])
for labelList in labelReference:
    for label in labelList:
        label.bind("<Double-Button-1>", onDoubleClick)
print(labelReference)
root.mainloop()