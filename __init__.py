from mycroft import MycroftSkill, intent_file_handler


class Robbie(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('robbie.intent')
    def handle_robbie(self, message):
        self.speak_dialog('robbie')


def create_skill():
    return Robbie()

