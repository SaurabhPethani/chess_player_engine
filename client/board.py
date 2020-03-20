from tkinter import *
import conversation
root = Tk()
labelReference = []
whiteList = ['\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u2657', '\u2658', '\u2656']
blackList = ['\u265C', '\u265E', '\u265D', '\u265B', '\u265A', '\u265D', '\u265E', '\u265C']
previousColor = 'gray'
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

conversation = conversation.Client_Server_Converse(labelReference)
conversation.initConversation()

root.mainloop()
# class MetaLabel:
#     def __init__(self, position, character):
#         self.position = position
#         if character == 56:
#             self.character = "black:eleph"
#         elif character ==58:
#             self.character = 'black:horse'
#         elif character ==57:
#             self.character = 'black:camel'
#         elif character ==55:
#             self.character = 'black:king'
#         elif character ==54:
#             self.character = 'black:queen'
#         elif character ==59:
#             self.character = 'black:soldier'
#         elif character == 50:
#             self.character = "white:eleph"
#         elif character ==52:
#             self.character = 'white:horse'
#         elif character ==51:
#             self.character = 'white:camel'
#         elif character ==49:
#             self.character = 'white:king'
#         elif character ==48:
#             self.character = 'white:queen'
#         elif character ==53:
#             self.character = 'white:soldier'
        
        
        
# # Bind Every label with double click mouse event
# metaLabel={}
# index = 1
# for i in range(8,0,-1):
#     for j in range(8):
#         metaLabel[index] = (chr(j+65), i)
#         index += 1

# def onDoubleClick(event):
#     labelName = str(event.widget)
#     if event.widget['text'] is not '':
#         val = labelName[7:]
#         print(str(event.widget['text'].encode('utf')[2])[1:])
#         char = int(str(event.widget['text'].encode('utf')[2])[1:])
#         print(len(event.widget['text'].encode('utf')))
#         pos = ''
#         if val is '':
#             print(metaLabel[1])
#             pos = metaLabel[1]
#         else:
#             print(metaLabel[int(val)])
#             pos = metaLabel[int(val)]
#         metaObject = MetaLabel(pos, char)
#         dataString = pickle.dumps(metaObject)
#         client.send(dataString)
#         print("meta Object ",metaObject.character)
# for labelList in labelReference:
#     for label in labelList:
#         label.bind("<Double-Button-1>", onDoubleClick)

# def action(position):
#     pass
# def receivePositions():
#     while 1:
#         received = client.recv(1024)
#         receivedPosition = pickle.loads(received)
#         for item in receivedPosition:
#             l1 = labelReference[8-item[1]][ord(item[0])- 65]
#             l1.config(bg='limeyellow')
#             # l1.bind('<Button>', (event)->action((item[1], ord(item[0])-65), ))

# recvPosThread = threading.Thread(target=receivePositions)
# recvPosThread.start()
# print(labelReference)