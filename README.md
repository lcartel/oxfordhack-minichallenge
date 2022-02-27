# Oxford hack mini challenge

See the full challenge brief, prizes and deadline at https://saltpay.co/oxfordhack.

Fork this repostory and fill out your details below:

**Prerequisites** : 
- Azure Account
- pip3, Python3
- Azure Function extension / Azure Function Core

**Architecture of folders** :
- processor.py : main application
- /GetGoogleJson : Google Search API
- /GetMapsJson : Google Maps API

**URL of the APIs** : 

*Google Map Api* : 

url : https://googleapibackend.azurewebsites.net/api/GetMapsJson

input param : {"place_name": "32 jump street"}

*Google Search Api* : 

url : https://googleapibackend.azurewebsites.net/api/GetGoogleJson

input param : {"username": Mickael Jordan}

**Run the application** :
- $> cd app 
- $> python3 processor.py ./training_sets/mini_training_set.json


## Your details

- Name: Léo Cartel, Amrit Sahani

