#import requests
#import json
#
#var=requests.get("https://fr-en.openfoodfacts.org/category/pizzas/1.json")
#var=json.loads(var.text)
#for product in var["products"]:
#    print (json.dumps(product,indent=2))

from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    iam_apikey='ZZbg4XfO6aA1lh2U1SopkxbR5Ti2oo3VHZXt-zjdbV84',
    url='https://gateway-syd.watsonplatform.net/text-to-speech/api'
)

escanor_bio = open("escanor_bio.txt","r")

with open('escanor_bio.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            escanor_bio.read(),
            'audio/wav',
            'en-US_MichaelVoice'
        ).get_result().content)