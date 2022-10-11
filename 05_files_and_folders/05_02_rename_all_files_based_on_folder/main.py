from pathlib import Path

folders = Path('files').iterdir()
for folder in folders:
    files = Path(folder).iterdir()
    for file in files:
        new_filename = folder.stem.lower() + '_' + file.stem + file.suffix
        # new_filename = file.stem[-3:] + file.suffix 
        new_filepath = file.with_name(new_filename)
        file.rename(new_filepath)

    