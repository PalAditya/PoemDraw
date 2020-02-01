import spacy
from spacy import displacy
from collections import Counter
from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint
import en_core_web_sm
from IPython.display import display, HTML
nlp = en_core_web_sm.load()
def url_to_string(url):
	res = requests.get(url)
	html = res.text
	soup = BeautifulSoup(html, 'html5lib')
	for script in soup(["script", "style", 'aside']):
		script.extract()
	return " ".join(re.split(r'[\n\t]+', soup.get_text()))
"""ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
article = nlp(ny_bb)
print(len(article.ents))
labels = [x.label_ for x in article.ents]
#Counter(labels)
items = [x.text for x in article.ents]
print(Counter(items).most_common(3))
sentences = [x for x in article.sents]
print(sentences[20])"""
#displacy.render(nlp(str(sentences[20])), jupyter=True, style='ent')
#image = displacy.render(nlp(str(sentences[20])), style='dep', jupyter = False, options = {'distance': 120})
sent = "I had Everest to my left and Caspian Sea below, thought Susan"
image = displacy.render(nlp(sent), style='dep', jupyter = False, options = {'distance': 120})
with open("a.html","w") as f:
	f.write(image)