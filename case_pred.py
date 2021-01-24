import streamlit as st
from sklearn import datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
import advertools as adv
from nltk.stem.snowball import SnowballStemmer
nltk.download('omw')

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
import string

from nltk.corpus import stopwords
import advertools as adv

lemmatizer = WordNetLemmatizer()
english_tagalog_stopwords = stopwords.words('english') + sorted(adv.stopwords['tagalog'])

def nltk2wn_tag(nltk_tag):
  if nltk_tag.startswith('J'):
    return wordnet.ADJ
  elif nltk_tag.startswith('V'):
    return wordnet.VERB
  elif nltk_tag.startswith('N'):
    return wordnet.NOUN
  elif nltk_tag.startswith('R'):
    return wordnet.ADV
  else:                    
    return None

def lemmatize_sentence(sentence):
  nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))    
  wn_tagged = map(lambda x: (x[0], nltk2wn_tag(x[1])), nltk_tagged)

  res_words = []
  for word, tag in wn_tagged:
    if(word in string.punctuation):
      continue
    if(tag == 'NNP'):
      continue
    if tag is None:                        
      res_words.append(word)
    else:
      res_words.append(lemmatizer.lemmatize(word, tag))

  return res_words

tlm_analyzer_2 = TfidfVectorizer(max_features=2000,ngram_range=(1,2),tokenizer=lemmatize_sentence,stop_words=english_tagalog_stopwords).build_analyzer()

def tlm_2(doc):
    return (w for w in tlm_analyzer_2(doc) if w not in string.punctuation)

st.title("Case Prediction Tool")
st.info('Curious about this tool? Find more details @ github.com/shebna12/case-prediction-tool')
user_input = st.text_input("Paste your case text here.", "")
if(len(user_input) == 0):
	st.error("Please input your text")
else:
	with st.spinner('Wait for it...'):
		vectorizer = joblib.load('tfidf_vectorizer.pkl')
		test_features = vectorizer.transform([user_input])

		model = joblib.load('model.pkl')
		y_preds = model.predict(test_features)

		st.write('The AI tool predicted that this case will be: ',y_preds[0])
	st.success('Done!')
	if(y_preds == 'affirmed'):
		st.balloons()
