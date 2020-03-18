import socket
import threading, pickle
import soldier, eleph
soc = socket.socket()
soc.bind(('localhost', 3690))
soc.listen(4)

class MetaLabel:
    def __init__(self, position, character):
        self.position = position
        self.character = character

class ReceiveRequest(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
    
    def processAndSend(self, char, pos):
        position = []

        if char == 'white:soldier' or char == 'black:soldier':
            sold = soldier.Soldier(char, pos)
            position = sold.getPositions()

        if char == 'white:eleph' or char == 'black:eleph':
            elephant = eleph.Elephant(char, pos)
            position = elephant.getPositions()

        print("Positions: ",position)
        dataString = pickle.dumps(position)
        self.client.send(dataString)            

    def run(self):
        while True:
            data = self.client.recv(1024)
            positionString = pickle.loads(data)
            print(type(positionString))
            print(positionString.position)
            print(positionString.character)
            self.processAndSend(positionString.character, positionString.position)
        self.client.close()
# while True:
client,addr = soc.accept()
receiver = ReceiveRequest(client)
receiver.start()