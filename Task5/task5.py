import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# Tokenization
word_data = "India Is The Second Most Populated Country After China And The Fourth Largest Economy After China  Other Two Are USA, Russia"
nltk_tokens = nltk.word_tokenize(word_data)
print("Word Tokenization:", nltk_tokens)
sentence_data = "India Is The Second Most Populated Country. After China. And The Fourth Largest Economy After China.  Other Two Are USA, Russia. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print("\nLine Tokenization:", nltk_tokens)

# #Lower casing
def lower_text(text):
  text = text.lower()
  return text
text = "India Is The Second Most Populated Country After China And The Fourth Largest Economy After China  Other Two Are USA, Russia."
output_str = lower_text(text)
print("\nLower casing:", output_str)

# Stop words removal
def remove_stopwords(text):
  stop_words = set(stopwords.words('english'))
  tokens = word_tokenize(text)
  result = [i for i in tokens if not i in stop_words]
  return " ".join(result)
inp_str = "NLTK is a leading platform for building Python programs to work with human language data."
opt_str = remove_stopwords(inp_str)
print("\nStop words removal:", opt_str)

# stemming
def stemming(text):
  tokens = []
  stemmer= PorterStemmer()
  tokenize_word=word_tokenize(text)
  for word in tokenize_word:
      tokens.append(stemmer.stem(word))
  return " ".join(tokens)
input_str="There are several types of stemming algorithms."
out = stemming(input_str)
print("\nStemming:", out)

# Lemmatization
def lemmatization(text):
  tokens = []
  lemmatizer=WordNetLemmatizer()
  input_str=word_tokenize(text)
  for word in input_str:
      tokens.append(lemmatizer.lemmatize(word))
  return " ".join(tokens)
text="been had done languages cities mice"
output_str = lemmatization(text)
print("\nLemmatization:", output_str)


