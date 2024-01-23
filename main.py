import pyttsx3
from langdetect import detect
from perplexity import Perplexity

perplexity = Perplexity("fanechlucas@gmail.com")
answer = perplexity.search("What is the weather like today?")
response = ""
for a in answer:
    response += a['answer']

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