from mycroft import MycroftSkill, intent_file_handler
import subprocess
from os.path import os
from mycroft.audio import wait_while_speaking
from mycroft.util import play_wav, resolve_resource_file


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
        morse = message.data.get("sentence")
        wait_while_speaking()
        self.log.info("morsecode "+morse)
        #play_wav(self.piep)
        self.send_morse(morse)

    @intent_file_handler('morse.intent')
    def handle_morse(self, message):
        morse = self.save_morse
        wait_while_speaking()
        self.log.info("morsecode "+morse)
        #self.log.info(self.morse_to_wav(str(morse)))
        self.send_morse(morse)
        #self.morse_to_wav(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def morse_handler(self, message):
        self.save_morse = message.data['utterance']
        #self.save_skill = message.data['skill_id']
        self.log.info('save output for morse')
    

    def send_morse(self, text):
        subprocess.call(['python /opt/mycroft/skills/morse-skill/morse.py '+
                                '-o sound '+
                                '-f '+self.file_system.path+'/morse.wav -s '+str(self.settings["speed"])+" "+text],
                                    preexec_fn=os.setsid, shell=True)
        play_wav(self.file_system.path+'/morse.wav')        


def create_skill():
    return Morse()