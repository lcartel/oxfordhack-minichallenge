from unittest import result
import requests
import json
import jmespath
import requests

import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    path = jmespath.search

    api_key = "AIzaSyAbspHegRiLSa9EkjpndQXwGSxs6rKdaIg"

    logging.info('Python HTTP trigger function processed a request.')

    place_name = req.params.get('place_name')
    if not place_name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            place_name = req_body.get('place_name')

    if place_name:
        ## #1 Getting the place id using the address name
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyAbspHegRiLSa9EkjpndQXwGSxs6rKdaIg".format(place_name) 

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        y = json.loads(response.text)

        try:
            place_id = jmespath.search('results[].place_id', y)[0]

        except:
            return func.HttpResponse("There is an error on the address !")

        ## #2 Getting info using place id

        url2 = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=name%2Cbusiness_status%2Crating%2Cwebsite%2Cuser_ratings_total%2Creview%2Cformatted_address%2Copening_hours%2Cphotos%2Cinternational_phone_number&key=AIzaSyAbspHegRiLSa9EkjpndQXwGSxs6rKdaIg".format(place_id) 

        payload={}
        headers = {}

        response2 = requests.request("GET", url2, headers=headers, data=payload)

        return func.HttpResponse(response2.text)
        
    else:
        return func.HttpResponse(
             "Call the API with the place_name parameter to get personnalised results",
             status_code=200
        )
