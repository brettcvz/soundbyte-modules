import time

example_variable = True


def start():
    """
    Called when this module should start executing.

    If there is an error starting this module, this function
    should throw an appropriate exception
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
