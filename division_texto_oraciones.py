#### Diviendo texto en oraciones ####
### Leer requisitos.txt 

#%% Primer Método

import nltk

#Lectura del texto original

nombre_archivo = "imperio_inca.txt"
archivo = open(nombre_archivo, "r", encoding="utf-8")
texto_real = archivo.read()
#print(texto_real)

# Se organiza el texto, reemplazando los saltos de línea por espacios.
texto_organizado = texto_real.replace("\n", " ")
#print(texto_organizado)

# Se inicializa un tokenizer NLTK. 
# útil para español
tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle") 

# Se divide el texto en oraciones:
oraciones = tokenizer.tokenize(texto_organizado)

# Se imprime el resultado. Se observan 3 oraciones, y están separadas por ','
print(oraciones)

#%% Segundo método

# También podemos usar una estrategia diferente para analizar 
# # el texto en oraciones, empleando otro paquete de PNL muy popular, spaCy.

import spacy

nombre_archivo2 = "imperio_inca.txt"
archivo2 = open(nombre_archivo2, "r", encoding="utf-8")
texto_real2 = archivo2.read()
#print(texto_real2)


texto_organizado2 = texto_real2.replace("\n", " ")
#print(texto_organizado2)

# Se inicializa el motor spaCy
nlp = spacy.load("en_core_web_sm")

# Se divide el texto en oraciones
documento = nlp(texto_organizado2)
oraciones2 = [sentence.text for sentence in documento.sents]

# Se imprime el resultado
print(oraciones2)

