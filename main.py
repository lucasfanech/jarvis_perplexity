from perplexity import Perplexity
#https://github.com/nathanrchn/perplexityai
import pyttsx3

perplexity = Perplexity("fanechlucas@gmail.com")
answer = perplexity.search("Quel est le sens de la vie?")
response = ""
for a in answer:
    response += a['answer']

print(response)
# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

# Changer la langue en français
engine.setProperty('voice', 'fr')  # Changer 'fr' par le code de la langue souhaitée

# Convertir le texte en discours
engine.say(response)

# Reproduire le discours
engine.runAndWait()
perplexity.close()