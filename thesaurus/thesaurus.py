import json
from difflib import get_close_matches

## a esta aplicacion le falta evitar que pregunte si o no
## ademas de eliminar los corchetes y colocar cada sinonimo por separado

data = json.load(open('thesaurus/data.json','r')) ## Es un dictionary del internet

def thesaurus(text):
    text = text.lower()
    if text in data:
        return data[text][0] # esta es una opcion para obtener sin corchetes pero eliminas las demas, a lo mejor en view con el bucle for
    elif text.title() in data:
        return data[text.title()]
    elif text.upper() in data:
        return data[text.upper()]
    elif len(get_close_matches(text, data.keys())) > 0:
        return data[get_close_matches(text, data.keys())[0]]
    else:
        return "Word does not exist. Please double check it."