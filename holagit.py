
import speech_recognition as sr
import pyttsx3
#import pyaudio

#Inicializar el motor de texto a voz
engine = pyttsx3.init()

#Inicializar el reconocimiento de coz
recognizer = sr.Recognizer()

#Establecer la voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Funcion para que el asistente responda
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Main loop
while True:
    #Escuchar al usuario
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)

    try:
        #Transcribir de texto a voz
        text = recognizer.recognize_google(audio)
        print("Has dicho: ", text)

        #procesar las peticiones del usuario 
        if "hola " in text:
            speak("¡Hola! ¿Como estas?")
        elif"adios" in text:
            speak("¡Hasta luego!")
            break

    except sr.UnknownValueError:
        print("No se ha entendido lo que has dicho")
    except sr.RequestError:
        print("Error en la transcripción")


#print("hola python")
