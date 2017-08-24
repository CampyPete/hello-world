# Exercise 16 - Reading and Writing Files

from sys import argv

# We're going to pass the name of the Python file (script) and text file (filename)
script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# The 'w' means opening the file to 'write'.
# We could have used:
# 'a' to append
# 'r' to read - also the default if nothing is used is 'r'
# 'w+' = write plus read
# 'r+' = read plus write
# 'a+' = append plus read
print "Opening the file..."
target = open(filename, 'w')

# Truncating is going to get rid of everything inside that file
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# the "\n" is going to insert a new line character

# The original exercise uses these lines to write...
	#target.write(line1)
	#target.write("\n")
	#target.write(line2)
	#target.write("\n")
	#target.write(line3)
	#target.write("\n")

# Here is a shorter way of writing it all out...
formatter = "%r\n%r\n%r\n" %(line1, line2, line3)
target.write(formatter)

print "And finally, we close it."
target.close()

# This is one more study drill.  Open the newly changed file and read it out.
# Note that to open the file, it has to be closed (i.e. saved) first
target_again = open(filename)
print "File %r is now open." %(filename)
print target_again.read()