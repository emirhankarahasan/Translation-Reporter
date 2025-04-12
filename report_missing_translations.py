import csv
import json

csv_file = "example.csv"
json_file = "strings_tr.json"

try:
    with open(csv_file, "r", encoding="cp1254") as f:
        reader = csv.DictReader(f)
        print("✅ CSV file loaded successfully.")
        print(f"🔍 Found columns: {reader.fieldnames}")

        data = {}
        missing_translations = []
        total_rows = 0
        translated_count = 0

        for row in reader:
            total_rows += 1
            key = row.get("key")
            tr = row.get("tr_text")

            if key:
                if tr:
                    data[key] = tr
                    translated_count += 1
                else:
                    missing_translations.append(key)

    # Write to JSON file
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"\n🎉 Conversion complete → {json_file}")

    # Print missing translations
    if missing_translations:
        print("\n❌ Missing Translations:")
        for key in missing_translations:
            print(f" - {key}")
    else:
        print("✅ All strings are translated!")

    # Print translation statistics
    if total_rows > 0:
        percent = (translated_count / total_rows) * 100
        print(f"\n📊 Translation Statistics:")
        print(f"   - Total entries: {total_rows}")
        print(f"   - Translated: {translated_count} ({round(percent, 2)}%)")
        print(f"   - Missing: {len(missing_translations)} ({round(100 - percent, 2)}%)")

except KeyError as e:
    print(f"❌ ERROR: Column '{e.args[0]}' is missing in your CSV file.")
    print("Please make sure the first row contains: key,text,tr_text")

except FileNotFoundError:
    print(f"❌ ERROR: '{csv_file}' not found. Please check the file name and path.")
