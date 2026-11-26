import os

# entry line must stay within the 140-character limit
line = ("Sorry — I heard 'pass the peas' as 'pass the police,' "
        "so dinner is now a crime scene and the peas are in custody.")
assert len(line) <= 140

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
