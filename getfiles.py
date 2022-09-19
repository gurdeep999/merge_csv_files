import os

def get_files():
    filenames = []
    for x in os.listdir('tomerge'):
        if x.endswith('csv'):
            filenames.append(f"tomerge/{x}")
    return filenames
