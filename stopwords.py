# Eliminación de STOPWORDS

# Importamos los módulos necesarios
import csv
import nltk

# Lectura de los stopwords en inglés

csv_file="stopwords.csv"

# Primer método
with open(csv_file, 'r', encoding='utf-8') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    stopwords = [row[0] for row in reader]

#print(type(stopwords))


# Forma alterna usando NLTK
stopwords_2 = nltk.corpus.stopwords.words('english') 


### Ejemplo práctico ###

#Lectura del archivo

filename = "GOT.txt"
file = open(filename, "r", encoding="utf-8")
text = file.read()

# Reemplazar saltos de línea por espacios
text = text.replace("\n", " ")
print(text)

# Tokenizar el texto:
words = nltk.tokenize.word_tokenize(text)


# Eliminar los stopwords:
words = [word for word in words if word.lower() not in stopwords]
print(words)


