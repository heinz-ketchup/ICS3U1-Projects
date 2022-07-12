# Author: Gavin Xiong
# Date: 2022/06/15
# Purpose: File justify exercise.
# -------------------------------------------------------------------------------------

# DEPENDENCIES
import os

# CLASSES

""" IntGroup

Author: Gavin Xiong
Date: 2022/06/15
Purpose: File justify functions.

    DATA ELEMENTS
        wordsList
        docList
        strInputFile
        strOutputFile
        strJustification
        intWidth
        
    METHODS
        __init__
        readFile()
        writeFile()
        createDoc()
        justifyLeft()
        justifyRight()
        justifyCentre()
        __str__

    DEPENDENCIES
        OS
"""
class JustifyText:
    """ __init__
    Author: Gavin Xiong
    Date: 2022/06/15
    Purpose: __init__ functions
    Parameters: strInputFile, strOutputFile, strJustification, intWidth.
    Output: N/A
    """
    def __init__(self, strInputFile = "input.txt", strOutputFile = "output.txt", 
                strJustification = "L", intWidth = 60):

        if type(strInputFile) != str: strInputFile = "input.txt"
        if type(strOutputFile) != str: strOutputFile = "output.txt"
        if type(strJustification) != str: strJustification = "L"
        if type(intWidth) != int: intWidth = 60
        
        strJustification = strJustification.upper()

        if strJustification != "L" and strJustification != "C" and strJustification != "R" and strJustification != "F":
            strJustification = "L"

        if not (intWidth >= 30 and intWidth <= 90): intWidth = 60
        
        self.wordsList = []
        self.docList = []
        self.strInputFile = strInputFile
        self.strOutputFile = strOutputFile
        self.strJustification = strJustification
        self.intWidth = intWidth

        self.readFile()
        self.createDoc()
        self.writeFile()

    """ readFile
    Author: Gavin Xiong
    Date: 2022/06/05
    Purpose: read files
    Parameters: N/A
    Output: N/A
    """
    def readFile(self):
        self.wordsList = []

        if os.path.isfile(self.strInputFile):
            inputFile = open(self.strInputFile, "r")
        else:
            self.wordsList.append("ERROR: File does not exist.")

        for index1, line in enumerate(inputFile):
            lineList = line.strip().split(" ")
            for index2, word in enumerate(lineList):
                if len(word) > 30:
                    word = word[:30]
                self.wordsList.append(word)

        inputFile.close()

    """ writeFile
    Author: Gavin Xiong
    Date: 2022/06/15
    Purpose: write values onto file.
    Parameters: N/A
    Output: N/A
    """
    def writeFile(self):
        outputFile = open(self.strOutputFile, 'w')
        outputFile.write(self.__str__())
        outputFile.close()

    """ createDoc
    Author: Gavin Xiong
    Date: 2022/06/15
    Purpose: Calls justify
    Parameters: N?A
    Output: N/A
    """
    def createDoc(self):
        self.writeFile()
        if self.strJustification == "L":
            self.justifyLeft()
        elif self.strJustification == "R":
            self.justifyRight()
        elif self.strJustification == "C":
            self.justifyCentre()

    """ justifyLeft
    Author: Gavin Xiong
    Date: 2022/06/15
    Purpose: justify left
    Parameters:N/A
    Output: N/A
    """
    def justifyLeft(self):
        strLine = ""
        for index, word in enumerate(self.wordsList):
            if strLine == "":
                strLine += word
            elif (len(strLine) + len(word) + 1) <= self.intWidth:
                strLine += " " + word
            else:
                self.docList.append(strLine)
                strLine = word
        if strLine != "":
            self.docList.append(strLine)

    """ justifyRight
    Author: Gavin Xiong
    Date: 2022/06/15
    Purpose: justify right
    Parameters:N/A
    Output: N/A
    """
    def justifyRight(self):
        self.justifyLeft()
        for index, line in enumerate(self.docList):
            self.docList[index] = " " * (self.intWidth - len(line)) + line
    
    """ justifyCentre
    Author: Gavin Xiong
    Date: 2022/06/15
    Purpose: justify centre
    Parameters:N/A
    Output: N/A
    """
    def justifyCentre(self):
        self.justifyLeft()
        for index, line in enumerate(self.docList):
            self.docList[index] = " " * ((self.intWidth - len(line)) // 2) + line

    
    """ __str__
    Author: Gavin Xiong
    Date: 2022/06/15
    Purpose: __str__ functions
    Parameters:N/A
    Output: paragraph
    """
    def __str__(self):
        paragraph = ""
        for index, line in enumerate(self.docList):
            paragraph += line + "\n"
        return paragraph
        

justifyExample = JustifyText(strInputFile = "copypasta.txt", strJustification = "C", intWidth = 90)
print(justifyExample)