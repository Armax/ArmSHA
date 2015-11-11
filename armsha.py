# -*- coding: utf-8 -*-
###########
# ArmSHA  #
#=========#
# v2.0.0  #
###########
import time, hashlib, random, binascii, string, os
brute = open('list.txt')
check = brute.read().split("\n")
print ("#################################")
print ("#          ArmSHA 2.0.0         #")
print ("#          developed by         #")
print ("#  @Arm4x follow me on twitter  #")
print ("#################################")
print
print ("[i] Loaded " + str(len(check)) + " password from list. For the command list write help")
print
main = "0"
while main == "0":
        command = raw_input(">>> ")
        if command == "help":
                print "ArmSHA command list"
                print "[1] Write singlehash for try to crack a single sha256 hash password"
                print "[2] Write genpass for generate a random list.txt password list"
                print "[3] Write hashlit for decrypt a hashlist.txt (must be in the same directories of armSHA)"
                print "[4] Write clear for clear the terminal screen"
                print "[5] Write quit for exit from armSHA"
                print
        if command == "genpass":
                minlan = input("Min lan. of password: ")
                maxlan = input("Max lan. of password: ")
                brute.close
                loop = 0
                npass = input("Number of password to generate: ")
                brute = open('list.txt', 'a+')
                while npass > loop:
                        prepend = ""
                        randpass=''.join(random.choice(string.letters+string.digits) for x in range(random.randint(minlan,maxlan)))
                        print ("[i] Generating pass [" + str(loop + 1) + "] "  +  str(randpass))
                
                        check = brute.read(1024).split("\n")
                        if randpass in check:
                                print "[i] Password previusly generated! Skipped..."
                        else:
                                brute.write(randpass+"\n")
                                brute.close
                                loop = loop + 1 
                print("[i] Password generation finished!")
        if command == "singlehash":
                print ("ArmSHA SHA256 cracker, Please insert the sha256 hash then press enter for start")
                password = raw_input("$SHA$")
                i = 0
                while i < len(check):
                  x = hashlib.sha256(check[i]).hexdigest()
                  print("[i] Encrypted " + check[i] + " = " + x)
                  if x == password:
                        print("[i] Cracking succesful! Password is " + check[i])
                        i = len(check) + 1
                  else:
                        print("[x] Password doesn't match")
                        i = i + 1       
        if command == "hashlist":
                print ("[i] Loading... opening list...")        
                database = open('hashlist.txt')
                db = database.read().split("\n")                        
                i = 0
                while i < len(check):
                  x = hashlib.sha256(check[i]).hexdigest()
                  print("[i] Encrypted " + check[i] + " = " + x)
                  u = 0
                  while u < len(db):
                        password = db[u]
                        print ("[i]trying to decrypt " + db[u])
                        if x == password:
                                print("[i] Cracking succesful!  Password for " +  db[u] + " is  " + check[i])
                                listcracked = open('hashcracked.txt', 'a+')
                                listcracked.write(db[u] + ":" + check[i] + "\n")
                                u = u + 1
                        else:
                                print("[x] Password isn't in the list")
                                u = u + 1
                  i = i + 1     
                                
        if command == "authme":
                print ("[i] Loading... opening database...")
                print ("[i] Purifing Authme Database...")
                yu = open("auths.db", "r")
                allp = yu.read().split("\n")
                for yu in allp:
                  if yu[0]==" ":
                          break
                  nick, hash, ip, timestamp = yu.split(":")
                  print
                  print ("Now trying to decrypt:")
                  print ("Nick: " + nick)
                  print ("Hash: " + hash)
                  print ("Ip: " + ip)
                  print ("Timestamp: " + timestamp)
                  print 
                  print ("Inizialising...")
                  time.sleep(3)
                
                  i = 0
                  if (hash[0]=="$")and(hash.split("$")[1]=="SHA"):
                    while i < len(check):
                      salt = hash.split("$")[2]
                      password = hash.split("$")[3]
                      x = hashlib.sha256(hashlib.sha256(check[i]).hexdigest()+salt).hexdigest()
                      print("[i] Encrypted " + check[i] + " = " + x)
                          
                      print ("[i]trying to decrypt " + password)
                      if x == password:
                        print("[i] Cracking succesful!  Password for " +  hash + " is  " + check[i])
                        listcracked = open('hashcracked.txt', 'a+')
                        listcracked.write(nick + ":" +  hash + ":" +  check[i] + "\n")
                                   
                      else:
                        print("[x] Password doesn't match")
                                         
                      i = i + 1
        if command == "quit":
                print("\n[i] Quitting from ArmSHA...")
                main = "quitted"
        if command == "clear":
                print ("\n" * 100)
                os.system ("clear")
                print ("#################################")
                print ("#          ArmSHA 2.0.0         #")
                print ("#          developed by         #")
                print ("#  @Arm4x follow me on twitter  #")
                print ("#################################")
                print
                print ("[i] Loaded " + str(len(check)) + " password from list. For the command list write help")
                print

