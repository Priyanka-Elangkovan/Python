#a program that prints numbers from 1 to 100. # Loop For
#However, for multiples of 3, print "Fizz" instead of the number, and
#for multiples of 5, print "Buzz."
#For numbers that are multiples of both 3 and 5, print "FizzBuzz.

i=1
for i in range(101):
    #print (i)
    if not(i%5 or i%3):
        #print(f"inside the loop {i}i")
        print("FizzBuzz")
    elif not(i%5):
        #print(f"inside the loop {i}i")
        print("Buzz")
    elif not (i % 3):
        # print(f"inside the loop {i}i")
            print("Fizz")
    else:
        print(i)
    i+=1