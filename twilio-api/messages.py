#!/bin/python
from twilio.rest import *
from datetime import datetime, timezone
import config

class Messages:
    #setup Twilio
    client = Client(config.account['account_sid'], config.account['auth_token'])


##### Prints all messages for no good reason #####
    def readAllMessages(self):
        messages = self.client.messages.list()

        for record in messages:
            message = self.client.messages(record.sid).fetch()
            print(message.body, message.date_created)


##### This function returns a single conversation between the account holder and another individual #####
    def returnSingleThread(self, number, accountNumber):
        messagesFrom = self.client.messages.list(from_=number, to=accountNumber)
        messagesTo = self.client.messages.list(from_=accountNumber, to=number)

        messagesFromCount = 0
        messagesToCount = 0
        messages = []

        for message in messagesFrom:
            messages.append([message.to, message.from_, message.body, message.date_created.replace(tzinfo=timezone.utc).astimezone(tz=None)])

        for message in messagesTo:
            messages.append([message.to, message.from_, message.body, message.date_created.replace(tzinfo=timezone.utc).astimezone(tz=None)])

        messages.sort(key=lambda messages: messages[3])
        return messages

##### This function returns a list of conversation - this is used to display the list for the user to choose #####
    def returnThreadList(self, number, accountNumber):
        return "thread"


##### Send a single message and return it's result #####
    def sendMessage(self, sender, recipient, message):
        self.client.messages.create( body=message, from_=sender, to=recipient)
        return True


        #print(totalMessages)
        #for message in messagesTo:
            #print(message)
            #print(message.body, message.date_created)

        #for message in messagesFrom:
            #print(message.body, message.date_created)
