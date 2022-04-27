"""
LOOP MEANS REPEATATION OF SAME WORK AGAIN AND AGAIN
PYTHON CONSISTS OF TWO LOOPS
1.WHILE LOOP
Syntax for while loop
while condition:
2.FOR LOOP
EX 1: PRINTING ONLY EVEN NUMBERS
"""
print("EVEN NUMBERS")
b=0
while b<=200:
    print(b)
    b+=2
#WHILE WITH CONTINUE STATEMENT
#It will print the the output if it satisfies the condition and repeat itself again and again
print("EVEN NUMBERS")
b=2
while b<=200:
    if b%2!=0:
        continue
    print(b)
    b+=2

#WHILE WITH BREAK STATEMENT
#It will break the while loop if it does not satisfies the condition
"""
print("EVEN NUMBERS")
c=2
while c<=200:
    if c==12:
        c+=2
        break
    print(c)
    c+=2
"""

