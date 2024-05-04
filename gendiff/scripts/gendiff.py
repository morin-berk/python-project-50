import argparse
import json
import os


def generate_diff(file1, file2):
    result = "{\n"
    file1_path, file2_path = os.path.abspath(file1), os.path.abspath(file2)
    dict1, dict2 = json.load(open(file1_path)), json.load(open(file2_path))
    united_dict = dict(sorted({**dict1, **dict2}.items()))
    for key in united_dict.keys():
        if key in dict1 and key in dict2 and dict1[key] == dict2[key]:
            result += "  " + f"{key}: {dict1[key]}" + "\n"
        elif key in dict1 and key in dict2:
            result += "- " + f"{key}: {dict1[key]}" + "\n"
            result += "+ " + f"{key}: {dict2[key]}" + "\n"
        elif key in dict1:
            result += "- " + f"{key}: {dict1[key]}" + "\n"
        elif key in dict2:
            result += "+ " + f"{key}: {dict2[key]}" + "\n"
    result += "}"
    return result


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first file')
    parser.add_argument('second file')
    parser.add_argument('-f', "--format", help="set format of output")

    args = vars(parser.parse_args())
    gendiff = generate_diff(args["first file"], args["second file"])
    print(gendiff)


if __name__ == "__main__":
    main()
