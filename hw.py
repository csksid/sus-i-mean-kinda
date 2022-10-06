year = int(input("Please enter the year you want to check: "))
if(year%4 == 0 and year%100 != 0 or year%400 == 0):
    print("It is a leap year!!!")
else:
    print("Nah bro bad luck, it ain't a leap year...")