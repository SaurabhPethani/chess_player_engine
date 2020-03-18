import pickle
class Elephant:
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position

    def checkCornerCases(self, finalPositions):
        letters = [chr(65+i) for i in range(8)]
        indexes = [i for i in range(1,9)]

        if self.position[0] == 'A' and self.position[1] in [1,8]:
            if self.position[1] == 1:
                for i in letters[1:]:
                    finalPositions.append((i, 1))
                for j in indexes[1:]:
                    finalPositions.append(('A', j))
            if self.position[1] == 8:
                for i in letters[1:]:
                    finalPositions.append((i, 8))
                for j in indexes[:-1]:
                    finalPositions.append(('A', j))
            return True
        if self.position[0] == 'H' and self.position[1] in [1,8]:
            if self.position[1] == 1:
                for i in letters[:-1]:
                    finalPositions.append((i, 1))
                for j in indexes[1:]:
                    finalPositions.append(('H', j))
            if self.position[1] == 8:
                for i in letters[:-1]:
                    finalPositions.append((i, 8))
                for j in indexes[:-1]:
                    finalPositions.append(('H', j))
            return True
        return False
    def checkBoundaryCases(self, finalPositions):
        letters = [chr(65+i) for i in range(8)]
        indexes = [i for i in range(1,9)]

        if self.position[1] == 1 and self.position[0] in letters:
            index = letters.index(self.position[0])
            for i in letters[:index]:
                finalPositions.append((i, 1))
            for i in letters[index+1:]:
                finalPositions.append((i, 1))
            for j in indexes[1:]:
                finalPositions.append((self.position[0], j))
            
            return True
        
        if self.position[1] == 8 and self.position[0] in letters:
            index = letters.index(self.position[0])
            for i in letters[:index]:
                finalPositions.append((i, 8))
            for i in letters[index+1:]:
                finalPositions.append((i, 8))
            for j in indexes[:-1]:
                finalPositions.append((self.position[0], j))
            
            return True
        
        if self.position[0] == 'A' and self.position[1] in indexes:
            index = indexes.index(self.position[1])
            for i in indexes[:index]:
                finalPositions.append(('A', i))
            for i in indexes[index+1:]:
                finalPositions.append(('A', i))
            for j in letters[1:]:
                finalPositions.append((j, self.position[1]))
            
            return True
        
        if self.position[0] == 'H' and self.position[1] in indexes:
            index = indexes.index(self.position[1])
            for i in indexes[:index]:
                finalPositions.append(('H', i))
            for i in indexes[index+1:]:
                finalPositions.append(('H', i))
            for j in letters[:-1]:
                finalPositions.append((j, self.position[1]))
            
            return True
        
        return False
    
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
            
            if self.checkCornerCases(finalPositions):
                return finalPositions
            elif self.checkBoundaryCases(finalPositions):
                return finalPositions
            else:
                self.checkMiddleCase(finalPositions)
                return finalPositions

        else:
            finalPositions.append('black:eleph')
            finalPositions.append(self.position)
            if self.checkCornerCases(finalPositions):
                return finalPositions
            elif self.checkBoundaryCases(finalPositions):
                return finalPositions
            else:
                self.checkMiddleCase(finalPositions)
                return finalPositions
        
        return finalPositions