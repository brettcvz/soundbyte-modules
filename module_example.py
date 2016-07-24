import time

example_variable = True


def start(card_id, card_data):
    """
    Called when this module should start executing.

    If there is an error starting this module, this function
    should throw an appropriate exception.

    This function is run on a background thread, and should not
    return until the module is finished running -- which could be
    an indefinite amount of time until stop() is called, such
    as a song on loop.
    """
    while example_variable:
        print "Hello World"
        time.sleep(1.0)


def stop():
    """
    Called when this module should stop executing and clean
    up any currently used resources
    """
    global example_variable
    example_variable = False

    print "Goodbye World"
