import pathlib
import zipfile

root_dir = pathlib.Path('folder')

for path in root_dir.glob('*.zip'):
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = root_dir / path.stem
        zf.extractall(path=final_path)
