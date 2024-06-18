import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    """Process recognized voice command"""
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif command.startswith("play"):
        song = command.split(" ", 1)[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
    elif "stop" in command:
        speak("Goodbye!")
        return False
    return True

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            # Use the microphone as the source for input
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                # Recognize the speech using Google Web Speech API
                word = recognizer.recognize_google(audio).lower()
                if "jarvis" in word:
                    speak("Yes my lord")
                    print("Jarvis active...")
                    
                    # Listen for the next command
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        print("Listening for your command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        try:
                            command = recognizer.recognize_google(audio).lower()
                            print(f"You said: {command}")
                            if not process_command(command):
                                break
                        except sr.UnknownValueError:
                            speak("Sorry, I didn't catch that.")
                            print("Could not understand the audio")
                        except sr.RequestError as e:
                            speak("Sorry, I'm having trouble connecting to the internet.")
                            print(f"Could not request results from Google Speech Recognition service; {e}")
        
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
