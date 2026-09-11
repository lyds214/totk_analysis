from pathlib import Path

from utils.api import fetch_api, normalize_json
from utils.data import material_names

OUTPUT_DIR = Path('data/raw/materials')

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for material in material_names:
        url = f"https://radar-totk.zeldamods.org/objs/MainAndMinusField/?q={material}_Upper&withMapNames=false&limit=2000"
        data = fetch_api(url)
        df = normalize_json(data)

        output_file = OUTPUT_DIR / f"{material}.csv"
        df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()