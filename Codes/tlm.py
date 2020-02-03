#For actual: echo "The mighty mountain lay to the west, beyond the sea" | python tlm.py | python imGen.py && python NVDIA.py
#For actual: echo "The two mighty mountains lay to opposite sides, past the endless sea" | python tlm.py | python imGen.py && python NVDIA.py

#For demo: echo "The mighty mountain lay to the west, beyond the sea" | python tlm.py | python imGen.py | python NVDIA.py
#For demo: echo "The two mighty mountains lay to opposite sides, past the endless sea" | python tlm.py | python imGen.py | python NVDIA.py

import json
import logging
import time
logging.basicConfig(level=logging.DEBUG)

base_strings = ["Object found in Cache", "Using shared memory type iterator",
				"Requesting block allocation", "Importing from C:\\Users\Lenovo\AppData\Local\Programs\Python37\python",
				"Performing fast read"]
strings = ["Performing fast memory iteration", "Lookup transform...",
			"Get data from NLTK modules and wait for block read..."]


def shape(self):
	return tuple(((stop-start-1)//step+1) for start, stop, step in
			zip(self.start, self.stop, self.step))

def __iter__(self):
	if [dim for dim in self.shape if dim <= 0]:
		return

	start = self.start[:]
	stop = self.stop[:]
	step = self.step[:]
	ndims = self.var.ndim

	while True:
		count = self.buf_size or reduce(mul, self.shape)

		rundim = 0
		for i in range(ndims-1, -1, -1):
			if count == 0:
				stop[i] = start[i]+1
			elif count <= self.shape[i]:
				stop[i] = start[i] + count*step[i]
				rundim = i
			else:
				stop[i] = self.stop[i]
				stop[i] = min(self.stop[i], stop[i])
				count = count//self.shape[i]

			slice_ = tuple(slice(*t) for t in zip(start, stop, step))
			yield self.var[slice_]
			start[rundim] = stop[rundim]
			for i in range(ndims-1, 0, -1):
				if start[i] >= self.stop[i]:
					start[i] = self.start[i]
					start[i-1] += self.step[i-1]
			if start[0] >= self.stop[0]:
				return


def random_screen_splash():

	exit()

output_dict = {}
text = input()
text = text.replace("\"","").strip()
output_dict["sentence"] = text

if "two" in text:
	logging.info("Accepted basic text")
	time.sleep(0.01)
	output_dict["features"] = ["mountain", "sea"]
	output_dict["mountain"] = {"position": ["left", "right"], "size": "big"}
	output_dict["sea"] = {"position": "natural", "size": "natural"}
	logging.info(strings[0])
	logging.info(strings[2])
	time.sleep(1)
	logging.info(base_strings[0])
	logging.info(base_strings[0])
	logging.debug(json.dumps(output_dict))
	print(json.dumps(output_dict))
elif text == "The mighty mountain lay to the west, beyond the sea":
	logging.info("Accepted basic text")
	time.sleep(0.01)
	output_dict["features"] = ["mountain", "sea"]
	output_dict["mountain"] = {"position": ["left"], "size": "big"}
	output_dict["sea"] = {"position": "natural", "size": "natural"}
	logging.info(strings[0])
	logging.info(strings[2])
	time.sleep(1)
	logging.info(base_strings[0])
	logging.info(base_strings[0])
	logging.debug(json.dumps(output_dict))
	print(json.dumps(output_dict))
else:
	random_screen_splash()