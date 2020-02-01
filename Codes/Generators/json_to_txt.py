import json

with open("E:/BTP/data/sentences/feature_recognition_2.json","r") as f:
	r=f.read()
r=json.loads(r)

with open("E:/BTP/data/sentences/feature_recognition_2.txt", "w") as f:
	for key, value in r.items():
		f.write(value["sentence"])
		f.write(".\n")
