from pathlib import Path
from zipfile import ZipFile

path = Path('./my_files')
if not path.exists():
    path.mkdir()

path_zip = Path('./my_files_backup')
if not path_zip.exists():
    path_zip.mkdir()

with open(f'{path}/first.txt', 'w') as my_file:
    my_file.write("this is first file")

with open(f'{path}/second.txt', 'w') as my_file:
    my_file.write('this is second file')

with ZipFile(f'{path_zip}/my_files.zip', mode='w') as zip_file:
    for file in Path('./my_files').iterdir():
        zip_file.write(file)

with ZipFile(f'{path_zip}/my_files.zip', mode='r') as zip_file:
    zip_file.extractall(f'{path_zip}')
