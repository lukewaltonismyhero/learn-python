from hashlib import md5
"""
Rule #1: Keep it fun

* Our goal is to learn how to open files.  
* Once we can open files we have all of  the power required to *BREAK PASSWORDS*

Use your new found power for good!
"""
password = 'things'
salt = 'mysalt'

combined_password = password + salt

print "Combined password: {}".format(combined_password)

encrypted_string = md5(password + salt).hexdigest()

print "Encrypted Password: {}".format(encrypted_string)