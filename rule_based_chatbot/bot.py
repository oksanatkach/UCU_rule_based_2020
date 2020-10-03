import re
import random
from rule_based_chatbot.flight import process_flight


class Bot:
    def __init__(self):
        self.bot = 'Bot: '
        self.user = 'You: '
        self.launch()

    def first_meeting(self):
        return "Hi, welcome! How can I help you?"

    def hello_response(self):
        answers = []
        return random.choice(answers)

    def goodbye_response(self):
        answers = []
        return random.choice(answers)

    def get_response(self, user_text):

        #@todo: check if the user wants to book a flight; if yes, call the flight function

        return "I don't know what to say."

    def launch(self):
        print(self.bot + self.first_meeting())

        user_text = input(self.user)
        while user_text != '\exit':
            response = self.get_response(user_text)
            print(self.bot + response)
            user_text = input(self.user)
        print(self.goodbye_response())


if __name__=='__main__':
    Bot()
