from pathlib import Path
import pandas as pd

from utils.api import fetch_api, normalize_json
from utils.data import location_names

OUTPUT_DIR = Path('data/raw/locations')

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    all_locations = []

    for loc in location_names:
        url = f"https://radar-totk.zeldamods.org/objs/MainAndMinusField/?q={loc}&limit=2000"
        data = fetch_api(url)
        df = normalize_json(data)
        all_locations.append(df)

    final_df = pd.concat(all_locations, ignore_index=True)
    output_file = OUTPUT_DIR / f"locations.csv"
    final_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()