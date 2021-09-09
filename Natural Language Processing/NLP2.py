# Preprocessing of text: Word Generation (Stemming , Lemmatiziation, Edit distance)

# Edit Distance

def editdist(str1,str2, m, n):
    #create table to save sol of subprob
    dp=[[0 for x in range(n + 1)] for x in range(m + 1)]
    #       do this            when     this is true

    for i in range(m + 1):
        for j in range(n+1):

            #check if either of string is empty
            if i==0:
                dp[i][j]=j # min operation is j
            elif j==0:
                dp[i][j]=i # min operation is i
            
            #if last chr is same move to 2nd last
            elif str1[i-1] == str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            
            #if all chr are diff
            else:
                dp[i][j]=1+min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                
    print(dp)
    print("")
    return dp[m][n]            

str1="sunday"
str2="saturday"   
print(f"Edit distance between {str1} and {str2} is {editdist(str1,str2,len(str1),len(str2))}")

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

#porter stemmer

from nltk.stem import PorterStemmer

Pstem=PorterStemmer()

stemmed_words=[]
for w in tokenized_word:
    stemmed_words.append(Pstem.stem(w))

print("Filtered sentence : \n",tokenized_word)
print("Stemmed sentence : \n",stemmed_words)
print("")

#lexcion normalization

from nltk.stem.wordnet import WordNetLemmatizer

WNlem=WordNetLemmatizer()
text="Flagged studies studying cries cry"
words=word_tokenize(text)
for i in words:
    print(f"Stemming for {i} is {Pstem.stem(i)}")
print("")
for i in words:
    print(f"Lemma for {i} is {WNlem.lemmatize(i)}")   
