import os

ALLOWED_EXTENSIONS = {".js", ".jsx", ".html", ".md"}
EXCLUDED_DIRS = {"node_modules"}
OUTPUT_FILE = "merged_all.txt"

def merge_files_from_src_and_readme(output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:

        # --- קודם כל README.md אם קיים ---
        if os.path.isfile("README.md"):
            try:
                with open("README.md", "r", encoding="utf-8") as f:
                    outfile.write("\n--- התחלה של README.md ---\n")
                    outfile.write(f.read())
                    outfile.write("\n--- סוף של README.md ---\n\n")
            except Exception as e:
                print(f"שגיאה בקריאת README.md: {e}")

        # --- עכשיו כל הקבצים מתוך src ---
        for root, dirs, files in os.walk("src"):
            # לדלג על node_modules אם בטעות קיים בפנים
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

            for filename in files:
                ext = os.path.splitext(filename)[1]
                if ext not in ALLOWED_EXTENSIONS:
                    continue

                file_path = os.path.join(root, filename)

                try:
                    with open(file_path, "r", encoding="utf-8") as infile:
                        outfile.write(f"\n--- התחלה של {file_path} ---\n")
                        outfile.write(infile.read())
                        outfile.write(f"\n--- סוף של {file_path} ---\n\n")
                except Exception as e:
                    print(f"שגיאה בקריאת הקובץ {file_path}: {e}")

if __name__ == "__main__":
    merge_files_from_src_and_readme(OUTPUT_FILE)
    print(f"הקובץ המאוחד נוצר בהצלחה בשם: {OUTPUT_FILE}")
