import hashlib

flag = 0
counter = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("file name : ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

  for word in pass_file:

  enc_wrd = word.ecncode('utf-8');
  digest = hashlib.md5(enc_wrd.strip()).hexdigest()
 #print(word)
 #print(digest)
 #print(pass_hash)

 counter += 1

if digest == pass_hash:
   print("password found")
   print("password is " + word)
   flag = 1
   break

if flag == 0:
print("password/passphrase is not in the list")