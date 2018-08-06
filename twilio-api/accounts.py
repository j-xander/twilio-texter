#!/bin/python
from twilio.rest import *
import config

class Accounts:
    #setup Twilio
    client = Client(config.account['account_sid'], config.account['auth_token'])

    def returnActiveNumbers(self):
        accountNumbers = self.client.incoming_phone_numbers.list()

        numbers = []

        for number in accountNumbers:
            numbers.append(number.phone_number)
        return numbers
