# PoemDraw: An attempt to generate images automatically which can describe a poem

## Why poemdraw?
- We have had tremendous success in using text-to-image engines as of late, and [StoryGAN]([https://github.com/yitong91/StoryGAN](https://github.com/yitong91/StoryGAN)) is pretty much at the pinnacle of it. The idea is to extend the concept and see if GANs can perform an equally good job on poems.
- Irrespective of success on Step 1, perform comparisons on different poem styles such as **sonnets**, **modern poems** and **haikus**.
- Create a framework-agnostic model, which can be re-implemented in *PyTorch* or *TensorFlow* later for efficiency.

## Indirect dependendices

This project relies heavily on the following projects, and borrows snippets from them. Please refer to each of them if you want to understand some of the unusual imports, which use them as modules

- [StoryGAN]([https://github.com/yitong91/StoryGAN](https://github.com/yitong91/StoryGAN))
- [AttnGAN]([https://github.com/taoxugit/AttnGAN](https://github.com/taoxugit/AttnGAN))
- [iGAN]([https://github.com/junyanz/iGAN](https://github.com/junyanz/iGAN))

## Architecture

It is as below:

![Architecture](https://user-images.githubusercontent.com/25523604/73596766-52aaa400-454b-11ea-9470-eaa96129d61d.PNG)

- The first step is an RNN, which is meant to handle English from different times (mid-1600s to now)
- A tokenizer built on top of TF-IDF, lemmatization and NER will find keywords.
- The sematic layer will find and output a json encoding of the image (in progress). 
Example JSON for sentence *"The mighty mountain lay to the west, beyond the sea"* could be:
```json
{
	"sentence": "The mighty mountain lay to the west, beyond the sea",
	"features": ["mountain", "sea"],
	"mountain": {
		"position": "left",
		"size": "big"
	},
	"sea": {
		"position": "natural",
		"size": "natural"
	}
}
```
- The [GAUGAN](http://nvidia-research-mingyuliu.com/gaugan) tool encoding will be fetched
- The TkInter script will generate a toy image mimicking the one on left panel of GauGAN
- Selenium will complete the pipeline and download the image

## Sample Usage

First, install all dependencies via **pip install -r requirements.txt** . You also need to install the version of chromedriver for your Chrome and place it in a folder named **drivers/** in root. Also, go to [TextRazor](https://www.textrazor.com/) and get your API Key, which is to be substituted in **creds.json** in root folder. Then, migrate to *Codes* and execute the following:

- With a small sentence: *echo YOUR_INPUT_SENTENCE | python tlm.py | python imGen.py && python NVDIA.py*
- With a file/poem: *cat YOUR_INPUT_SENTENCE | python tlm.py | python imGen.py && python NVDIA.py*

You can make any number of modifications, such as increasing the number of features you want to be recognized by migrating to *Codes/Generators/natureDescriptor.py* and editing the keywords list. You can increase the lemmatization length by editing *Codes/module1.py* and generate new data by running *Codes/Generators/datagen.py*. Scraping code for poem is available in *Codes/sonnetExtractor.py*