from pathlib import Path
from datetime import datetime
folder = 'files'
subfolders = Path(folder).iterdir()
for subfolder in subfolders:
    files = Path(subfolder).iterdir()
    for file in files:
        stats = file.stat()
        seconds_created = stats.st_ctime
        date_created = datetime.fromtimestamp(seconds_created)
        date_created = date_created.strftime('%Y%m%d_%H:%M:%S')
        new_filename = date_created + '_' + file.stem + file.suffix
        # new_filename = file.stem[-3:] + file.suffix 
        new_filepath = file.with_name(new_filename)
        file.rename(new_filepath)