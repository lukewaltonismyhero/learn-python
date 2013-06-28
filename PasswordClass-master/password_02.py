"""
Make it rain file descriptors!

Open the file, "a" means "append".  This will also create a file if one does 
not already exist.
"""
filename = "my_encrypted_passwords.txt"

# The write permission used is 'a', for "append or create if doesn't exist"
myfile = open(filename, "a")

#  Write to the file
myfile.write("Hello World\n")

# A warning:
print "Please look at the file {}".format(filename)
# Close the file
myfile.close()

# Look at how easy files really are.  We haven't done anything different.