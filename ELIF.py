"""
IF ELIF STATEMENT IN PYTHON
IF ELIF Statement is used for decision-making operations
IT SAME AS IF ELSE BUT WE CAN USE MULTIPLE CONDITIONS HERE
EX 1: FINE FOR LIBRARY BOOK SUBMISSION
IF  0-5 DAYS NO FINE
    5-10 DAYS 1RS FINE
    10-20 DAYS 5RS FINE
    20-30 DAYS 10RS FINE
    AFTER 30 DAYS MEMBERSHIP CANCEL
"""
days=int(input("ENTER THE NUMBER OF DAYS : "))
if (days>=0 and days<=5):
    print("NO FINE FOR ",days," DAYS")
elif (days>5 and days<=10):
    print("FINE AMOUNT FOR",days,"IS",days*1,"RUPEES")
elif (days>10 and days<=20):
    print("FINE AMOUNT FOR", days, "DAYS IS", days*5, "RUPEES")
elif (days>20 and days<=30):
    print("FINE AMOUNT FOR", days, "DAYS IS", days * 10, "RUPEES")
else:
    print("NO MEMBERSHIP FOR AFTER",days,"DAYS")



