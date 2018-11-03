# Analysis worksheet problem III by vincenzo scotto di uccio

course = int(input("Please enter the credits amount this course is: "))
grade = int(input(" Please enter the grade you got in that class 1-4 is d-a respectively: "))

a = 4
b = 3
c = 2
d = 1

if grade == a:
    print ("Your gpa is: ", course * grade / course)
    
if grade == b:
    print ("Your gpa is: ", course * grade / course)

if grade == c:
    print ("Your gpa is: ", course * grade / course)
if grade == d:
    print ("Your gpa is: ", course * grade / course)
if grade !=a or grade !=b or grade !=c or grade !=d:
    print ("Error")
    
    
