import json
import pyjson5

class QuteJSON:

    def json_from_file(filename, json5=True):
        """
        Util function to read the json from a file

        :param filename:
        :return:
        """
        fp = open(filename, "r+")
        if json5:
            data = fp.read()
            fp.close()
            return pyjson5.decode(data)

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
        fp = open(filename, "w+")
        print(content, file=fp)
        fp.close()

