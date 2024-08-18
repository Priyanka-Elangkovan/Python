num= input("Enter the number you want tables until 10 :")
num= int(num)

print(f"The tables for the number {num} is " )
i=int(1)
while i<11 :
    print(f"{num}*{i} = {num*i}")
    i=i+1
print("end")