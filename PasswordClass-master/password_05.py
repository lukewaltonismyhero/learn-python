from crypt import crypt

"""
And now the password dictionary attack begins!
"""
attack_list = []
identified_target_list = []
combined_filename = "my_new_passwords_combined.txt"
attack_filename = "./targets/little_guy.txt"

# tricky!  What is different? What does it mean?
read_this_file = open(combined_filename)

print "\nInitializing the attack list:"

# New hotness: .split() & .rstrip()
# What are we doing?!
for line in read_this_file:
    (plaintext, encrypted) = line.split(";")
    print "plaintext: {}\t encrypted: {} added to attack list".format(plaintext, encrypted.rstrip())
    attack_list.append((plaintext, encrypted.rstrip()))
read_this_file.close()

# At this point can you tell me what the attack list looks like?


# Identify targets  
print "\nIdentify the targets:"

# Open the file and read in the users we're going to attack
attack_this_file = open(attack_filename, 'r')
for line in attack_this_file:
    (user, uid, encrypted_password) = line.rstrip().split(":")
    print "user:{}\tuid:{}\tpw:{}".format(user, uid, encrypted_password)
    # Add the target to our list
    identified_target_list.append((user, encrypted_password))

# Always close the file!
attack_this_file.close()

# Attack the targets
print "\nInitiate Attack Sequence ... 40 years in the making!\n"
for target in identified_target_list:
    (user, target_password) = target

    # Check passwords
    for word in attack_list:
        (attack_word_plaintext, attack_word_encrypted) = word
        if target_password == attack_word_encrypted:
            print "Target identified! user:{}\tpassword:{}".format(user, attack_word_plaintext)

