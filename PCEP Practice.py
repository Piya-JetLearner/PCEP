"""Write a complete Python that performs the following actions:
Accept a single input from the user and convert it to an integer
If the number is even, display “That is an even number”. If it is odd, display “That is an odd number”.
If the number is negative, display “That is a negative number”. If it is zero or positive, display “That is a positive number”.
"""

a=int(input("enter a number please: "))
if a!=0 and a%2==0:
    print("That is an even number")
elif a!=0:
    print("That is an odd number")
elif a%2!=0:
    print("That is an odd number")

if a<0:
    print("This is a negative number")
else:
    print("This is a positive number")
