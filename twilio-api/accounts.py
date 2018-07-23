#!/bin/python
from twilio.rest import *

class Accounts:
    #setup Twilio
    account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    client = Client(account_sid, auth_token)

    def returnActiveNumbers(self):
        accountNumbers = self.client.incoming_phone_numbers.list()

        numbers = []

        for number in accountNumbers:
            numbers.append(number.phone_number)
        return numbers
