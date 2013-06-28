from hashlib import md5

"""
Rule #1: Keep it fun

Our goal is to learn how to open files.  Once we can open files we have all of 
the power required to *BREAK PASSWORDS*

Use your new found power for good!
"""


"""
Serious business ...
We're going to write a plaintext password, and an encrypted password
"""

passwords_of_good = ["burrito", "Burrito", "pickle", "cashew", "laser", "Python"]
salt = "saltysaltgoodness"
plaintext_filename = "my_new_passwords_plaintext.txt"
encrypted_filename = "my_new_passwords_encrypted.txt"
#TODO both filenames

# w is for write mode
plaintext_file = open(plaintext_filename, "w") 
encrypted_file = open(encrypted_filename, "w")

# Something we're used to, this is our header
print "word:\t\tencrypted\n"

# for every password of good, let's encrypt it, and add the plain password to the
# plain file and the encrypted version in the encrypted file
for word in passwords_of_good:
    encrypted_result = md5(word + salt).hexdigest()
    print "word : {}\t\tencrypted: {}".format(word, encrypted_result)
    plaintext_file.write("{}\n".format(word))
    encrypted_file.write("{}\n".format(encrypted_result))

# Close the file
plaintext_file.close()
encrypted_file.close()