import speech_recognition
import pyttsx3

engine = pyttsx3.init()

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Say something: ")
    engine.say("Say something")
    engine.runAndWait()
    while True:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        print("You said: ", end = "")
        print(recognizer.recognize_google(audio))

        words = recognizer.recognize_google(audio)
        if "hello" in words:
            print("Bot: Hello to you too!")
            engine.say("Hello to you too!")
        elif "how are you" in words:
            print("Bot: I'm Good, thank you!")
            engine.say("I'm Good, thank you!")
        elif "who are you" in words:
            print("Bot: My name is Bob. I'm just a bot!")
            engine.say("My name is Bob. I'm just a bot!")
        elif "bye" in words:
            print("Bot: Bye, see you later!")
            engine.say("Bye, see you later!")
            engine.runAndWait()
            exit()
        else:
            print("Bot: I can't understand what you're saying..")
            engine.say("I can't understand what you're saying..")

        engine.runAndWait()
        print("Say something: ")