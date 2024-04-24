def write_file(file_name, file_content):
    with open(str(file_name) + ".txt", mode="w") as file_name:
        file_name.write(file_content)
    pass

def append_file(file_name, append_content):
    with open(str(file_name) + ".txt", mode="a") as file_name:
        file_name.write(append_content)
    pass

def read_file(file_name):
    with open(str(file_name) + ".txt", mode="r") as file_name:
        return file_name.read()
    pass
