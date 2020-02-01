'''A File to generate a large number of sentences
with keywords related to natural phenomena, used for training.
The subset of nature we would be looking at is as follows:
a) Green fields/plains b)Sunrise c)Mountains(Snow capped/Otherwise) d) Rivers
e) Ocean and beaches f)Flowers d)Storms (Phase 2)
'''

import json
import random
from pprint import pprint

keywords=["green plains","green plain","blue skies", "cloudy sky", "clear sky",
"bright sun","scorching sun", "full daylight","sunlight","tall mountains",
"high hills","rocky hills", "steep mountains","snow-capped peaks","sloshing ocean",
"vast sea","sunny sky","frozen fields","blue sea","rippling waters","sea",
"sky","ocean","plain","meadows","dusky sky","fog","foggy sky","misty sky","mist",
"raging river","river","river currents","stream","blue streams","barren plateau",
"setting sun","rising sun","dawn","dusk","midday","rolling mist","majestic mountains",
"moonlit night","steep peaks", "salt water", "fresh water", "muddy water", "tree brunch",
"wide valley", "yawning valley", "fluffy cloud", "creamy clouds", "dark clouds",
"stormy clouds", "raindrops","pitter-patter", "birds", "tigers", "lions", "gold leaves",
"blue summer skies","day", "forest","squirrel", "sun", "moon", "sunrise", "moonlight"]

sentence_list = ["I looked at the {} and realized with a smile that they reminded me of {}",
				"The {} was sure fine to look at, but the beauty of {} wasn't any less either",
				"Looking at the {} made me wonder if it was better than {}",
				"There's not much to look here other than {} and {}",
				"I can't believe I was seeing such a scenic beauty comprised of {} and {}",
				"I guess the {} really took the cake as it outshone {}",
				"Isn't it little things in nature like {} and {} that make life worth living?",
				"Seeing either {} or {} does put a smile to my face",
				"Both {} and not to mention, {} always was charming to see",
				"My vision was briefly obscured by {}-not unlike how it might happen with {}",
				"Are {} and the plain {} only things this region has to offer?",
				"There was no way I was leaving without having seen {}, given that {} was already off my checklist",
				"It is annoying to think that simple things like {} and {} could make such an impact on my mind",
				"{} is a beauty as always, but {} has become another subject for poets to gush about",
				"It is strange that someone could like {}, yet despise {}",
				"I am ready to sacrifice anything if I get to see anything like {} again-{} last year was not nearly enough",
				"Would you rather see {} or marvel at {}?",
				"Nature seems to love symmetry-{} and {} are pairs, aren't they?",
				"A thing of beauty is a joy forever-Was that written when he viewed {}, or rather the completely different but no less beautiful {}, one can ony wonder",
				"I guess that {} is my new favourite scenary, replacing {}"]


def getKeywords():
	return keywords

def getSentenceList():
	return sentence_list

viz={}
for i in range (10000):
	a = keywords[random.randint(0, len(keywords) - 1)]
	b = a
	while b == a:
		b = keywords[random.randint(0, len(keywords) - 1)]
	c=random.randint(0,len(sentence_list)-1)
	viz[(i+1)] = {"sentence":sentence_list[c].format(a,b),"features":[a,b]}

with open("E:/BTP/data/sentences/feature_recognition_2.json","w") as f:
	f.write(json.dumps(viz))