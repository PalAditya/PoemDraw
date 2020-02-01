import json
from Generators.natureDescriptor import getKeywords
import textblob
from datetime import datetime
import random

def scramble(sentence, keywords):
	# Return a scrambled list, but keep keywords together
	l = sentence.split(" ")
	split_keywords = " ".join(keywords).split(" ")
	l = [i for i in l if i not in split_keywords]
	random.shuffle(l)
	for i in keywords:
		ind1 = random.randint(0,len(l)-1)
		l.insert(ind1, i)
	sentence = " ".join(l)
	return sentence

def method1():
	with open("../data/haiku/gen.json") as f:
		r=f.read()

	r=json.loads(r)
	keyWords=getKeywords()
	lemmatized_keywords=[]
	for keyword in keyWords:
		lemmatized_keywords.append(textblob.Word(keyword).lemmatize())

	index=0
	match_found = 0
	for key,value in r.items():
		#value["sentence"] = scramble(value["sentence"],value["features"])
		l=textblob.TextBlob(value["sentence"])

		#print(value["sentence"])
		l1=l.ngrams(n=1)
		l2=l.ngrams(n=2)
		l3=l.ngrams(n=3)
		l1=[" ".join(i) for i in l1]
		l2=[" ".join(i) for i in l2]
		l3=[" ".join(i) for i in l3]
		l=[]
		for i in l1:
			l.append(i)
		for i in l2:
			l.append(i)
		for i in l3:
			l.append(i)

		#print(l)
		found_keywords=[]
		for word in l:
			w = textblob.Word(word)
			if w.lemmatize() in lemmatized_keywords:
				found_keywords.append(w.lemmatize())
		
		print(found_keywords)
		
		actual_keywords = [textblob.Word(i).lemmatize() for i in value["features"]]
		
		print(actual_keywords)

		if found_keywords == actual_keywords or all(elem in found_keywords  for elem in actual_keywords):
			match_found += 1
		"""else:
			print(actual_keywords)
			print(found_keywords)"""
		
		"""index+=1
		if index==10:
			break"""
		
	acc = match_found/len(r)

	with open("Stats.txt","a") as f:
		f.write("Accuracy on feature_recognition_2_5.json is: "+str(acc)+"\n")

	print("Accuracy = ", acc)

startTime = datetime.now()
method1()
print(datetime.now() - startTime)