from tkinter import *
from conversation import Client_Server_Converse
root = Tk()
labelReference = []
whiteList = ['\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u2657', '\u2658', '\u2656']
blackList = ['\u265C', '\u265E', '\u265D', '\u265B', '\u265A', '\u265D', '\u265E', '\u265C']
color = input("Enter the Color: ")
whiteListNum = [ord(num) for num in whiteList ]
blackListNum = [ord(num) for num in blackList]
for i in range(8):
    ls = []
    for j in range(8): 
        l1 = Label(root, bg='lightgoldenrod',height=4, width=7)
        l1.grid(row=i+1,column=j+1, padx=2, pady=2)
        ls.append(l1)
    labelReference.append(ls)
# Printing Black Pieces
for i in range(8):
    labelReference[0][i]['text'] = blackList[i]
for i in range(8):
    labelReference[1][i]['text'] = '\u265F'

# Printing White Pieces
for i in range(8):
    labelReference[7][i]['text'] = whiteList[i]
for i in range(8):
    labelReference[6][i]['text'] = '\u2659'

conversatio = Client_Server_Converse(labelReference)
conversatio.initConversation(color)
root.mainloop()