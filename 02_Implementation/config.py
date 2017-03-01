"""
gateway point to getting configurations saved in the config.txt file
not using class here because singleton implementations in python appear
to be a lot more complicated to realise than simply doing this without an
OOP focus.

functionality implemented in a way that makes sure the configuration file is
only read from storage once so that disk access is reduced.
"""

configuration = {}
got_configuration = False

base_configurations = []

def get_config():
    global configuration
    global got_configuration

    if got_configuration:
        return configuration
    result = {}



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