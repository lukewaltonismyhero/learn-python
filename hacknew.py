#encryption libraries
from hashlib import md5
from hashlib import sha256
from base64 import standard_b64encode

#def salt
salt = "saltysaltgoodness"

#def plaintext
plaintext_filename = "british-english"
plaintext_file = open(plaintext_filename, "r")


#def encrypt text for md5 encryption
md5_encrypted_filename = "md5.txt"
md5_encrypted_file = open(md5_encrypted_filename, "w")

#def encrypt text for md5 encryption
sha256_encrypted_filename = "sha256.txt"
sha256_encrypted_file = open(sha256_encrypted_filename, "w")

#def encrypt text for md5 encryption
b64_encrypted_filename = "b64.txt"
b64_encrypted_file = open(b64_encrypted_filename, "w")

#def combined files
md5_combined_filename = "md5_comb.txt"
sha256_combined_filename = "sha256_comb.txt"
b64_combined_filename = "b64_comb.txt"

md5_combined_file = open(md5_combined_filename, "w")
sha256_combined_file = open(sha256_combined_filename, "w")
b64_combined_file = open(b64_combined_filename, "w")

#encrypt plaintext and put results into encrypted text for md5 encryption
for word in plaintext_file:
    encrypted_result = md5(word + salt).hexdigest()
    #print "word : {}\t\tencrypted: {}".format(word, encrypted_result)
    md5_combined_file.write("{};{}\n".format(word.rstrip(), encrypted_result))

#encrypt plaintext and put results into encrypted text for sha256 encryption
for word in plaintext_file:
    encrypted_result = sha256(word + salt).hexdigest()
    #print "word : {}\t\tencrypted: {}".format(word, encrypted_result)
    sha256_combined_file.write("{};{}\n".format(word.rstrip(), encrypted_result))
	
#encrypt plaintext and put results into encrypted text for md5 encryption
for word in plaintext_file:
    encrypted_result = standard_b64encode(word + salt).hexdigest()
    #print "word : {}\t\tencrypted: {}".format(word, encrypted_result)
    b64_combined_file.write("{};{}\n".format(word.rstrip(), encrypted_result))
	
#close files
plaintext_file.close()
md5_encrypted_file.close()
sha256_encrypted_file.close()
b64_encrypted_file.close()
md5_combined_file.close()
sha256_combined_file.close()
b64_combined_file.close()

#open combined files
md5_combined_file = open(md5_combined_filename, "r")
sha256_combined_file = open(sha256_combined_filename, "r")
b64_combined_file = open(b64_combined_filename, "r")

#set up attack and target lists
md5_attack_list = []
sha256_attack_list = []
b64_attack_list = []
identified_target_list = []
attack_filename = "big_guy.txt"

#format md5 encrypted words for comparison
for line in md5_combined_file:
    (plaintext, encrypted) = line.split(";")
    md5_attack_list.append((plaintext, encrypted.rstrip()))
md5_combined_file.close()

#format sha256 encrypted words for comparison
for line in sha256_combined_file:
    (plaintext, encrypted) = line.split(";")
    sha256_attack_list.append((plaintext, encrypted.rstrip()))
sha256_combined_file.close()

#format standard_base64 encrypted words for comparison
for line in b64_combined_file:
    (plaintext, encrypted) = line.split(";")
    b64_attack_list.append((plaintext, encrypted.rstrip()))
b64_combined_file.close()


#take away uid
attack_this_file = open(attack_filename, 'r')
for line in attack_this_file:
    (user, uid, encrypted_password) = line.rstrip().split(":")
    # Add the target to our list
    identified_target_list.append((user, encrypted_password))

#close attack file
attack_this_file.close()

#ATTACK!!!
for target in identified_target_list:
    (user, target_password) = target
	
#check md5 passwords
    for word in md5_attack_list:
        (attack_word_plaintext, attack_word_encrypted) = word
        if target_password == attack_word_encrypted:
            print "Target identified! user:{}\tpassword:{}".format(user, attack_word_plaintext)

#check sha256 passwords
    for word in sha256_attack_list:
        (attack_word_plaintext, attack_word_encrypted) = word
        if target_password == attack_word_encrypted:
            print "Target identified! user:{}\tpassword:{}".format(user, attack_word_plaintext)			

#check b64 passwords
    for word in b64_attack_list:
        (attack_word_plaintext, attack_word_encrypted) = word
        if target_password == attack_word_encrypted:
            print "Target identified! user:{}\tpassword:{}".format(user, attack_word_plaintext)
