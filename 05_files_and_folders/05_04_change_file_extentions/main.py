from pathlib import Path

for file in Path('folder').iterdir():
    new_filename = file.stem + '.csv'
    new_filepath = file.with_name(new_filename)
    file.rename(new_filepath)