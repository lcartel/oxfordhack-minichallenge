import logging

import azure.functions as func

import json 

from googlesearch import search

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    username = req.params.get('username')
    if not username:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            username = req_body.get('username')

    if username:
        data = {}
        for url in search('%s site=*.twitter.com'%username, stop=1):
            data['owner_twitter'] = url

        for url in search('%s site=*.linkedin.com/in*'%username, stop=1):
            data['owner_linkedin'] = url

        for url in search('%s site=*.facebook.com'%username, stop=1):
            data['owner_facebook'] = url

        json_response = json.dumps(data)
        
        return func.HttpResponse(   
            body = json_response,
            status_code = 200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
