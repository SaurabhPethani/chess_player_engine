class Soldier:
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position

    def getPositions(self):
        finalPositions = []
        letters = [chr(65+i) for i in range(8)]
        indexes = [i for i in range(1,9)]
        leftLetter = chr(ord(self.position[0])-1)
        rightLetter = chr(ord(self.position[0])+1)
        downIndex = self.position[1]-1
        upIndex = self.position[1]+1

        if self.pieceColor == 'white:soldier':
            finalPositions.append('white:soldier')
            finalPositions.append(self.position)
            if self.position[1] == 2:
                finalPositions.append((self.position[0], 4))
                finalPositions.append((self.position[0], 3))
                if leftLetter in letters:
                    finalPositions.append((leftLetter, upIndex))
                if rightLetter in letters:
                    finalPositions.append((rightLetter, upIndex))

            else:
                finalPositions.append((self.position[0], upIndex))
                if leftLetter in letters and upIndex in indexes:
                    finalPositions.append((leftLetter, upIndex))
                if rightLetter in letters and upIndex in indexes:
                    finalPositions.append((rightLetter, upIndex))

        
        else:
            finalPositions.append('black:soldier')
            finalPositions.append(self.position)
            if self.position[1] == 7:
                finalPositions.append((self.position[0], 6))
                finalPositions.append((self.position[0], 5))
                if leftLetter in letters:
                    finalPositions.append((leftLetter, downIndex))
                if rightLetter in letters:
                    finalPositions.append((rightLetter, downIndex))
            
            else:
                finalPositions.append((self.position[0], downIndex))
                if leftLetter in letters and downIndex in indexes:
                    finalPositions.append((leftLetter, downIndex))
                if rightLetter in letters and downIndex in indexes:
                    finalPositions.append((rightLetter, downIndex))
        
        return finalPositions