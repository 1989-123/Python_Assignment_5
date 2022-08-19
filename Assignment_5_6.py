""" Write a python script which takes a three digit number from the user
and displays only its middle digit."""

x = int(input("Enter a three digit number: "))
y = x % 10
x //= 10
y = x % 10
print("Middle digit is:",y)
