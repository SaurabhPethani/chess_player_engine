import socket
import threading, pickle
import soldier, eleph, camel, horse,queen, king
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

        elif char == 'white:eleph' or char == 'black:eleph':
            elephant = eleph.Elephant(char, pos)
            position = elephant.getPositions()
        
        elif char == 'white:camel' or char == 'black:camel':
            cam = camel.Camel(char, pos)
            position = cam.getPositions()

        elif char == 'white:horse' or char == 'black:horse':
            hors = horse.Horse(char, pos)
            position = hors.getPositions()
            
        elif char == 'white:queen' or char == 'black:queen':
            qun = queen.Queen(char, pos)
            position = qun.getPositions()
        
        elif char == 'white:king' or char == 'black:king':
            kin = king.King(char, pos)
            position = kin.getPositions()

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
receiver.setDaemon(True)