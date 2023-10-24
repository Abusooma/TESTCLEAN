from pathlib import Path
import re


def cleaner(char):
    return re.sub(r'[^a-zA-Z\s]', "", char)


def read_name(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def write_clean_names(output_file, names):
    with open(output_file, "w") as f:
        return f.write("\n".join(names))


# sourcery skip: remove-str-from-print
BASE_DIR = Path(__file__).parent.parent
FILE_DIR = BASE_DIR / "liste_des_noms.txt"
OUTPUT_FILE = BASE_DIR / "list_name_cleans.txt"
try:
    names = read_name(FILE_DIR)
    liste_names = [cleaner(name.strip()) for name in names]
    output_file = write_clean_names(OUTPUT_FILE, liste_names)
except FileNotFoundError:
    print("Le fichier est introuvable..!")
except Exception as e:
    print("Une erreur est survenue..", str(e))
