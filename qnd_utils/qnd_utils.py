"""Main module."""
from .log import log
from .filehandling import read_from_csv, write_to_csv, ensure_dir, collect_headers

class QuteCSV:

    @staticmethod
    def from_file(filename, headers=None, delimiter=","):
        return read_from_csv(filename, headers, delimiter)

    @staticmethod
    def to_file(filename, resultset, headers=False):
        return write_to_csv(filename, resultset, headers)
