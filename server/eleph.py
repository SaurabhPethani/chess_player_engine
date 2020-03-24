class Elephant:
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position

    def checkMiddleCase(self, finalPositions, color):
        letters = [chr(65+i) for i in range(8)]
        indexes = [i for i in range(1,9)]
        tempList = []
        index1 = letters.index(self.position[0])
        index2 = indexes.index(self.position[1])
        if color == 'white':            
            for i in indexes[0 if index2-1<0 else index2-1::-1]:
                tempList.append((self.position[0], i))
            finalPositions.append(tempList)
            tempList=[]
            for i in indexes[index2+1: ]:
                tempList.append((self.position[0], i))
            finalPositions.append(tempList)
            tempList=[]
            for j in letters[0 if index1-1<0 else index1-1::-1]:
                tempList.append((j, self.position[1]))
            finalPositions.append(tempList)
            tempList=[]
            for j in letters[index1+1: ]:
                tempList.append((j, self.position[1]))
            finalPositions.append(tempList)
            tempList=[]
        else:
            for i in indexes[0 if index2-1< 0 else index2-1: :-1]:
                tempList.append((self.position[0], i))
            finalPositions.append(tempList)
            tempList=[]
            for i in indexes[index2+1: ]:
                tempList.append((self.position[0], i))
            finalPositions.append(tempList)
            tempList=[]
            for j in letters[0 if index1-1<0 else index1-1::-1]:
                tempList.append((j, self.position[1]))
            finalPositions.append(tempList)
            tempList=[]
            for j in letters[index1+1: ]:
                tempList.append((j, self.position[1]))
            finalPositions.append(tempList)
            tempList=[]

    def getPositions(self):
        finalPositions = []
        
        if self.pieceColor == 'white:eleph':
            finalPositions.append('white:eleph')
            finalPositions.append(self.position)
            self.checkMiddleCase(finalPositions, 'white')
            return finalPositions

        else:
            finalPositions.append('black:eleph')
            finalPositions.append(self.position)
            self.checkMiddleCase(finalPositions, 'black')
            return finalPositions
        
        return finalPositions