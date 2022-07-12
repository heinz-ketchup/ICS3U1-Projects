# Author: Gavin Xiong
# Date: 2022/04/22
# Purpose: Create a calendar/date class
# ____________________________________________________________________

from tkinter import *

import sys
import io

# Author: Gavin Xiong
# Date: 2022/04/22
# Purpose: Provide date class functions.
# ____________________________________________________________________
# DATA ELEMENTS
# Day - which is between 1 and MaxDay.
# Month - which is between 1 and 12.
# Year - which is between 1600 and 2200.
# -------------------------------------------------
# METHODS
# __init__ - Initializes the object of the class.
# returnMonthName -  Converts the number to a month name.
# returnLeapYear -  Returns whether or not the year is a leap year.
# returnMaxDay -  Returns the max day of the month.
# calcZeller -  Returns the day of the week of any day.
# returnDayName - Converts day of the week into day name.
# dateValid - Returns whether or not the date is valid.
# getDate - Gets the date directly from the user.
# getPosDate - Assists getDate with getting some numbers.
# __str__ - Returns the object's values as a string.
# displayCalendar - Displays the calendar.
# generateCalendar - Returns a variable which stores the calendar.
# firstdayOfMonth - Returns the first day of any month.
# dayOfYear - Returns the day of the year.
# -------------------------------------------------
class Date:

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Initializes the object.
    # Parameters: day, month and year.
    # Output: Nothing
    def __init__(self, intDay = 1, intMonth = 1, intYear = 2019):
        self.intDay = intDay
        self.intMonth = intMonth
        self.intYear = intYear
        if not self.dateValid():
            self.intDay = 1
            self.intMonth = 1
            self.intYear = 2019

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Converts current month into string.
    # Parameters: Nothing
    # Output: Month name.
    def returnMonthName(self):
        if self.intMonth == 1:
            month = "January"
        elif self.intMonth == 2:
            month = "Feburary"
        elif self.intMonth == 3:
            month = "March"
        elif self.intMonth == 4:
            month = "April"
        elif self.intMonth == 5:
            month = "May"
        elif self.intMonth == 6:
            month = "June"
        elif self.intMonth == 7:
            month = "July"
        elif self.intMonth == 8:
            month = "August"
        elif self.intMonth == 9:
            month = "September"
        elif self.intMonth == 10:
            month = "October"
        elif self.intMonth == 11:
            month = "November"
        elif self.intMonth == 12:
            month = "December"
        else:
            print("Unexpected: %i" % self.intMonth)
            month = 1
        return month

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Checks if current year is a leap year.
    # Parameters: Nothing
    # Output: Boolean
    def returnLeapYear(self):
        year = self.intYear
        if (year % 4 == 0) and (year % 100 != 0):
            leapYear = True
        elif (year % 400 == 0) and (year % 100 == 0):
            leapYear = True
        else:
            leapYear = False
        return leapYear

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Returns max day of the month.
    # Parameters: Nothing
    # Output: Max day.
    def returnMaxDay(self):
        month = self.intMonth
        month31 = [1, 3, 5, 7, 8, 10, 12]
        month30 = [4, 6, 9, 11]
        if month in month31:
            maxDay = 31
        elif month in month30:
            maxDay = 30
        elif month == 2:
            if self.returnLeapYear():
                maxDay = 29
            else:
                maxDay = 28
        return maxDay

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Calculates day of the week.
    # Parameters: Nothing
    # Output: Day of the week.
    def calcZeller(self):
        day = self.intDay
        month = self.intMonth
        year = self.intYear
        
        m = month - 2
        y = year
        if m <= 0:
            m = m + 12
            y = y - 1

        p = y // 100
        r = y % 100

        zeller = (day + (26 * m - 2) // 10 + r + r // 4 + p // 4 + 5 * p) % 7

        return zeller

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Convert number into day name.
    # Parameters: Nothing
    # Output: Day name.
    def returnDayName(self):
        zeller = self.calcZeller()
        if zeller == 0:
            dayOfTheWeek = "Sunday"
        elif zeller == 1:
            dayOfTheWeek = "Monday"
        elif zeller == 2:
            dayOfTheWeek = "Tuesday"
        elif zeller == 3:
            dayOfTheWeek = "Wednesday"
        elif zeller == 4:
            dayOfTheWeek = "Thursday"
        elif zeller == 5:
            dayOfTheWeek = "Friday"
        elif zeller == 6:
            dayOfTheWeek = "Saturday"
        else:
            print("Unexpected: Zeller is %i" % zeller)
            dayOfTheWeek = "Monday"

        return dayOfTheWeek
    
    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Checks if current date is valid.
    # Parameters: Nothing
    # Output: Boolean value.
    def dateValid(self):
        if (self.intDay >= 1 and self.intDay <= self.returnMaxDay()) and (self.intMonth >= 1 and self.intMonth <= 12) \
            and (self.intYear >= 1600 and self.intYear <= 2200):
            valid = True
        else:
            valid = False
        return valid
    
    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Gets date values from user.
    # Parameters: Nothing
    # Output: Nothing
    def getDate(self):
        self.intYear = self.getPosDate(prompt = "year", low = 1600, high = 2200)
        self.intMonth = self.getPosDate(prompt = "month", low = 1, high = 12)
        self.intDay = self.getPosDate(prompt = "day", low = 1, high = self.returnMaxDay())
        while not self.dateValid():
            self.intYear = self.getPosDate(prompt = "year", low = 1600, high = 2200)
            self.intMonth = self.getPosDate(prompt = "month", low = 1, high = 12)
            self.intDay = self.getPosDate(prompt = "day", low = 1, high = self.returnMaxDay())
        return self

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Assists in getting values for date object from user.
    # Parameters: prompt, low and high values.
    # Output: Value from user.  
    def getPosDate(self, prompt = "day", low = 1, high=31):
        prompt = "Please enter the %s which is between %s and %s inclusive: " % (prompt, str(low), str(high))
        loopCheck = True
        strInput = input(prompt)

        while loopCheck:
            if not strInput.isdigit():
                print("Error: Not a valid number.")
                strInput = input(prompt)
            else:
                intInput = int(strInput)
                if not (intInput >= low and intInput <= high):
                    print("Error: %i is not within the specified range." % intInput)
                    strInput = input(prompt)
                else:
                    loopCheck = False
        return intInput
    
    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Converts object into string.
    # Parameters: Nothing
    # Output: Values of the object converted to string.
    def __str__(self):
        day = self.intDay
        year = self.intYear

        dayName = self.returnDayName()
        monthName = self.returnMonthName()

        strDate = "%s, %s %i, %i" % (dayName, monthName, day, year)
        return strDate

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Prints the calendar and day of the year.
    # Parameters: Nothing.
    # Output: Nothing
    def displayCalendar(self):
        print(self.generateCalendar())
        print()
        print(f"This is day {self.dayOfYear()} of the year {self.intYear}.")
    
    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Generates a calendar
    # Parameters: None.
    # Output: Variable containing calendar.
    def generateCalendar(self):
        # Storing all printing into one variable.
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        # Printing header
        print(f"{self.__str__(): ^27}")
        dateString = "%s %i" % (self.returnMonthName(), self.intYear)
        print(f"{dateString: ^27}")

        print("Sun Mon Tue Wed Thu Fri Sat")

        
        for count in range(self.returnMaxDay()+self.firstDayOfMonth()):
            if count < self.firstDayOfMonth():
                # Empty spaces for first date
                print("    ", end="")
            else:
                if (count-self.firstDayOfMonth()+1) != self.intDay:
                    print(f"{count-self.firstDayOfMonth()+1: 03}", end=" ")
                else:
                    tempString = f"{count-self.firstDayOfMonth()+1:0>2}"
                    print(f"[{tempString}]", end="")

                if (count+1) % 7 == 0:
                    print()


        sys.stdout = old_stdout
        output = new_stdout.getvalue()
        
        return output

    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Returns day of the week for first day of the month.
    # Parameters: Nothing
    # Output: First day of the month.
    def firstDayOfMonth(self):
        month = self.intMonth
        year = self.intYear
        
        month = self.intMonth
        year = self.intYear
        
        m = month - 2
        y = year
        if m <= 0:
            m = m + 12
            y = y - 1

        p = y // 100
        r = y % 100

        firstDay = (1 + (26 * m - 2) // 10 + r + r // 4 + p // 4 + 5 * p) % 7

        return firstDay
    
    # Author: Gavin Xiong
    # Date: 2022/04/23
    # Purpose: Calculates the day of the year.
    # Parameters: Nothing
    # Output: Day of the year.
    def dayOfYear(self):
        day = self.intDay
        month = self.intMonth-1

        dayList     = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leapDayList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        totalDays   = 0

        if not self.returnLeapYear():                   # Check if it is leap year.
            for months in range(len(dayList)):
                if months <= month:                     # For loop up until current month.
                
                    if months == month:                 # Check whether this is your current month.
                        for days in range(day):         # Adds up until day.
                            totalDays += 1

                    else:
                        monthDays = dayList[months]     # Gets month from list.
                        for days in range(monthDays): 
                            totalDays += 1
        else:
            for months in range(len(leapDayList)):      # Uses leap year list instead.
                if months <= month:
                    
                    if months == month:
                        for days in range(day):
                            totalDays += 1

                    else:
                        monthDays = leapDayList[months]
                        for days in range(monthDays):
                            totalDays += 1
        
        return totalDays

# SUBPROGRAMS
# Author: Gavin Xiong
# Date: 2022/04/23
# Purpose: Asks user whether to rerun the program or not.
# Parameters: Boolean value
# Output: Nothing
def rerunCheck(rerunCheck):
    rerunInput = input("Rerun? (Y/N) ")

    while rerunInput not in {"Y", "y", "N", "n"}:
        print("Error: Y/N only.")
        rerunInput = input("Rerun? (Y/N) ")

    if rerunInput not in {"Y", "y"}:
        rerunCheck  = False

    for count in range(30):
        print()

# MAIN
loopCheck = True

while loopCheck:
    userDate = Date().getDate()
    userDate.displayCalendar()

    rerunCheck(loopCheck)