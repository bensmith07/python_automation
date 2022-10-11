import pathlib

root_dir = pathlib.Path('folder')

for path in root_dir.glob('*.csv'):
    with open(path, 'wb') as file:
        file.write(b'')
    path.unlink()
