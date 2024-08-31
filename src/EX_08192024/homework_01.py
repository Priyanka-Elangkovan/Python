#Create a program that determines whether a given year is a leap year.
#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.

num1= input("Enter a year:\n")
num1=int(num1)

#check if the year is leap year

if num1%4 == 0:
    if num1%100 ==0:
        #print("num is div by 100")
        if num1%400 ==0 :
           #print("no. div by 400")
           print(f"year {num1} is a leap year")

        else:
            #print("num is not div by 400")
            print(f"year {num1} is not a leap year")
    else :
        print(f"year {num1} is a leap year")
else :
    print(f"year {num1} is not a leap year")
