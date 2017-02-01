def when_finished(dec):
    """ just a more canonical way to wrap with default settings, IMO

    :param dec: the decorator to wrap (one of the decorators in `im_finished.decorators`)
    :return: `func` the decorator with default settings applied
    """
    def wrapper(fn):
        return dec()(fn)

    return wrapper