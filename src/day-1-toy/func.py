# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

def is_even(num):
    if int(num) % 2 == 0:
        return "Even!"
    else:
        return "Odd"
print(is_even(num)) 
# Print out "Even!" if the number is even. Otherwise print "Odd"