# Continuous output logger.

def log(state, msg=False, timerobj=False):
    """
    Print a left padded line

    :param state:
    :param msg:
    :param timerobj: Timer
    :return:
    """
    if state == "separator":
        print()
        print("---------------------------------------------------------")
        print()
        return
    if timerobj:
        msg = "{0} ({1})".format(
            msg, timerobj.get_offset(format="{M:02}m {S:02.00f}s {mS:03}ms")
        )
    print(state.upper().ljust(12) + ": " + msg)

