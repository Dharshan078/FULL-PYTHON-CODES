"""
IT IS SAME AS FOR LOOP
BUT WE CAN USE MANY FOR LOOPS UNDER ONE FOR LOOP FOR SOME CERTAIN CONDITION IN THE PROBLEM
EX1: TO PRINT
*
**
***
****
*****
*****
****
***
**
*
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
ASCHI VALUE FOR A-Z(65-90) & a-z(97-122)
"""

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print("")


for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("")

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")
