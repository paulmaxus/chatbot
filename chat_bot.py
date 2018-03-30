import sys
sys.path.append('./aiml')
import time

import aiml
k = aiml.Kernel()
k.learn('chat_bot.aiml')

# log file
logfile = open("log.txt", 'a')
logfile.write(time.strftime("%a,%d %b %Y %H:%M:%S\n"))
logfile.flush()

inapp = 0
turns = 0

print("------------------------------------------------------------------------")
print("-------------------------- INSTRUCTIONS --------------------------------")
print("------------------------------------------------------------------------")
print("--- Type exit to quit --------------------------------------------------")
print("--- Type ! if an answer by the chat bot seems inappropriate ------------")
print("------------------------------------------------------------------------")

user = input(">")

while(user != "exit"):
	if user != "!":
		logfile.write("U: "+str(user)+"\r")
		turns += 1
		agent = k.respond(user)
		print(agent)
		turns += 1
		user = input(">")
		logfile.write("S: "+str(agent)+"\r")
	else:
		logfile.write("--- Above statement is inappropriate"+"\r")
		inapp += 1
		user = input(">")
	logfile.flush()

print("------------------------------------------------------------------------")
print("------------------------------- RATING ---------------------------------")
print("------------------------------------------------------------------------")
print("--- Tell us how much you liked communicating with this chat bot --------")
print("--- You can type in integer values from 1 to 5 -------------------------")
print("------------------------------------------------------------------------")
print("--- 5: you were maximally satisfied ------------------------------------")
print("--- 1: you did not like it at all --------------------------------------")
print("------------------------------------------------------------------------")
rating = input(">")
print("------------------------------------------------------------------------")
print("------------------------------ THANK YOU -------------------------------")
print("------------------------------------------------------------------------")

logfile.write("-----------------------------------------------------------------------------------"+"\r")
logfile.write("--- Number of inappropriate utterances: "+str(inapp)+" -----------------------------------------"+"\r")
logfile.write("--- Number of turns: "+str(turns)+" -----------------------------------------------------------"+"\r")
logfile.write("--- Rating: "+str(rating)+" ---------------------------------------------------------------------"+"\r")
logfile.write("-----------------------------------------------------------------------------------"+"\r")
logfile.close()
