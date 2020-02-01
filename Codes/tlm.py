import json

def random_screen_splash():
	exit()

output_dict = {}
text = input()[1:-2]
output_dict["sentence"] = text
if text == "The mighty mountain lay to the west, beyond the sea":
	output_dict["features"] = ["mountain", "sea"]
	output_dict["mountain"] = {"position": "left", "size": "big"}
	output_dict["sea"] = {"position": "natural", "size": "natural"}
	print(json.dumps(output_dict))
else:
	random_screen_splash()