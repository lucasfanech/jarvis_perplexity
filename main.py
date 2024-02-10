import pyttsx3
from langdetect import detect
from perplexity import Perplexity

perplexity = Perplexity("fanechlucas@gmail.com")
answer = perplexity.search("Quelle est la température à Compiègne?")
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