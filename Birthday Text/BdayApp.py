from twilio.rest import Client
import schedule
from datetime import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

class Recipient:
    def __init__(self, name):
        self.name = name
        self.number = input('Please enter {}\'s phone number(include +1): '.format(self.name))

        bday_inp = input('Please enter {}\'s birthday (e.x. June 06 1980): '.format(self.name))
        self.birthday = datetime.strptime(bday_inp, '%B %d %Y')
        self.birthDate = (self.birthday.month, self.birthday.day)

    def message(self):
        hbd = client.messages.create(
            body='Hi {}!. Happy birthday! <3'.format(self.name),
            from_='+12484066529',
            to=self.number
        )
    #Method for changing a recipient's phone number
    def new_number(self, num):
        self.number = num

#Dictionary with a list of birthday message recipients, with Recipient.birthDate as keys, and a list  of Recipient objects as values
Recipients = {}

def addRecipient(name):
    person = Recipient(name)
    if person.birthDate in Recipients:
        Recipients[person.birthDate].append(person)
    else:
        Recipients[person.birthDate] = [person]

def check():
    today = (datetime.today().month, datetime.today().day)
    if today in Recipients:
        for i in Recipients[today]:
            i.message()

def main():
    if __name__ == "__main__":
        schedule.run_pending()
        time.sleep(86400)