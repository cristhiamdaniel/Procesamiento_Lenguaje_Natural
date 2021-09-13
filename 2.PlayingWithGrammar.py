'''
Author: Cristhiam Daniel Campos Julca
Source: Python Natural Language Processing - Zhenya Antic
'''

'''
2. JUGANDO CON LA GRAMÁTICA
'''

'''
Requerimientos técnicos

pip install spacy
pip install nltk

pip install inflect
python -m spacy download en_core_web_md
pip install textacy

pip install neuralcoref
'''
#%% 2.1 Contar sustantivos - sustantivos plurales y singulares

# Módulos necesarios

import nltk
from nltk.stem import WordNetLemmatizer
import inflect 

# Lectura del texto:
filename = "Tw_paper.txt"
file = open(filename, "r", encoding="utf-8")
tw_paper = file.read()

# Organización del texto
tw_paper_org = tw_paper.replace("\n", " ")

# Token
palabras = nltk.tokenize.word_tokenize(tw_paper_org)

# Hacer parte del etiquetado del habla:
palabras_con_pos = nltk.pos_tag(palabras)

# Definir función que filtrará los sustantivos de todas las palabras:
def get_nouns(palabras_con_pos):
    noun_set = ["NN", "NNS"]
    nouns = [word for word in palabras_con_pos if 
             word[1] in noun_set]
    return nouns   

sustantivos = get_nouns(palabras_con_pos)    

# Determinar si es plural o singular

## 1ra opción
## to use the NLTK tags, where NN indicates a singular noun and NNS \
## indicates a plural noun.
def is_plural_nltk(noun_info):
    pos = noun_info[1]
    if (pos == "NNS"):
        return True
    else:
        return False

## 2da opción
## to use the WordNetLemmatizer class in the nltk.stem package. \
## The following function returns True if the noun is plural.
def is_plural_wn(noun):
    wnl = WordNetLemmatizer()
    lemma = wnl.lemmatize(noun, 'n')
    plural = True if noun is not lemma else False
    return plural

# La siguiente función cambiará un sustantivo singular en plural:
def get_plural(singular_noun):
    p = inflect.engine()
    return p.plural(singular_noun)

# La siguiente función cambiará un sustantivo plural en singular:
def get_singular(plural_noun):
    p = inflect.engine()
    plural = p.singular_noun(plural_noun)
    if (plural):
        return plural
    else:
        return plural_noun

# Ahora podemos usar las dos funciones anteriores para devolver una lista\
# de sustantivos cambiados en plural o singular, dependiendo del sustantivo original. 

def plurals_wn(palabras_con_pos):
    other_nouns = []
    for noun_info in palabras_con_pos:
        word = noun_info[0]
        plural = is_plural_wn(word)
        if (plural):
            singular = get_singular(word)
            other_nouns.append(singular)
        else:
            plural = get_plural(word)
            other_nouns.append(plural)
    return other_nouns

# Utilice la función anterior para devolver una lista de sustantivos modificados:
other_nouns_wn = plurals_wn(sustantivos)