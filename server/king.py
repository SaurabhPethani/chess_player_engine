class King:
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position
    
    def getNeighbours(self, finalPositions):
        letters = [chr(65+i) for i in range(8)]
        indexes = [i for i in range(1,9)]

        index1 = letters.index(self.position[0])
        index2 = indexes.index(self.position[1])
        print("Index1 :", index1)
        print("Index2 :",index2)
        up = index2+1
        down= index2-1
        left = index1-1
        right = index1+1
        print("up: ",up)
        print("down: ",down)
        print("left: ",left)
        print("right: ",right)
        temp = [i for i in range(8)]
        if up in temp:
            finalPositions.append((letters[index1], indexes[up]))
        if down in temp:
            finalPositions.append((letters[index1], indexes[down]))
        if left in temp:
            finalPositions.append((letters[left], indexes[index2]))
        if right in temp:
            finalPositions.append((letters[right], indexes[index2]))
        if up in temp and right in temp:
            finalPositions.append((letters[right], indexes[up]))
        if down in temp and right in temp:
            finalPositions.append((letters[right], indexes[down]))
        if up in temp and left in temp:
            finalPositions.append((letters[left], indexes[up]))
        if down in temp and left in temp:
            finalPositions.append((letters[left], indexes[down]))
        

    def getPositions(self):
        finalPositions = []
        
        if self.pieceColor == 'white:king':
            finalPositions.append('white:king')
            finalPositions.append(self.position)
            self.getNeighbours(finalPositions)
            return finalPositions

        else:
            finalPositions.append('black:king')
            finalPositions.append(self.position)
            self.getNeighbours(finalPositions)
            return finalPositions
        
        return finalPositions