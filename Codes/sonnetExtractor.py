from bs4 import BeautifulSoup
import requests
import json
import random


user_agent_list = [
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
			"Chrome/72.0.3626.121 Safari/537.36",
			"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) "
			"Chrome/19.0.1084.46 Safari/536.5",
			"Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) "
			"Chrome/19.0.1084.46 Safari/536.5",
		]
headers = {
			"Cache-Control": 'no-cache',
			"Connection": "keep-alive",
			"User-Agent": random.choice(user_agent_list),
		}

def shakespeare():
	base_url = "https://williamshakespearefacts.com/sonnets/sonnet-"
	to_write = dict()
	for i in range (1, 155):
		url = base_url + str(i)
		r = requests.get(url)
		sonnet = dict()
		sonnet["features"] = list()
		if r.status_code == 200:
			text = r.text
			parsed = BeautifulSoup(text, "html.parser")
			req = parsed.find("div", class_ = "maincontent").find_all("p")
			count = 0
			poem = ""
			for line in req:
				poem += line.text
				count += 1
				if count == 14:
					break
				poem += "\n"
			print("Done " + str(i))
			sonnet["sentence"] = poem
			to_write[i] = sonnet
			print("\n\n")

	with open("a.json", "w") as f:
		f.write(json.dumps(to_write, sort_keys=True, indent=4))

def keats():
	base_url = "http://keats-poems.com/"
	to_write = dict()
	r = requests.get(base_url + "poems/sonnets/", headers = headers)
	text = r.text
	parsed = BeautifulSoup(text, "html.parser")
	req = parsed.select("div.entry-content.clearfix")[0].find_all("li")
	count = 1
	for item in req:
		sonnet = dict()
		sonnet["features"] = list()
		soup = requests.get(item.find("a").get('href'), headers = headers).text
		soup = BeautifulSoup(soup, "html.parser")
		poem = soup.select("div.entry-content.clearfix")[0].find_all('h4')
		for sentence in poem:
			if len(sentence.text) > 10:
				sonnet["sentence"] = sentence.text
				break
		to_write[count] = sonnet
		print("Done " + str(count))
		count += 1
		if count == 31:
			break

	with open("a.json", "w") as f:
		f.write(json.dumps(to_write, sort_keys=True, indent=4))

#shakespeare()
#keats()