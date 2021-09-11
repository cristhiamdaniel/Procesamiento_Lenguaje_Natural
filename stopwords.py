#!/usr/bin/env python
# coding: utf-8

# # Eliminación de STOPWORDS

# Las Stop Words o palabras vacías, hacen referencia a aquellas palabras que no están registradas por los robots de Google, las cuales carecen de sentido cuando se escriben solas o sin la palabra clave o keyword. 

# In[1]:


# Importamos los módulos necesarios
import csv
import nltk


# In[3]:


csv_file="stopwords.csv"


# In[4]:


with open(csv_file, 'r', encoding='utf-8') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    stopwords = [row[0] for row in reader]


# In[8]:


print(type(stopwords))


# In[9]:


# Forma alterna usando NLTK
stopwords_2 = nltk.corpus.stopwords.words('english') # Para inglés


# In[11]:


# imprimir los primeros 5 elementos de la lista:
print(stopwords_2[0:5])


# In[12]:


filename = "GOT.txt"
file = open(filename, "r", encoding="utf-8")
text = file.read()


# In[15]:


text = text.replace("\n", " ")
text


# In[17]:


# Tokenizar el texto:
words = nltk.tokenize.word_tokenize(text)
words


# In[18]:


# Eliminar los stopwords:
words = [word for word in words if word.lower() not in stopwords]
words


# In[ ]:




