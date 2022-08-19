""" Write a python script which takes a three digit number from the user
and displays only its first digit."""

x = int(input("Enter three digit number: "))
x //= 100
print("First digit is:",x)
