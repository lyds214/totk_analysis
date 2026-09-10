import requests
import pandas as pd


def fetch_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def normalize_json(data):
    df = pd.json_normalize(data)
    return df


def main():
    data = fetch_api('https://radar-totk.zeldamods.org/objs/MainAndMinusField/?q=Enemy_Chuchu_Junior&withMapNames=false&limit=2000')
    df = normalize_json(data)
    df.to_csv("chuchus.csv", index=False)

if __name__ == "__main__":
    main()