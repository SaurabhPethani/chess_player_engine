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
            self.checkMiddleCase(finalPositions)
            self.getDiagonals()
            if self.checkCorner(finalPositions):
                return finalPositions
            elif self.checkBoundary(finalPositions):
                return finalPositions
            else:
                finalPositions.extend(self.up_up+self.up_lo+self.lo_up+self.lo_lo)
            return finalPositions

        else:
            finalPositions.append('black:queen')
            finalPositions.append(self.position)
            self.checkMiddleCase(finalPositions)
            self.getDiagonals()
            if self.checkCorner(finalPositions):
                return finalPositions
            elif self.checkBoundary(finalPositions):
                return finalPositions
            else:
                finalPositions.extend(self.up_up+self.up_lo+self.lo_up+self.lo_lo)
            return finalPositions
        
        return finalPositions