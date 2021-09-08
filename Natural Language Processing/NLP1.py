import nltk
from nltk import punkt


#sentence token
from nltk.tokenize import sent_tokenize
text="Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue. You shouldn't eat cardboard"
tokenized_text=sent_tokenize(text)
print("")
print("Tokenized Sentence \n",tokenized_text)

print("")

#word Token
from nltk import word_tokenize
tokenized_word=word_tokenize(text)
print("Tokenized words \n",tokenized_word)

print("")

#freq dist
from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print("Frequency distribution \n",fdist)

print("")

print("Most common 3 words \n",fdist.most_common(3))

print("")

#Freq dist plot
import matplotlib.pyplot as plt
# fdist.plot(30,cumulative=False)
# plt.show()

print("")

from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print("Stopword in the module are \n",stop_words)

print("")

#removing Stop words
filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Words \n",tokenized_word)
print("Filtered Words \n",filtered_sent)
