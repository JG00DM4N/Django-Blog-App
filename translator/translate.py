from googletrans import Translator

def translate(text, language):
    translation = Translator()
    return translation.translate(text=text, dest=language).text