import pandas as pd

files = {
    "PG": '1094591345_us.csv',
    "Giant": '1536111825_us.csv',
    "Trek": '1609966547_us.csv',
    "Shimano": '1437969979_us.csv',
    "Ninebot US": '1484302191_us.csv'
}

def sentiment_from_rating(rating):
    if rating > 3:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"


for label, file_path in files.items():
    print(f"Processing {label}...")

    df = pd.read_csv(file_path)

    if "rating" not in df.columns:
        print("  ⚠ No rating column found. Skipping.")
        continue

    # Overwrite sentiment column (English only)
    df["sentiment"] = df["rating"].apply(sentiment_from_rating)

    # Remove sentiment_en if exists
    if "sentiment_en" in df.columns:
        df.drop(columns=["sentiment_en"], inplace=True)

    # Save back to original file
    df.to_csv(file_path, index=False)

    print(f"  ✓ sentiment normalized and sentiment_en removed\n")


