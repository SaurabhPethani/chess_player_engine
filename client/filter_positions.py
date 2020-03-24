
class FilterPosition:
    def __init__(self, positions, labelReference):
        self.positions = positions
        self.labelReference = labelReference
        self.pieceName = self.positions[0][6:]
        self.pieceColor = self.positions[0][:5]

    def getList(self):
        if self.pieceName == 'soldier':
            return self.soldier()
        elif self.pieceName == 'horse':
            return self.horse()
        elif self.pieceName == 'camel':
            return self.camel()
        elif self.pieceName == 'eleph':
            return self.elephant()
        elif self.pieceName == 'queen':
            return self.queen()
        elif self.pieceName == 'king':
            return self.king()
        else:
            return None
        
    def getName(self, char):
        if char == 9817:
            return 'white:soldier'
        elif char == 9814:
            return 'white:eleph'
        elif char == 9816:
            return 'white:horse'
        elif char == 9815:
            return 'white:camel'
        elif char == 9813:
            return 'white:king'
        elif char == 9812:
            return 'white:queen'
        elif char == 9823:
            return 'black:soldier'
        elif char==9820:
            return 'black:eleph'
        elif char == 9822:
            return 'black:horse'
        elif char == 9821:
            return 'black:camel'
        elif char == 9819:
            return 'black:king'
        elif char == 9818:
            return 'black:queen'
        else:
            return ''

    def getLabelCharFromPosition(self, item):
        #returns name and labelreference
        # metaLabelList = ''
        print("Item in char pos : ",item)
        l1 = self.labelReference[8-item[1]][ord(item[0])- 65]
        name = ''
        print("L1 = ",l1)
        if l1['text'] != '':
            name = self.getName(ord(l1['text']))
        # metaLabelList.append(name)
        # metaLabelList.append(l1)
        return name
        
    def soldier(self):
        currentPosition = self.positions[1]
        finalList= []
        if self.pieceColor == 'white':
            for item in self.positions[2:]:
                if currentPosition[0] == item[0]:
                    metaLabelList = self.getLabelCharFromPosition(item)
                    if metaLabelList == '':
                        finalList.append(item)
                else:
                    metaLabelList = self.getLabelCharFromPosition(item)
                    if metaLabelList[:5] == 'black':
                        finalList.append(item)
        else:
            for item in self.positions[2:]:
                if currentPosition[0] == item[0]:
                    metaLabelList = self.getLabelCharFromPosition(item)
                    if metaLabelList == '':
                        finalList.append(item)
                else:
                    metaLabelList = self.getLabelCharFromPosition(item)
                    if metaLabelList[:5] == 'white':
                        finalList.append(item)
        return finalList

    def horse(self):
        finalList = []
        if self.pieceColor == 'white':
            for item in self.positions[2:]:
                metaLabel = self.getLabelCharFromPosition(item)
                if metaLabel == '':
                    finalList.append(item)
                else:
                    if metaLabel[:5] == 'black':
                        finalList.append(item)
        else:
            for item in self.positions[2:]:
                metaLabel = self.getLabelCharFromPosition(item)
                if metaLabel == '':
                    finalList.append(item)
                else:
                    if metaLabel[:5] == 'white':
                        finalList.append(item)

        return finalList
    def camel(self):
        finalList = []
        if self.pieceColor == 'white':
            for items in self.positions[2:]:
                for item in items:
                    metaLabel = self.getLabelCharFromPosition(item)
                    if metaLabel == '':
                        finalList.append(item)
                    else:
                        if metaLabel[:5] == 'black':
                            finalList.append(item)
                            break
                        elif metaLabel[:5] == 'white':
                            break
        else:
            for items in self.positions[2:]:
                for item in items:
                    metaLabel = self.getLabelCharFromPosition(item)
                    if metaLabel == '':
                        finalList.append(item)
                    else:
                        if metaLabel[:5] == 'white':
                            finalList.append(item)
                            break
                        elif metaLabel[:5] == 'black':
                            break
        return finalList

    def elephant(self):
        finalList = []
        if self.pieceColor == 'white':
            for items in self.positions[2:]:
                print("Item from position: ", items)
                for item in items:
                    metaLabel = self.getLabelCharFromPosition(item)
                    print("Meta Label: ",metaLabel)
                    if metaLabel == '':
                        finalList.append(item)
                    else:
                        if metaLabel[:5] == 'black':
                            finalList.append(item)
                            break
                        elif metaLabel[:5] == 'white':
                            break
        else:
            for items in self.positions[2:]:
                for item in items:
                    metaLabel = self.getLabelCharFromPosition(item)
                    if metaLabel == '':
                        finalList.append(item)
                    else:
                        if metaLabel[:5] == 'white':
                            finalList.append(item)
                            break
                        elif metaLabel[:5] == 'black':
                            break
        print("Elephant FinalList = ", finalList)
        return finalList

    def queen(self):
        finalList = []
        if self.pieceColor == 'white':
            for items in self.positions[2:]:
                print("Item from position: ", items)
                for item in items:
                    metaLabel = self.getLabelCharFromPosition(item)
                    print("Meta Label: ",metaLabel)
                    if metaLabel == '':
                        finalList.append(item)
                    else:
                        if metaLabel[:5] == 'black':
                            finalList.append(item)
                            break
                        elif metaLabel[:5] == 'white':
                            print("Breaking White Pair")
                            break
        else:
            for items in self.positions[2:]:
                for item in items:
                    metaLabel = self.getLabelCharFromPosition(item)
                    if metaLabel == '':
                        finalList.append(item)
                    else:
                        if metaLabel[:5] == 'white':
                            finalList.append(item)
                            break
                        elif metaLabel[:5] == 'black':
                            break
        print("Elephant FinalList = ", finalList)
        return finalList

    def king(self):
        finalList=[]
        if self.pieceColor == 'white':
            for item in self.positions[2:]:
                metaLabel = self.getLabelCharFromPosition(item)
                if metaLabel == '':
                    finalList.append(item)
                else:
                    if metaLabel[:5] == 'black':
                        finalList.append(item)
        else:
            for item in self.positions[2:]:
                metaLabel = self.getLabelCharFromPosition(item)
                if metaLabel == '':
                    finalList.append(item)
                else:
                    if metaLabel[:5] == 'white':
                        finalList.append(item)

        return finalList

