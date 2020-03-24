import eleph, camel
class Queen(eleph.Elephant, camel.Camel):
    def __init__(self, pieceColor, position):
        self.pieceColor = pieceColor
        self.position = position
        
    def getPositions(self):
        finalPositions = []
        
        if self.pieceColor == 'white:queen':
            finalPositions.append('white:queen')
            finalPositions.append(self.position)
            self.checkMiddleCase(finalPositions,'white')
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
            finalPositions.append('black:queen')
            finalPositions.append(self.position)
            self.checkMiddleCase(finalPositions, 'black')
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