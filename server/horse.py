class Horse:
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position

    def getAllPositions(self, finalPositions):
        letters = [chr(65+i) for i in range(8)]
        indexes = [i for i in range(1,9)]

        index1 = letters.index(self.position[0])
        index2 = indexes.index(self.position[1])

        ind1 = index1+2
        ind2 = index1-2
        ind3 = index1+1
        ind4 = index1-1

        ind5 = index2+2
        ind6 = index2-2
        ind7 = index2+1
        ind8 = index2-1

        temp = [i for i in range(8)]
        if ind1 in temp and ind7 in temp:
            finalPositions.append((letters[ind1], indexes[ind7]))
        if ind1 in temp and ind8 in temp:
            finalPositions.append((letters[ind1], indexes[ind8]))
        if ind2 in temp and ind7 in temp:
            finalPositions.append((letters[ind2], indexes[ind7]))
        if ind2 in temp and ind8 in temp:
            finalPositions.append((letters[ind2], indexes[ind8]))
        
        if ind3 in temp and ind6 in temp:
            finalPositions.append((letters[ind3], indexes[ind6]))
        if ind4 in temp and ind6 in temp:
            finalPositions.append((letters[ind4], indexes[ind6]))
        if ind3 in temp and ind5 in temp:
            finalPositions.append((letters[ind3], indexes[ind5]))
        if ind4 in temp and ind5 in temp:
            finalPositions.append((letters[ind4], indexes[ind5]))
        


    def getPositions(self):
        finalPositions = []
        
        if self.pieceColor == 'white:horse':
            finalPositions.append('white:horse')
            finalPositions.append(self.position)
            self.getAllPositions(finalPositions)
            return finalPositions

        else:
            finalPositions.append('black:horse')
            finalPositions.append(self.position)
            self.getAllPositions(finalPositions)
            return finalPositions
        
        return finalPositions