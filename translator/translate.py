from googletrans import Translator

def translater(text):
    translator = Translator()
    translation = translator.translate(text=text, dest='de')
    return translation.text