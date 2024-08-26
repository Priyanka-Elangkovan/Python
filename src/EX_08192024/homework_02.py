#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
#determine if the triangle is equilateral (all sides are equal),
#isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.


print("enter three sides of the triangle as a,b,c")
a=int(input("enter a :"))
b=int(input("enter b :"))
c=int(input("enter c :"))

if a==b and b==c :
    print("Triangle is an Equilateral triangle")
elif a == b or c == a or b == c:
    print("Triangle is an isosceles triangle")
else:
    print("Triangle is an scalene triangle")
