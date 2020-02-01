import random
import webbrowser
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def preprocess(text):
	text=text.lower()
	return text
	
def getStopWords(filepath):
	with open(filepath,"r") as f:
		s=f.readlines()
		stop_set=set(m.strip() for m in s)
		return frozenset(stop_set)

def sort_coo(coo_matrix):
	tuples = zip(coo_matrix.col, coo_matrix.data)
	return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
	sorted_items = sorted_items[:topn]

	score_vals = []
	feature_vals = []

	for idx, score in sorted_items:
		fname = feature_names[idx]
		score_vals.append(round(score, 3))
		feature_vals.append(feature_names[idx])
		
	results= {}
	for idx in range(len(feature_vals)):
		results[feature_vals[idx]]=score_vals[idx]
	
	return results

sentence = input("Enter sentence: ").lower()
sentence = sentence.split(" ")
prefix = "file:///E:/BTP/Codes/Images/"
mountain = "mountain"
sky = "sky"
plains = "plains"
r=random.randint(1,3)

df_idf=pd.read_json("custom_dataset.json",orient='records',encoding="utf8")
df_idf['sentence']=df_idf['sentence'].apply(lambda x:preprocess(x))
stopwords=getStopWords("stopwords.txt")

docs=df_idf['sentence'].tolist()
cv=CountVectorizer(max_df=0.85, stop_words=stopwords)
word_count_vector=cv.fit_transform(docs)

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)

df_test=pd.read_json("custom_test.json",orient='records',encoding="utf8")
df_test['sentence']=df_test['sentence'].apply(lambda x:preprocess(x))
docs_test=df_test['sentence'].tolist()

feature_names=cv.get_feature_names()
text=[]
for doc in docs_test:
	tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))
	sorted_items=sort_coo(tf_idf_vector.tocoo())
	keywords=extract_topn_from_vector(feature_names,sorted_items,10)
	'''print(doc)
	for k in keywords:
		print(k,keywords[k])'''
	temp_text=[k for k in keywords]
	text.append(temp_text)
print(text)
