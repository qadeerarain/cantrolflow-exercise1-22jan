#Exercise 2:
#Create a program that checks if a user-inputted year is a leap year. Print the result accordingly.

year=int(input("enter a  year: "))
if year%4==0:
    print("leap year")
else:
    print("not a leap year")