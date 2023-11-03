"""
Psalm PreLoader. Simple script that prepares all psalms (373 psamls sorted alphabetically)
to be loaded to OrionGT Controller.
"""
import os
import subprocess
import shutil
from pathlib import Path

with open("psalms.txt", "r", encoding="UTF-8") as f:
    lines = f.read().splitlines()

tmp_output_dir = "psalms_tmp"
output_dir = "formatted_psalms"
os.makedirs(tmp_output_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

nb_of_full_files = int(len(lines) / 15)
chunks = []
for x in range(nb_of_full_files):
    lines_per_file = [line + "\n\n" for line in lines[x * 15:(x+1) * 15]]
    chunks.append(lines_per_file)
chunks.append([line + "\n\n" for line in lines[nb_of_full_files * 15:]])
for chunk in chunks:
    begin = chunk[0][:2].strip()
    end = chunk[-1][:2].strip()
    if begin == end:
        begin = chunk[0][:7].strip()
        end = chunk[-1][:7].strip()
    filename = os.path.join(tmp_output_dir, f"{begin}-{end}.txt")
    with open(filename, "w", encoding="UTF-8") as f:
        f.writelines(chunk)

for idx, tmp_file in enumerate(Path(tmp_output_dir).iterdir()):
    subprocess.call(["python3",  "format_lyrics.py", "--input_file",  str(tmp_file),
                     f"{tmp_file.stem}",  "--output_file",
                     os.path.join(output_dir, f"{idx:02d}.TXT")])

shutil.rmtree(tmp_output_dir)
