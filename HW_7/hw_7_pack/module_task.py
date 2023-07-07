from pathlib import Path


def rename_files(path, old_ext, new_ext, new_name):
    directory = Path(path)
    files_to_rename = [i for i in directory.iterdir() if i.suffix[1:] == old_ext]
    for enum, file in enumerate(files_to_rename, start=1):
        Path.rename(file, Path(f"{path}/{file.stem}_{new_name}_{enum}.{new_ext}"))


# if __name__ == '__main__':
#     rename_files('files', 'jpg', 'png', 'image_file')
