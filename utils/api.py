import requests
import pandas as pd

def fetch_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def normalize_json(data):
    df = pd.json_normalize(data)
    return df