import socket,pickle,threading
from   filter_positions import FilterPosition
client = socket.socket()
background = 'lightgoldenrod'
colors= ['white', 'black']
class MetaLabel:
    def __init__(self, position, character):
        self.position = position
        self.character = "black:eleph" if character == 56 else 'black:horse' if character == 58 else 'black:camel' if character == 57 else 'black:king' if character==55 else 'black:queen' if character == 54 else 'black:soldier' if character==59 else 'white:eleph' if character==50 else 'white:horse' if character == 52 else 'white:camel' if character==51 else 'white:king' if character == 49 else 'white:queen' if character==48 else 'white:soldier' if character==53 else ''
        # if character == 56:
        #     self.character = "black:eleph"
        # elif character ==58:
        #     self.character = 'black:horse'
        # elif character ==57:
        #     self.character = 'black:camel'
        # elif character ==55:
        #     self.character = 'black:king'
        # elif character ==54:
        #     self.character = 'black:queen'
        # elif character ==59:
        #     self.character = 'black:soldier'
        # elif character == 50:
        #     self.character = "white:eleph"
        # elif character ==52:
        #     self.character = 'white:horse'
        # elif character ==51:
        #     self.character = 'white:camel'
        # elif character ==49:
        #     self.character = 'white:king'
        # elif character ==48:
        #     self.character = 'white:queen'
        # elif character ==53:
        #     self.character = 'white:soldier'
labRef= []
class Client_Server_Converse:
    def __init__(self, labelReference):
        global labRef
        self.labelReference = labelReference
        labRef = labelReference
        self.count = 2
    def initConversation(self, color):
        metaLabeling()
        makeConnection()
        client.send(color.encode('utf-8'))
        color = client.recv(1024).decode('utf-8')
        bindLabel(color)
        startReceiving(self.labelReference)
def makeConnection():
    client.connect(('localhost', 3690))

metaLabel={}
def metaLabeling():
    index = 1
    for i in range(8,0,-1):
        for j in range(8):
            metaLabel[index] = (chr(j+65), i)
            index += 1


def onDoubleClick(event):
    labelName = str(event.widget)
    print(event)
    if event.widget['text'] is not '':
        val = labelName[7:]
        char = int(str(event.widget['text'].encode('utf')[2])[1:])
        pos = ''
        if val is '':
            pos = metaLabel[1]
        else:
            pos = metaLabel[int(val)]
        metaObject = MetaLabel(pos, char)
        dataString = pickle.dumps(metaObject)
        client.send(dataString)
        unbindLabel(metaObject.character[:5])

def bindLabel(color):
    if color == 'white':
        for labelList in labRef[6:]:
            for label in labelList:
                label.bind("<Double-Button-1>", onDoubleClick)
    elif color == 'black':
        for labelList in labRef[:2]:
            for label in labelList:
                label.bind("<Double-Button-1>", onDoubleClick)
def unbindLabel(color):
    if color == 'white':
        for labelList in labRef[6:]:
            for label in labelList:
                label.unbind("<Double-Button-1>")
    elif color == 'black':
        for labelList in labRef[:2]:
            for label in labelList:
                label.unbind("<Double-Button-1>")
functionId= []
labelBindList = []

def action(event, args):
    global labelBindList
    sendList = []
    if args[2] == 'black:soldier':
        args[1].config(text = '\u265F')
    elif args[2] == 'white:soldier':
        args[1].config(text = '\u2659')
    elif args[2] == 'black:eleph':
        args[1].config(text= '\u265C')
    elif args[2] == 'white:eleph':
        args[1].config(text= '\u2656')
    elif args[2] == 'black:camel':
        args[1].config(text= '\u265D')
    elif args[2] == 'white:camel':
        args[1].config(text= '\u2657')
    elif args[2] == 'black:horse':
        args[1].config(text= '\u265E')
    elif args[2] == 'white:horse':
        args[1].config(text= '\u2658')
    elif args[2] == 'black:queen':
        args[1].config(text= '\u265A')
    elif args[2] == 'white:queen':
        args[1].config(text= '\u2654')
    elif args[2] == 'black:king':
        args[1].config(text= '\u265B')
    elif args[2] == 'white:king':
        args[1].config(text= '\u2655')
    sendList.append(args[5])
    args[1].bind('<Double-Button-1>', onDoubleClick)

    for lab in labelBindList:
        lab.config(bg=background)
        lab.unbind('<Button-1>')
    original = args[4][8-args[3][1]][ord(args[3][0])- 65]
    sendList.append(args[3])    # original position
    original.unbind('<Double-Button-1>')
    original.config(text='')
    labelBindList.clear()
    bindLabel(args[2][:5])
    sendData = pickle.dumps(sendList)
    client.send(sendData)
    
def receivePositions(labelReference):
    global labelBindList
    while True:
        received = client.recv(2048)
        receivedData = pickle.loads(received)
        if len(receivedData) > 3:
            filterPos = FilterPosition(receivedData, labelReference)
            validPos = filterPos.getList()
            for item in validPos:
                l1 = labelReference[8-item[1]][ord(item[0])- 65]
                labelBindList.append(l1)
                l1.config(bg='cyan')
                data= {1: l1, 2: receivedData[0], 3: receivedData[1], 4:labelReference, 5:item}
                l1.bind('<Button-1>', lambda event, arg=data: action(event, arg))
        else:
            original = labelReference[8-receivedData[1][1]][ord(receivedData[1][0])- 65]
            intended = labelReference[8-receivedData[0][1]][ord(receivedData[0][0])- 65]
            char = original['text']
            original['text'] = ''
            original.unbind('<Double-Button-1>')
            intended['text'] = char
            intended.bind('<Double-Button-1>')
def startReceiving(labelReference):
    recvPosThread = threading.Thread(target=receivePositions, args=(labelReference,))
    recvPosThread.start()