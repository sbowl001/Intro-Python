# Use open to open file "foo.txt" for reading

file = open('foo.txt', 'r')
# Print all the lines in the file

for line in file:
    print(line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
file.write("Hi\n")
file.write("This is\n")
file.write("a new line")

# Close the file
file.close()