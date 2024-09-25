# Simple Text Editor
import os


def read_file(filename):
    with open(filename, mode="r") as file:
        return file.read()


def write_file(filename, content):
    with open(filename, mode="w") as file:
        if len(content) > 0:
            file.write(content)
            print(f"Data saved!")


def get_user_input():
    file_content = []
    while True:
        line = input()
        if line.upper() == "SAVE":
            break
        file_content.append(line)
    return file_content


def main():
    file_name = input("Enter a file name: ").strip()
    full_path = f"./Simple_Text_Editor/{file_name}"
    try:
        file_exists = os.path.isfile(full_path)
        if file_exists:
            content = read_file(full_path)
            print(content)
        else:
            write_file(full_path, "")
            # print(f"File {file_name} could not be open!")

        file_content = get_user_input()
        write_file(full_path, "\n".join(file_content))
    except OSError as ex:
        print(f"{file_name} could not be open!")


if __name__ == "__main__":
    main()
