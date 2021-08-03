import os
import csv
from ..log import log

def read_from_csv(filename, headers, delimiter=","):
    """
    This function reads the content from a csv file, checks if the headers are correct
    and returns the content in a json-object ordered by supplier_id

    :param filename:
    :param headers:
    :return: object
    """

    if not os.path.isfile(filename):
        log("Fatal error", "File {0} does not exist.".format(filename))
        exit(1)

    ####################################
    ### READ THE INPUT FROM THE FILE ###
    ####################################
    reader = csv.DictReader(open(filename, "r", encoding="utf-8-sig"), delimiter=delimiter)

    # VALIDATE FIELDNAMES
    if not len(reader.fieldnames) == len(headers) or reader.fieldnames != headers:
        log(
            "Fatal error",
            "Incorrect CSV format: ensure to match given headers",
        )
        import pprint
        pprint.pprint(headers)
        pprint.pprint(reader.fieldnames)
        exit(1)
    res = []
    for line in reader:
        res.append(line)
    return res


def write_to_csv(resultset, filename, headers=False):
    """
    Write the resulset into a file

    :param resultset: dictionary
    :param filename: filename
    :return: None
    """
    if not headers:
        headers = collect_headers(resultset)

    with open(filename, "w+") as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(headers)

        for i_r in resultset:
            csv_w.writerow(map(lambda x: i_r.get(x, ""), headers))


def collect_headers(resultset):
    """
    Get all common headers from the resultset

    :param resultset: list
    :return:
    """
    headers = []
    for row in resultset:
        headers += list(row.keys())

    return list(set(headers))
