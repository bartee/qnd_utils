import pathlib

def ensure_dir(dirname):
    """
    Ensure that a dirtree exists

    :param dirname:
    :return:
    """
    pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
