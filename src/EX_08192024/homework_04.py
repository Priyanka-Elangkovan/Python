#Factorial n= 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

a= int(input("enter the number you wanted the factorial to"))
i=1
result=1
for i in range(1,a+1):
    result = result*i
print(result)
