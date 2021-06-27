import speech_recognition as sr
from playsound import playsound 
from gtts import gTTS
import datetime
from nlp import Nlp


class VoiceRecognition:

    def __init__(self, gui=None):
        self.prompt_limit = None
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.nlp = Nlp()
        self.gui = gui

    def run(self):
        self.wish_me()
        while True:
            response = self.recognize_speech_from_mic()
            print(response)
            if response['transcription'] == None:
                continue
            #self.nlp.gui_launcher(response['transcription'], self.gui)
            self.nlp.other_launcher(response['transcription'])
            self.nlp.query(response['transcription'])

    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            text = "Good Morning! "
        elif hour>=21 and hour<18:
            text = "Good Afternoon! "
        else:
            text = "Good Evening! "

        text += "sir, how may I help you?"
        self.speak(text)

    def speak(self, text):
        Message = text
        speech = gTTS(text = Message)
        speech.save('./data/sound.mp3')
        playsound('./data/sound.mp3')

    def recognize_speech_from_mic(self):
        """Transcribe speech from recorded from `self.microphone`.
    
        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                   successful
        "error":   `None` if no error occured, otherwise a string containing
                   an error message if the API could not be reached or
                   speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                   otherwise a string containing the transcribed text
        """
        # check that self.recognizer and self.microphone arguments are appropriate type
        if not isinstance(self.recognizer, sr.Recognizer):
            raise TypeError("`self.recognizer` must be `Recognizer` instance")
    
        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`self.microphone` must be `Microphone` instance")
    
        # adjust the self.recognizer sensitivity to ambient noise and record audio
        # from the self.microphone
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
    
        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
    
        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = self.recognizer.recognize_google(audio, language="en-in")
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
    
        return response

