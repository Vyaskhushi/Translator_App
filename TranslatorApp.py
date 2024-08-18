import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize the translator and recognizer
translator = Translator()
recognizer = sr.Recognizer()


# Function for speech-to-text conversion
def speech_to_text():
    with sr.Microphone() as source:
        print("Say Something to Translated")
        audio = recognizer.listen(source)
        try:
            print("Processing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError:
            print("Error with the request")
            return None

# Function to translate text into another language
def translate_text(text, target_lang):
    translated = translator.translate(text, dest=target_lang)
    print(f"Translated Text: {translated.text}")
    return translated.text


# Function to convert text into speech
def text_to_speech(text, language):
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("translated_speech.mp3")
    os.system("start translated_speech.mp3")


# Function to handle language selection
def select_language():
    languages = {
        '1': 'es',  # Spanish
        '2': 'fr',  # French
        '3': 'de',  # German
        '4': 'hi',  # Hindi
        '5': 'zh-cn',  # Chinese
        '6': 'kn',  # Kannada
        '7': 'ta',  # Tamil
        '8': 'te'  # Telugu
    }
    print("Select the language to translate to:")
    print("1. Spanish")
    print("2. French")
    print("3. German")
    print("4. Hindi")
    print("5. Chinese")
    print("6. Kannada")
    print("7. Tamil")
    print("8. Telugu")

    choice = input("Enter the number of your choice: ")
    return languages.get(choice, 'en')  # Default to English if invalid choice


# Main function to run the translator app
def translator_app():
    print("Do you want to provide input by speaking or typing?")
    mode = input("Enter 's' for speech or 't' for typing: ").lower()

    if mode == 's':
        input_text = speech_to_text()
        if not input_text:
            return
    else:
        input_text = input("Enter the text to translate: ")

    target_language = select_language()
    translated_text = translate_text(input_text, target_language)

    print("Do you want to hear the translation?")
    speak = input("Enter 'y' to hear, 'n' to skip: ").lower()

    if speak == 'y':
        text_to_speech(translated_text, target_language)


if __name__ == "__main__":
    translator_app()
