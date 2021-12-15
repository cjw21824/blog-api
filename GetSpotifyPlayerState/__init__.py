import logging
import os
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    url = "https://api.spotify.com/v1/me/player"
    logging.info('Python HTTP trigger function processed a request.')
    spotify_bearer_token = os.environ["spotify_bearer_token"]
    headers = {'authorization': f'Bearer {spotify_bearer_token}'}
    r = requests.get(url, headers= headers)
    return func.HttpResponse(
            r.text,
            status_code=200
    )

