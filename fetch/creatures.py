from pathlib import Path

from utils.api import fetch_api, normalize_json
from utils.data import creature_names

OUTPUT_DIR = Path('data/raw/creatures')

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for creature in creature_names:
        url = f"https://radar-totk.zeldamods.org/objs/MainAndMinusField/?q={creature}_Upper&withMapNames=false&limit=2000"
        data = fetch_api(url)
        df = normalize_json(data)

        output_file = OUTPUT_DIR / f"{creature}.csv"
        df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()