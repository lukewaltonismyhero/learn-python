from hashlib import md5
"""
Serious business ...
We're going to write a plaintext password, and an encrypted password
"""

passwords_of_good = ["burrito", "Burrito", "pickle", "cashew", "laser", "Python"]
combined_filename = "my_new_passwords_combined.txt"
salt = "saltysaltgoodness"

print "\nGoing to write the file \"{}\"".format(combined_filename)
combined_file = open(combined_filename, "w")

# Something we're used to
for word in passwords_of_good:
    encrypted_result = md5(word + salt).hexdigest()
    print "word: {}\t\tencrypted: {}".format(word, encrypted_result)
    combined_file.write("{};{}\n".format(word, encrypted_result))

# Close the file
combined_file.close()


"""
Take that and rewind it back!
Now that we've grabbed a file, let's open it read only and display the results.
Not just display the results, let's display it like an adult!
"""

print "\nNow we're opening our file and reading it out:\n"

# tricky!  What is different? What does it mean?
read_this_file = open(combined_filename)

# New hotness: .split() & .rstrip()
# What are we doing?!
for line in read_this_file:
    (plaintext, encrypted) = line.split(";")
    print "plaintext: {}\t encrypted: {}".format(plaintext, encrypted.rstrip())

read_this_file.close()