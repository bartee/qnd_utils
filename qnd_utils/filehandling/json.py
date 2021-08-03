import json

def json_from_file(filename):
    """
    Util function to read the json from a file

    :param filename:
    :return:
    """
    fp = open(filename, "r+")
    json_content = json.load(fp)
    fp.close()
    return json_content


def json_to_file(filename, content):
    """
    Write content to file

    :param filename:
    :param content:
    :return:
    """
    print("writing to " + filename)
    fp = open(filename, "w+")
    print(content, file=fp)
    fp.close()
