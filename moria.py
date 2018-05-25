#!/usr/bin/env python

"""Moria.py: Solution to root-me.org challenge "Go back to College" 
 https://www.root-me.org/en/Challenges/Programming/Go-back-to-college-147 ."""

__author__      = "Tano Mattioli"
__copyright__   = "Copyleft 2018, Planet Earth?"

import platform
import random
import socket
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

server = "irc.root-me.org"
channel = "#root-me_challenge"
botnick = "Moria" + str(random.randint(1, 10000))
sentUser = False
sentNick = False

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket connection
print "\nConnecting to:" + server
irc.connect((server, 6667))

try:
   x = 1
   y = 1
   while 1:
      text = irc.recv(2048)
      if len(text) > 0:
         print text
      else:
         continue

      if text.find("PING") != -1:
         irc.send("PONG " + text.split()[1] + "\n")

      if text.find("PRIVMSG") != -1:
      	 if y == 1:
      	 	nums = text.split()[-3:] #Convert the answer into a list and take the las 3 objects (num1 slash num2)
      	 	num1 = int(nums[0][1::]) #number 1 - The first character is a ':' that takes it out.
      	 	num2 = int(nums[2]) #number 2
      	 	result = round(((num1**0.5) * num2), 2) #Square Root of the first number multiplied by the second one rouded 2 decimals.
      	 	irc.send(str.encode("PRIVMSG Candy !ep1 -rep " + str(result) + "\n")) #MAGIC!
      	 	y =- 1
      	 else:
      	 	print "HACKED\n"
      	 	sys.exit()

      if sentUser == False:
         irc.send("USER " + botnick + " " + botnick + " " + botnick + " :This is NOT a fun bot\n")
         sentUser = True
         continue

      if sentUser and sentNick == False:
         irc.send("NICK " + botnick + "\n")
         sentNick = True
         continue

      if text.find("255 " + botnick) != -1:
         irc.send("JOIN " + channel + "\n")

      if text.find(":!host") != -1:
         irc.send("PRIVMSG " + channel + " :" + str(platform.platform()) + "\n")

      while x == 1:
      	 irc.send(str.encode("PRIVMSG Candy !ep1" + "\n"))
      	 x =- 1

except KeyboardInterrupt:
   irc.send("QUIT :Sorry, my master needs me!\n")
   print "\n"
   sys.exit()