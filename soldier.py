import pickle
class Soldier:
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position

    def getPositions(self):
        finalPositions = []
        if self.pieceColor == 'white:soldier':
            if self.position[1] == 2:
                finalPositions.append((self.position[0], 4))
                finalPositions.append((self.position[0], 3))

            else:
                finalPositions.append((self.position[0], self.position[1]+1))
        
        else:
            if self.position[1] == 7:
                finalPositions.append((self.position[0], 6))
                finalPositions.append((self.position[0], 5))
            
            else:
                finalPositions.append((self.position[0], self.position[1] - 1))
        
        return finalPositions
