import socket
import threading, pickle
from conversation import Client_Server_Converse
from soldier import Soldier
from eleph import Elephant
from camel import Camel
from horse import Horse
from queen import Queen
from king import King
# from . import soldier, eleph, camel, horse, queen, king
soc = socket.socket()
soc.bind(('localhost', 3690))
soc.listen(4)

class MetaLabel:
    def __init__(self, position, character):
        self.position = position
        self.character = character
globalTurn = {'YOUR_TURN':'YOUR_TURN', 'MY_TURN':'MY_TURN'}
localTurn = 'MY_TURN'
class ReceiveRequest(threading.Thread):
    def __init__(self, client, turn):
        threading.Thread.__init__(self)
        self.client = client
        self.turn = turn
    
    def processAndSend(self, char, pos):
        position = []
        if char == 'white:soldier' or char == 'black:soldier':
            sold = Soldier(char, pos)
            position = sold.getPositions()

        elif char == 'white:eleph' or char == 'black:eleph':
            elephant = Elephant(char, pos)
            position = elephant.getPositions()
        
        elif char == 'white:camel' or char == 'black:camel':
            cam = Camel(char, pos)
            position = cam.getPositions()

        elif char == 'white:horse' or char == 'black:horse':
            hors = Horse(char, pos)
            position = hors.getPositions()
            
        elif char == 'white:queen' or char == 'black:queen':
            qun = Queen(char, pos)
            position = qun.getPositions()
        
        elif char == 'white:king' or char == 'black:king':
            kin = King(char, pos)
            position = kin.getPositions()
        dataString = pickle.dumps(position)
        self.client.send(dataString)
           
    def sendToOther(self, position):
        data = pickle.dumps(position)
        for connection in toAll:
            if connection != self.client:
                connection.send(data)
    def run(self):
        global localTurn
        while True:
            if self.turn is localTurn:
                pass
            else:
                print("Wating for ", globalTurn)
                print("Completed ", self.turn)
                data = self.client.recv(1024)
                positionString = pickle.loads(data)
                print("Server Received: ",positionString)
                if type(positionString) is not list:    # if meta label object
                    self.processAndSend(positionString.character, positionString.position)
                elif type(positionString) is list:
                    self.sendToOther(positionString)
                    localTurn = globalTurn[self.turn]
        self.client.close()

    def validate(self, color):
        global colors
        if color in colors:
            colors.remove(color)
            return color
        color = colors[0]
        colors.pop(0)
        return color
toAll = []
colors = ['white', 'black']
turns = ['YOUR_TURN', 'MY_TURN']
while True:
    client,addr = soc.accept()
    toAll.append(client)
    receiver = ReceiveRequest(client, turns[0])
    turns.pop(0)
    color = client.recv(1024).decode('utf-8')
    result = receiver.validate(color)
    client.send(str(result).encode('utf-8'))
    receiver.start()