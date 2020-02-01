import random
import webbrowser

sentence = input().lower()
sentence = sentence.split(" ")
prefix = "file:///E:/BTP/Codes/Images/"
mountain = "mountain"
sky = "sky"
plains = "plains"
r=random.randint(1,3)

if mountain in sentence and sky in sentence and plains in sentence:
	filename=prefix+'blueSkyMountainMeadows/'+str(r)+'.png'
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(filename)
elif mountain in sentence and sky in sentence and plains not in sentence:
	filename=prefix+'blueSkyMountain/'+str(r)+'.png'
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(filename)
elif mountain in sentence and sky not in sentence and plains in sentence:
	filename=prefix+'mountainMeadows/'+str(r)+'.png'
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(filename)
elif mountain in sentence and sky not in sentence and plains not in sentence:
	filename=prefix+'mountain/'+str(r)+'.png'
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(filename)
else:
	print("Basic model failed :(")