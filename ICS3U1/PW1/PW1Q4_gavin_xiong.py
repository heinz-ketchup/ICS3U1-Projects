# Author: Gavin Xiong
# Date: 2022/02/20
# Purpose: Calculate 3 expressions.
# Input: N/A
# Output: Answers to the 3 expressions
# Question: PW1Q4
# _______________________________________________________________

# Initialization of variables.

# Sequence 1
product = 1 

# Sequence 2
result = 0
counter1 = 1

# Sequence 3
sum = 0
counter2 = 0
denominatorNum1 = 0
denominatorNum2 = 0

# Expression 1
for number in range(1, 21):
    product *= number

print("The result of first expression is %i." % product)
print()

# Expression 2
while counter1 <= 1000000:
    if counter1 % 2 == 0:
        result += 1/(2 * counter1 - 1)
    else:
        result -= 1/(2  * counter1 - 1)
    counter1 += 1
result *= 4

print("The result of the second expression is %0.2f." % result)
print()

# Expression 3
while counter2 < 1000000:
    denominatorNum1 += 2 * counter2 + 1
    denominatorNum2 += denominatorNum1 + 2
    sum += 1/(denominatorNum1+denominatorNum2)
    counter2 += 1

print("The result of the third expression is %0.2f." % sum)

    
