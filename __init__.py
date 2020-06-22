from mycroft import MycroftSkill, intent_file_handler
import subprocess
from os.path import os, abspath, dirname
from mycroft.audio import wait_while_speaking
from mycroft.util import play_wav


class Morse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.settings["speed"] = self.settings.get('speed', 1)
        self.add_event('speak',
            self.morse_handler)
        self.save_answer = ""

    @intent_file_handler('morse.input.intent')
    def handle_morse_input(self, message):
        if message.data.get("sentence"):
            morse = message.data.get("sentence")
        else:
            morse = None
        wait_while_speaking()
        self.send_morse(morse)

    @intent_file_handler('morse.intent')
    def handle_morse(self, message):
        morse = self.save_morse
        wait_while_speaking()
        self.send_morse(morse)

    def morse_handler(self, message):
        self.save_morse = message.data['utterance']
        self.log.info('save output for morse')
    
    def send_morse(self, text=None):
        text = text.replace("'", " ")
        text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss") #convert umlautes
        if text is None:
            text = self.get_response("tell.text")
        self.log.info("morse "+text)
        if not text is None:
            subprocess.call(['python '+abspath(dirname(__file__))+'/morse.py '+
                                '-o sound '+
                                '-f '+self.file_system.path+'/morse.wav -s '+str(self.settings["speed"])+" "+text],
                                    preexec_fn=os.setsid, shell=True)
            play_wav(self.file_system.path+'/morse.wav')

def create_skill():
    return Morse()