from sys import argv

script, filename = argv

txt = open(filename)
print "The file %s is now open" %(filename)

print "Here's your file %r:" %filename
print txt.read()
print

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print

close(filename)
print "The file %s is now closed" %(filename)



