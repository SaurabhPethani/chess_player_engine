import socket,pickle,threading

client = socket.socket()

class MetaLabel:
    def __init__(self, position, character):
        self.position = position
        if character == 56:
            self.character = "black:eleph"
        elif character ==58:
            self.character = 'black:horse'
        elif character ==57:
            self.character = 'black:camel'
        elif character ==55:
            self.character = 'black:king'
        elif character ==54:
            self.character = 'black:queen'
        elif character ==59:
            self.character = 'black:soldier'
        elif character == 50:
            self.character = "white:eleph"
        elif character ==52:
            self.character = 'white:horse'
        elif character ==51:
            self.character = 'white:camel'
        elif character ==49:
            self.character = 'white:king'
        elif character ==48:
            self.character = 'white:queen'
        elif character ==53:
            self.character = 'white:soldier'
        
class Client_Server_Converse:
    def __init__(self, labelReference):
        self.labelReference = labelReference

    def initConversation(self):
        metaLabeling()
        makeConnection()
        bindLabel(self.labelReference)
        startReceiving(self.labelReference)

# Bind Every label with double click mouse event
def makeConnection():
    client.connect(('localhost', 3690))

metaLabel={}
def metaLabeling():
    index = 1
    for i in range(8,0,-1):
        for j in range(8):
            metaLabel[index] = (chr(j+65), i)
            index += 1
    print(metaLabel)


def onDoubleClick(event):
    labelName = str(event.widget)
    if event.widget['text'] is not '':
        val = labelName[7:]
        print(str(event.widget['text'].encode('utf')[2])[1:])
        char = int(str(event.widget['text'].encode('utf')[2])[1:])
        print(len(event.widget['text'].encode('utf')))
        pos = ''
        if val is '':
            print(metaLabel[1])
            pos = metaLabel[1]
        else:
            print(metaLabel[int(val)])
            pos = metaLabel[int(val)]
        metaObject = MetaLabel(pos, char)
        dataString = pickle.dumps(metaObject)
        client.send(dataString)
        print("meta Object ",metaObject.character)

def bindLabel(labelReference):
    for labelList in labelReference:
        for label in labelList:
            label.bind("<Double-Button-1>", onDoubleClick)

def action(position):
    pass
def receivePositions(labelReference):
    while 1:
        received = client.recv(1024)
        receivedPosition = pickle.loads(received)
        for item in receivedPosition:
            l1 = labelReference[8-item[1]][ord(item[0])- 65]
            l1.config(bg='cyan')
            # l1.bind('<Button>', (event)->action((item[1], ord(item[0])-65), ))

def startReceiving(labelReference):
    recvPosThread = threading.Thread(target=receivePositions, args=(labelReference,))
    recvPosThread.start()