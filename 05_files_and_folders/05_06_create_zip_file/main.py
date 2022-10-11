from pathlib import Path
import zipfile

root_dir = Path('folder')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob('*.txt'):
        zf.write(path)
        # path.unlink() # if you want to delete the original file
