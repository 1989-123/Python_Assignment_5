""" Write a python script which takes a three digit number from the user
and displays only its last digit. """

x = int(input("Enter a three digit number: "))
y = x % 10
print("Last digit is:",y)
