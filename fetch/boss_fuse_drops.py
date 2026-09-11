from pathlib import Path

from utils.api import fetch_api, normalize_json
from utils.data import boss_fuse_drop_names

OUTPUT_DIR = Path('data/raw/boss_fuse_drops')

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for boss_fuse_drop in boss_fuse_drop_names:
        url = f"https://radar-totk.zeldamods.org/objs/MainAndMinusField/?q={boss_fuse_drop}_Upper&withMapNames=false&limit=2000"
        data = fetch_api(url)
        df = normalize_json(data)

        output_file = OUTPUT_DIR / f"{boss_fuse_drop}.csv"
        df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()