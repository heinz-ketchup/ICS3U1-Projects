# Author: Gavin Xiong
# Date: 2022/05/31
# Purpose: Data structures for a int group.
# -------------------------------------------------------------------------------------

# DEPENDENCIES
import random

# CLASS
""" IntGroup

Author: Gavin Xiong
Date: 2022/05/31
Purpose: Int and list functions.

    DATA ELEMENTS
        size: Size of the list
        
    METHODS
        __init__: __init__
        __str__: __str__
        initAsNum: List of one value
        initAsSeq: Sequence of values
        calcTotal: Calculates total of list
        calcMean: Calculates mean of list
        findLargest: Finds largest value in list
        calcFreq: Calculates frequency of a value
        insertAt: Inserts a value
        removeAt: Removes a value
        removeAll: Remove all occurences of a value
        findFirst: Find first occurence of a value
        isSorted: Returns true if sorted
        merge: Merges two sorted lists
        refreshSize: Refreshes the size data element.

    DEPENDENCIES
        Random
"""
class IntGroup:
    """ __init__
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: __init__ functions
    Parameters:N/A
    Output: N/A
    """
    def __init__(self, size = 0):
        if not (size >= 0 and size <= 20): size = 0

        self.size = size
        self.intList = []

        for i in range(size):
            self.intList.append(random.randint(0, size))
    
    """ __str__
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: __str__ functions
    Parameters:N/A
    Output: N/A
    """
    def __str__(self):
        return (f"{self.intList} size: {self.size}")
    
    """ initAsNum
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Init a list of one single value.
    Parameters: Value and size.
    Output: N/A
    """
    def initAsNum(self, value=0, size=0):
        self.intList.clear()
        for count in range(size):
            self.intList.append(value)

        self.refreshSize()    

    """ initAsSeq
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Init a sequence.
    Parameters: Size
    Output: N/A
    """
    def initAsSeq(self, size=0):
        self.intList.clear()
        for count in range(1, size+1):
            self.intList.append(count)

        self.refreshSize()

    """ calcTotal
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Calculate total sum of the list.
    Parameters: N/A
    Output: Sum
    """
    def calcTotal(self):
        sumTotal = 0
        for number in self.intList:
            sumTotal += number
        
        return sumTotal
    
    """ calcMean
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: calculate mean of the list.
    Parameters:N/A
    Output: Mean
    """
    def calcMean(self):
        return self.calcTotal() / len(self.intList)

    """ findLargest
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Find largest value in list.
    Parameters: N/A 
    Output: N/A
    """
    def findLargest(self):
        return max(self.intList, default="0")

    """ calcFreq
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Find number of occurences of a value.
    Parameters: Value
    Output: Count
    """
    def calcFreq(self, value=0):
        count = 0
        if value in self.intList:
            count = self.intList.count(value)

        return count

    """ insertAt
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Insert value at position
    Parameters: Position and value.
    Output: N/A
    """
    def insertAt(self, position=1, value=0):
        if abs(position) > len(self.intList):
            self.intList.append(value)
        else:
            if position <= 0: position = 1           # Offset from 0.
            self.intList.insert(position-1, value)

        self.refreshSize()

    """ removeAt
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Remove value at position.
    Parameters: Position
    Output: N/A
    """
    def removeAt(self, position=1):
        if not (abs(position) > len(self.intList)):
            del self.intList[position-1]

        self.refreshSize()

    """ removeAll
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Remove all occurences of a value.
    Parameters: Value
    Output: N/A
    """
    def removeAll(self, value=0):
        while value in self.intList:
            self.intList.remove(value)

        self.refreshSize()

    """ findFirst
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Find first index of a value.
    Parameters: Value
    Output: Position of the value.
    """
    def findFirst(self, value=0):
        if not value in self.intList:
            position = -1
        else: 
            position = self.intList.index(value) + 1

        return position

    """ isSorted
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Checks whether list is sorted.
    Parameters:N/A
    Output: Bool of whether it is sorted.
    """   
    def isSorted(self):
        self.refreshSize()

        isSorted = True
        for index in range(1, self.size):
            if self.intList[index-1] > self.intList[index]:
                isSorted = False

        return isSorted

    """ merge
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Merge two sorted lists into a third one.
    Parameters: second
    Output: N/A
    """   
    def merge(self, secondGroup):
        if not (self.isSorted() and secondGroup.isSorted()):
            newIntGroup = IntGroup(size=0)
        else:
            newIntGroup = IntGroup(size=0)
            firstList = self.intList
            secondList = secondGroup.intList
            i1 = 0
            i2 = 0
            while i1 < len(firstList) and i2 < len(secondList):
                if firstList[i1] <= secondList[i2]:
                    newIntGroup.intList.append(firstList[i1])
                    i1 += 1
                else:
                    newIntGroup.intList.append(secondList[i2])
                    i2 += 1

            while i1 < len(firstList):
                newIntGroup.intList.append(firstList[i1])
                i1 += 1
            
            while i2 < len(secondList):
                newIntGroup.intList.append(secondList[i2])
                i2 += 1

        newIntGroup.refreshSize()

        return newIntGroup

    """ refreshSize
    Author: Gavin Xiong
    Date: 2022/06/01
    Purpose: Refresh size data element.
    Parameters:N/A
    Output: N/A
    """   
    def refreshSize(self):
        self.size = len(self.intList)

# MAIN

# Init
print("Init Demonstration")
testList = IntGroup(size = 10)
print(f"List Info: {testList}")
testList.initAsNum(size=10, value=42)
print(f"InitAsNum: {testList}")
testList.initAsSeq(size=10)
print(f"initAsSeq: {testList}")

# Calc
print()
print("Calc Demonstration")
testList = IntGroup(size = 10)
print(f"Calc List: {testList}")
print(f"Total: {testList.calcTotal()}")
print(f"Mean: {testList.calcMean()}")   

# Insert/Remove
print()
print("Insert/Remove demonstration")
print("Insert 'Insert', remove last pos and remove all 0s.")
testList = IntGroup(size = 10)
print(f"Insert/Remove List: {testList}")
testList.insertAt(position=5, value="Insert")
testList.removeAt(position=11)
testList.removeAll(value = 0)
print(f"Final: {testList}")

# Misc
print()
print("Misc Demonstration")
testList = IntGroup()
testList.intList = [1, 2, 2, 3, 3, 5, 7, 9]
testList.refreshSize()
print(f"Misc List: {testList}")
print(f"FindFirst: {testList.findFirst(7)}")
print(f"isSorted: {testList.isSorted()}")   
mergeList1 = IntGroup(size=2)
mergeList2 = IntGroup(size=5)   
mergeList1.intList.sort()
mergeList2.intList.sort()
print(f"List 1: {mergeList1}")
print(f"List 1: {mergeList2}")
print(f"Merged: {mergeList1.merge(mergeList2)}")
