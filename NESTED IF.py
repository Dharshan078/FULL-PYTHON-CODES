"""
IF A LOOP HAS MORE THAN ONE "IF" INSIDE A "IF" LOOP ITS CALLED AS NESTED IF LOOP
EX1:    THREE SUBJECTS WITH PASS MARK 50
        FIND TOTAL, AVERAGE
        GRADE   90-100 A
                80-89  B
                70-79  C
                50-69  D
                BELOW  FAIL
"""
subject1=int(input("ENTER THE MARK OF SUBJECT 1 : "))
subject2=int(input("ENTER THE MARK OF SUBJECT 2 : "))
subject3=int(input("ENTER THE MARK OF SUBJECT 3 : "))
total=subject1+subject2+subject3
print("TOTAL MARKS =",total)
average=total/3
print("YOUR AVERAGE =",average)
if subject1>=50 and subject2>=50 and subject3>=50:
    print("YOU HAVE PASSED!")
    if average>=90 and average<=100:
        print("CONGRATULATIONS YOU HAVE SECURED A GRADE")
    elif average>=80 and average<=89:
        print("CONGRATULATIONS YOU HAVE SECURED B GRADE")
    elif average>=70 and average<=79:
        print("CONGRATULATIONS YOU HAVE SECURED C GRADE")
    elif average>=50 and average<=69:
        print("CONGRATULATIONS YOU HAVE SECURED D GRADE")
else:
    print("SORRY YOU FAILED")
    print("BETTER LUCK NEXT TIME")
