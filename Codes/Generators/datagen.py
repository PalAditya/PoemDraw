"""
This file is used to create a basic set of sentences from which we
will be extracting features later. We will create random sentences 
and save their corresponding features in a hashmap, so that it can be used
to create the training and test model
"""


import markovgen
f = open('small.txt')
markov = markovgen.Markov(f)
l=[]
for i in range (10):
	try:
		l.append(markov.generate_markov_text())
	except:
		pass

f.close()
print(l)


