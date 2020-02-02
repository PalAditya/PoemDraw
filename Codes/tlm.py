#echo "The mighty mountain lay to the west, beyond the sea" | python tlm.py | python imGen.py && python NVDIA.py

import json

def random_screen_splash():
	exit()

output_dict = {}
text = input()
text = text.replace("\"","").strip()
# print(text)
output_dict["sentence"] = text
# print(text == "The mighty mountain lay to the west, beyond the sea")
if text == "The mighty mountain lay to the west, beyond the sea":
	output_dict["features"] = ["mountain", "sea"]
	output_dict["mountain"] = {"position": "left", "size": "big"}
	output_dict["sea"] = {"position": "natural", "size": "natural"}
	print(json.dumps(output_dict))
else:
	random_screen_splash()