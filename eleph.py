class Elephant:
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position

    def checkMiddleCase(self, finalPositions):
        letters = [chr(65+i) for i in range(8)]
        indexes = [i for i in range(1,9)]

        index1 = letters.index(self.position[0])
        index2 = indexes.index(self.position[1])

        for i in indexes[:index2]:
            finalPositions.append((self.position[0], i))
        for i in indexes[index2+1: ]:
            finalPositions.append((self.position[0], i))
        for j in letters[:index1]:
            finalPositions.append((j, self.position[1]))
        for j in letters[index1+1: ]:
            finalPositions.append((j, self.position[1]))
        
    def getPositions(self):
        finalPositions = []
        
        if self.pieceColor == 'white:eleph':
            finalPositions.append('white:eleph')
            finalPositions.append(self.position)
            self.checkMiddleCase(finalPositions)
            return finalPositions

        else:
            finalPositions.append('black:eleph')
            finalPositions.append(self.position)
            self.checkMiddleCase(finalPositions)
            return finalPositions
        
        return finalPositions