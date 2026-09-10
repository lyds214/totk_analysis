import requests
import pandas as pd
from utils import actor_names


def fetch_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


def normalize_json(data):
    df = pd.json_normalize(data)
    return df


def main():
    output_dir = "data/raw/enemy"

    for monster in actor_names:
        data = fetch_api(f'https://radar-totk.zeldamods.org/objs/MainAndMinusField/?q={monster}&withMapNames=false&limit=2000')
        df = normalize_json(data)
        df.to_csv(f"{output_dir}/{monster}.csv", index=False)

if __name__ == "__main__":
    main()