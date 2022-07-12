# Author: Gavin Xiong
# Date: 2022/02/21
# Purpose: Display a level of success based on a mark.
# Input: A mark between 0 and 100.
# Output: The level of success.
# Question: PW1Q5
# ________________________________________________________________________________________________________

# Initilization of variables
successLevel = ""

mark = int(input("Please input the mark that you recieved from your test: "))

# Edit to make sure it is within the bounds.
while mark < 0 or mark > 100:
    print("Your number was outside the range of 0 and 100.")
    mark = int(input("Please input the mark that you recieved from your test: "))


if mark >= 0 and mark <= 39:
    successLevel = "Unsuccesful"
elif mark >= 40 and mark <= 49:
    successLevel = "Credit Recovery"
elif mark >= 50 and mark <= 59:
    successLevel = "Level 1"
elif mark >= 60 and mark <= 69:
    successLevel = "Level 2"
elif mark >= 70 and mark <= 79:
    successLevel = "Level 3"
elif mark >= 80 and mark <= 100:
    successLevel = "Level 4"

print("Your level of success based on the mark '%i' is '%s'." % (mark, successLevel))