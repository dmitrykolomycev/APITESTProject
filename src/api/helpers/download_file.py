def download_file(filename: str, file_content):
    with open(filename, 'wb') as file:
        file.write(file_content)