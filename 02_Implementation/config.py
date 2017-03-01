"""
gateway point to getting configurations saved in the config.txt file
not using class here because singleton implementations in python appear
to be a lot more complicated to realise than simply doing this without an
OOP focus.

functionality implemented in a way that makes sure the configuration file is
only read from storage once so that disk access is reduced.
"""

import os


configuration = {}
got_configuration = False

base_configurations = []

def get_config():
    raise NotImplementedError
    global configuration
    global got_configuration

    if got_configuration:
        return configuration
    result = {}

    file_directory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(file_directory)
    with open("config.txt") as file:
        got_delimiter = False
        delimiter = ""
        for line in file:
            # skip comment and empty lines
            if line.startswith("$") or len(line) == 0:
                continue

            if not got_delimiter:
                pass
                # TODO


    configuration = result
    got_configuration = True
    return configuration

def extend_configuration(new_info):
    """
    extends the previously fethed configuration data with new items
    will only work after the original configuration has been read from
    config.txt (--> get_config())
    @params:
        new_info: dict to extend configuration with
    @return:
        True if the update was successful, otherwise False
        may be false if configuration has not been fetched or if the
        supplied dict was invalid
    """
    global configuration
    global got_configuration

    if not got_configuration:
        return False

    try:
        configuration.update(new_info)
    except:
        return False
    return True

