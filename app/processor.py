import json
import sys
import os
import requests
import json
import unicodedata
import jmespath
from decimal import Decimal


## USAGE : python3 processor.py ./training_sets/mini_training_set.json

path = sys.argv[1]

with open(path, 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

final_json = []
# f = open("output.json", "x")
# f = open("output.json", "w")
path = jmespath.search

for value in obj:
    business_score = 0
    
    ### BUSINESS TEST

    business_name = value["name"]
    address_name = value["address"]

    r1 = requests.post(
        "https://googleapibackend.azurewebsites.net/api/GetMapsJson",
        data=json.dumps({"place_name": business_name + " " + address_name}),
        headers={"Content-Type": "application/json"},
    )

    y = json.loads(r1.text)

    business_status = jmespath.search('result.business_status', y)
    rating = jmespath.search('result.rating', y)
    number_of_comment = jmespath.search('result.user_ratings_total', y)

    ### OWNER TEST
    # owner = value["owner"]

    # accented_name = owner
    # unaccented_name_nfkd = unicodedata.normalize('NFKD', accented_name) 
    # unaccented_name_byte = unaccented_name_nfkd.encode('ASCII', 'ignore')
    # unaccented_name = unaccented_name_byte.decode("utf-8")

    # r2 = requests.post(
    #     "https://googleapibackend.azurewebsites.net/api/GetGoogleJson",
    #     data=json.dumps({"username": owner}),
    #     headers={"Content-Type": "application/json"},
    # )

    # line = {"ssn":value["ssn"], "business_score": 10.0}

    # r2.text
    # final_json.append(line.copy())$

    if not number_of_comment == None:
        business_score = Decimal(rating)
        if (number_of_comment >= 1 ):
            business_score += 1
        elif (number_of_comment >= 50 ):
            business_score += 2
        elif (number_of_comment >= 100 ):
            business_score += 3
        elif (number_of_comment >= 200 ):
            business_score += 4

    if not business_status.__eq__("OPERATIONAL"):
        business_score = 0

    print("SSN :", value["ssn"], ";", "Business Score : ", business_score)

# print(final_json)