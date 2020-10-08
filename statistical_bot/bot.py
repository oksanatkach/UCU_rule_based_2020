import dialogflow
import os
import random


class Bot:
    def __init__(self):
        self.bot = 'Bot: '
        self.user = 'You: '
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ucu-test-ceriuu-5ece8310f3bc.json'
        self.DIALOGFLOW_PROJECT_ID = 'ucu-test-ceriuu'
        self.LANG_CODE = 'en'
        self.SESSION_ID = 'me'
        self.launch()

    def check_intent(self, text2analyze):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.DIALOGFLOW_PROJECT_ID, self.SESSION_ID)
        text_input = dialogflow.types.TextInput(text=text2analyze, language_code=self.LANG_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.intent.display_name, response

    def first_meeting(self):
        return "Hi, welcome! How can I help you?"

    def respond_greetings(self):

        answers = [
            'Hey! Happy to see you again! How can I help you?',
            "Woow, it's amazing that you get in touch! What do you wanna do today?",
            "Hey there! What about our plans for today?",
            "Hello! Is there anything I can help you with?",
            "Hey heeey! I'm ready to help!",
            "Nice to see you here. Is there something you'd like to talk about?"
            "Hi! I'm so happy when you come back here. Anything you want to chat about?"
            "Hey there! What can I do to help you today?"
        ]
        return random.choice(answers)

    def get_response(self, user_text):
        intent, response = self.check_intent(user_text)
        if intent == 'book_flight':
            return
        return response

    def goodbye_response(self):
        answers = [
            "Goodbye! Hope to see you again)",
            "Bye bye, see you soon",
            "It's all for today! See ya",
            "Have a nice day! See you soon",
            "It was pretty interesting chat! Bye bye",
            "Amazing work for today! See you tomorrow",
            "Good work! Talk to you later",
        ]
        return random.choice(answers)

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
