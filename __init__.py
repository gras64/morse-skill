from mycroft import MycroftSkill, intent_file_handler


class Morse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('morse.intent')
    def handle_morse(self, message):
        self.speak_dialog('morse')


def create_skill():
    return Morse()

