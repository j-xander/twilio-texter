#!/bin/python

#import statements
import sys
sys.path.append('./twilio-api/')
sys.path.append('./app/')

from messages import Messages
from accounts import Accounts
from main_app import App
from tkinter import *
from datetime import datetime, timezone
import time

#instaniate objects for later use
messenger = Messages()
accountNumbers = Accounts()

app = App()

##### METHODS THAT WILL PROBABLY BE MOVED #####
def printSingleThread(number, accountNumber):
    messages = messenger.returnSingleThread(number, accountNumber)

    for message in messages:
        print("")
        print(message[1])
        print(message[2])
        print(message[3].strftime("%B %d, %Y %I:%M%p %Z"))


accountNumbers = accountNumbers.returnActiveNumbers()

print(accountNumbers)

accountNumberChoice = input("Choose an account: 1-" + str(len(accountNumbers)) + " : ")
accountNumber = accountNumbers[int(accountNumberChoice)-1]

number = input("Which conversation would you like to enter? ")

printSingleThread(number, accountNumber)

if(messenger.sendMessage(accountNumber, number, input("Reply: "))):
    printSingleThread(number, accountNumber)
