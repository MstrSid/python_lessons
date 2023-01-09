from pathlib import Path
from datetime import datetime
import json

path = Path('D:/for tests/')
files = {}
for i, item in enumerate(path.iterdir()):
    if item.is_file():
        size = item.stat().st_size / 1024
        name = item.name
        access_time = datetime.fromtimestamp(item.stat().st_mtime).replace(microsecond=0)
        mod_time = datetime.fromtimestamp(item.stat().st_mtime).replace(microsecond=0)
        files[i] = {
            'name': name,
            'size': size,
            'l_mod_time': str(mod_time),
            'l_acc_time': str(access_time),
        }
data_json = json.dumps(files, indent=2, ensure_ascii=False)
print(data_json)
