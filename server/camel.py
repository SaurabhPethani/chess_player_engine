class Camel:
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position

    def checkCorner(self,finalPositions):
        if self.position[0] == 'A' and self.position[1] == 1:
            finalPositions.append(self.up_up)
            return True
        elif self.position[0] == 'H' and self.position[1] == 8:
            finalPositions.append(self.lo_lo)
            return True
        elif self.position[0] == 'A' and self.position[1] == 8:
            finalPositions.append(self.up_lo)
            return True
        elif self.position[0] == 'H' and self.position[1] == 1:
            finalPositions.append(self.lo_up)
            return True
        return False
    
    def checkBoundary(self, finalPositions):
        if self.position[1] == 1:
            finalPositions.append(self.lo_up)
            finalPositions.append(self.up_up)
            return True
        elif self.position[1] == 8:
            finalPositions.append(self.lo_lo)
            finalPositions.append(self.up_lo)
            return True
        elif self.position[0] == 'A':
            finalPositions.append(self.up_up)
            finalPositions.append(self.up_lo)
            return True
        elif self.position[0] == 'H':
            finalPositions.append(self.lo_up)
            finalPositions.append(self.lo_lo)
            return True
        return False

    def getDiagonals(self):
        letters = [chr(65+i) for i in range(8)]
        indexes = [i for i in range(1,9)]

        letterIndex = letters.index(self.position[0])
        verticalIndex = indexes.index(self.position[1])
        
        letterListLower = letters[letterIndex-1::-1]
        letterListUpper = letters[letterIndex+1:]
        indexListLower = indexes[verticalIndex-1::-1]
        indexListUpper = indexes[verticalIndex+1:]

        print("Letter lower: ",letterListLower)
        print("Letter Upper: ",letterListUpper)
        print("Index Lower: ", indexListLower)
        print("Index Upper: ",indexListUpper)
        self.up_up = list(zip(letterListUpper, indexListUpper))
        self.lo_lo = list(zip(letterListLower, indexListLower))
        self.lo_up = list(zip(letterListLower, indexListUpper))
        self.up_lo = list(zip(letterListUpper, indexListLower))
    def getPositions(self):
        finalPositions = []
        
        if self.pieceColor == 'white:camel':
            finalPositions.append('white:camel')
            finalPositions.append(self.position)
            self.getDiagonals()
            if self.checkCorner(finalPositions):
                return finalPositions
            elif self.checkBoundary(finalPositions):
                return finalPositions
            else:
                finalPositions.append(self.up_up)
                finalPositions.append(self.up_lo)
                finalPositions.append(self.lo_up)
                finalPositions.append(self.lo_lo)
            return finalPositions

        else:
            finalPositions.append('black:camel')
            finalPositions.append(self.position)
            self.getDiagonals()
            if self.checkCorner(finalPositions):
                return finalPositions
            elif self.checkBoundary(finalPositions):
                return finalPositions
            else:
                finalPositions.append(self.up_up)
                finalPositions.append(self.up_lo)
                finalPositions.append(self.lo_up)
                finalPositions.append(self.lo_lo)
            return finalPositions            
        return finalPositions