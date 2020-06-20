Feature: morse

    Scenario: morse last answer
        Given an english speaking user
        When the user says "how are you"
        Then "mycroft-hello-world" should reply with dialog from "how.are.you.dialog"
        And the user replies "can you morse"
        Then mycroft should send the message "recognizer_loop:audio_output_start"

    Scenario: morse a sentence
        Given an english speaking user
        When the user says "morse the sentence hello world"
        Then mycroft should send the message "recognizer_loop:audio_output_start"

    Scenario: morse with ask sentence
        Given an english speaking user
        When the user says "morse the sentence"
        Then "morse-skill" should reply with dialog from "tell.text.dialog"
        And the user replies "hello world"
        Then mycroft should send the message "recognizer_loop:audio_output_start"