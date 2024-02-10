import pyttsx3
from langdetect import detect
from perplexity import Perplexity
import speech_recognition as sr
# activation word: "rio" or "Rio"
activation_word = "rio"
activation_word_caps = activation_word.capitalize()
print("Activation word:", activation_word)

# Initialise le recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Dites quelque chose :")
    audio = r.listen(source)

    try:
        # Utilise Google Speech Recognition pour convertir l'audio en texte
        user_input = r.recognize_google(audio, language='en-US')
        if activation_word or activation_word_caps in user_input:
            print("Activation détectée.")
            # remove what is before the activation word from the user input
            if activation_word in user_input:
                user_input = user_input.split(activation_word, 1)[1]
                # remove the activation word from the user input
                user_input = user_input.replace(activation_word, "")
            if activation_word_caps in user_input:
                user_input = user_input.split(activation_word_caps, 1)[1]
                # remove the activation word from the user input
                user_input = user_input.replace(activation_word_caps, "")

            print("Vous avez dit : " + user_input)
            perplexity = Perplexity("fanechlucas@gmail.com")
            answer = perplexity.search(user_input)
            response = ""
            for a in answer:
                if a["status"] == "completed":
                    print(a)
                    response = a['answer']
                    break

            # Remove "*" from the response
            response = response.replace("*", "")
            # Loop through the response and remove every [ and ] and everything in between them
            while "[" in response:
                start = response.index("[")
                end = response.index("]")
                response = response[:start] + response[end+1:]

            # Print the response
            print(response)
            # Initialiser le moteur de synthèse vocale
            engine = pyttsx3.init()

            # Détecter la langue du texte
            langue = detect(response)
            print("Langue choisie:", langue)
            # Changer la langue du moteur de synthèse vocale
            engine.setProperty('voice', langue)  # Utilise la langue détectée

            # Convertir le texte en discours
            engine.say(response)

            # Reproduire le discours
            engine.runAndWait()
            perplexity.close()

    except sr.UnknownValueError:
        print("Google Speech Recognition n'a pas pu comprendre l'audio")
    except sr.RequestError:
        print("Impossible de contacter Google Speech Recognition")