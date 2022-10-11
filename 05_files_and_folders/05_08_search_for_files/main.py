import pathlib

matches = []
search_term = '14'
dir_to_search = '.'

# rglob searches in all subfolders 
for item in pathlib.Path(dir_to_search).rglob('*'):
    if search_term in item.stem:
        matches.append(item.absolute())
for match in matches:
    print(match)
