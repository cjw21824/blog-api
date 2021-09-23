import logging
import os
import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    url = "https://api.twitter.com/2/users/2279555525/tweets"
    logging.info('Python HTTP trigger function processed a request.')
    twitter_bearer_token = os.environ["twitter_bearer_token"]
    headers = {'authorization': f'Bearer {twitter_bearer_token}'}
    r = requests.get(url, headers= headers)
    return func.HttpResponse(
            r.text,
            status_code=200
    )
