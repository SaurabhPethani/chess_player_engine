import socket
import threading, pickle


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
        finalPositions = []

        if char == 'white:soldier':
            if pos[1] == 2:
                finalPositions.append((pos[0], 4))
                finalPositions.append((pos[0], 3))

            else:
                finalPositions.append((pos[0], pos[1]+1))

        self.client.send(finalPositions)            

    def run(self):
        while True:
            data = self.client.recv(1024)
            positionString = pickle.loads(data)
            print(type(positionString))
            print(positionString.position)
            print(positionString.character)
            self.processAndSend(positionString.character, positionString.position)
        self.client.close()
while True:
    client,addr = soc.accept()
    receiver = ReceiveRequest(client)
    receiver.start()
