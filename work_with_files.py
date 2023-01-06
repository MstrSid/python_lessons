# Create folder files.
# In folder create files first.txt and second.txt. Write in files some text lines.
# Read all strings from first file.
# Read string-to-string from second files.
# Remove both files
# Remove files folder

from pathlib import Path

directory = Path('.').joinpath('files')
if not directory.exists():
    directory.mkdir()

file1 = Path(f'{directory}/first.txt')
file2 = Path(f'{directory}/second.txt')

with open(file1, 'w') as file_one:
    file_one.write("String 1\n")
    file_one.write("String 2\n")
    file_one.write("String 3")

with open(file2, 'w') as file_two:
    file_two.write("String 1_1\n")
    file_two.write("String 2_2\n")
    file_two.write("String 3_3")

with open(file1) as file_r:
    print(file_r.read())

with open(file2) as file_r2:
    while True:
        line = file_r2.readline()
        if not line:
            break
        print(line)

if file1.exists():
    file1.unlink()

if file2.exists():
    file2.unlink()

if directory.exists():
    directory.rmdir()
