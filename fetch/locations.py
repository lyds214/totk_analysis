# https://radar-totk.zeldamods.org/objs/MainAndMinusField/?q=CentralExchange&withMapNames=false&limit=2000

from pathlib import Path

from utils.api import fetch_api, normalize_json
from utils.data import location_names

OUTPUT_DIR = Path('data/raw/locations')

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for loc in location_names:
        url = f"https://radar-totk.zeldamods.org/objs/MainAndMinusField/?q={loc}_Upper&withMapNames=false&limit=2000"
        data = fetch_api(url)
        df = normalize_json(data)

        output_file = OUTPUT_DIR / f"{loc}.csv"
        df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()